from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "https://ipsi.gwnu.ac.kr/user_board/ipsi/"
    notice_url = "boardList.mbs?boardId=249&id=ipsi_060100000000"
    html = await fetch(session, prefix_url + notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()
    for notice in bs.find('tbody').find_all('tr'):
        anchor = notice.find('a')
        link = anchor.attrs['href']
        data = univ_info2dict("강릉원주대", anchor.text.strip(), prefix_url, link)
        notice_list.append(data)

    return notice_list
