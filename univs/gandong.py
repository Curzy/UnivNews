from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "http://ipsi.cku.ac.kr/mbs/iphak/jsp/board/"
    notice_url = "list.jsp?boardId=1&mcategoryId=&id=iphak_060100000000"
    html = await fetch(session, prefix_url + notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()
    for notice in bs.find('div', {'class': 'board_wrap'}).find('ul').find_all('li'):
        anchor = notice.find('a')
        link = anchor.attrs['href']
        data = univ_info2dict("가톨릭관동대", anchor.text.strip(), prefix_url, link)
        notice_list.append(data)
    return notice_list
