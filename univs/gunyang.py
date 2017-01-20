
from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "http://ipsi.konyang.ac.kr"
    notice_url = "/cop/bbs/BBSMSTR_000000000615/selectBoardList.do"
    html = await fetch(session, prefix_url + notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()
    for notice in bs.find('tbody').find_all('tr'):
        anchor = notice.find('span', {'class': 'link'}).find('a')
        link = anchor.attrs['href']
        data = univ_info2dict("건양대학교", anchor.text.strip(), prefix_url, link)

        notice_list.append(data)

    return notice_list
