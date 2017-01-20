from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "http://ipsi.wku.ac.kr"
    notice_url = "/blog/category/admission-desk/notice/"
    html = await fetch(session, prefix_url + notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()
    for notice in bs.find('div', {"class": "wa-board-a"}).find_all("div", {"class": "tr"}):
        anchor = notice.find('a')
        link = anchor.attrs['href']
        data = univ_info2dict("원광대", anchor.text.strip(), prefix_url, link)

        notice_list.append(data)
    return notice_list
