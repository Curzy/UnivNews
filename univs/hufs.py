
from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "http://adms.hufs.ac.kr"
    notice_url = "/enter/html/regular/notice.asp"
    html = await fetch(session, prefix_url + notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()
    for notice in bs.find('tbody').find_all('tr'):
        title = notice.find('span', {'class': 'subject'}).text
        data = univ_info2dict("한국어대학교", title, prefix_url, notice_url)
        notice_list.append(data)

    return notice_list
