import importlib
import aiohttp
import asyncio
import sys

import time

import datetime

import settings
import univs
import itertools

from database import db, engine
from models import Notice

from mail.gmail import GMail, Message

if sys.argv[1] == 'init':
    from database import Base
    from models import *

    Base.metadata.create_all(engine)

if sys.argv[1] == 'crawl':
    async def fetch_all(loop, univs):
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(loop=loop, connector=conn) as session:
            fetches = [asyncio.Task(univ(session)) for univ in univs]
            result = await asyncio.gather(*fetches, return_exceptions=True)
            return itertools.chain(*result)


    sender = GMail(settings.GMAIL_ID, settings.GMAIL_PW)

    loop = asyncio.get_event_loop()
    notices = loop.run_until_complete(fetch_all(loop,
                                                [importlib.import_module('univs.' + module).get_list for module in
                                                 univs.__all__],
                                                sender))

    while True:

        try:
            dict_notice = next(notices)
        except StopIteration:
            break

        if not isinstance(dict_notice, dict):
            continue

        try:
            notice = Notice(**dict_notice)
            db.add(notice)
            db.commit()

            sender.send(Message('[%s] %s' % (notice.univ, notice.title),
                                to="curzy@move.is",
                                text=notice.link))

        except Exception as e:  # Duplicate Error
            db.rollback()

    sender.close()
