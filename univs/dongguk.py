from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "https://ipsi.dongguk.edu"
    notice_url = prefix_url + "/help/notice_list.jsp?notiType=A"
    html = await fetch(session, notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()
    for notice in bs.find('tbody').find_all('tr'):
        anchor = notice.find('a')
        data = univ_info2dict("동국대", anchor.text.strip(), prefix_url, notice_url)
        notice_list.append(data)

    return notice_list
