
from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "https://ipsi.chungbuk.ac.kr:5443/pub/board/"
    notice_url = "bbs_free.html?cboardID=cumm110101"
    html = await fetch(session, prefix_url + notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()
    for notice in bs.find_all('table')[2].find_all('tr'):
        anchor = notice.find('a')
        link = anchor.attrs['href']
        data = univ_info2dict("충북대", anchor.text.strip(), prefix_url, link)
        notice_list.append(data)
    return notice_list
