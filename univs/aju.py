
from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "http://www.iajou.ac.kr/guide/"
    notice_url = "notice_list.asp"

    html = await fetch(session, prefix_url + notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()

    for notice in bs.find('table', {"class": "tbl_list2"}).find_all('tr'):
        anchor = notice.find('a')
        link = anchor.attrs['href']
        data = univ_info2dict("아주대", anchor.text.strip(), prefix_url, link)
        notice_list.append(data)

    return notice_list
