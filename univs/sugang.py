from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "http://admission.sogang.ac.kr"
    notice_url = "/admission/html/counsel/notice.asp"
    html = await fetch(session, notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = []
    for notice in bs.find('tbody').find_all('tr'):
        title = notice.find('span').text
        data = univ_info2dict("서강대", title, prefix_url, notice_url)
        notice_list.append(data)
    return notice_list
