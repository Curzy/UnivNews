from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "http://admission.yonsei.ac.kr/wonju/admission/html/counsel/"
    notice_url = "notice.asp?s_type=TYPE2"
    html = await fetch(session, prefix_url + notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()
    for notice in bs.find('tbody').find_all('tr'):
        anchor = notice.find('a')
        title = notice.find('span', {'class': 'tit'}).text.strip()
        link = anchor.attrs['href']
        data = univ_info2dict("연세대 원주캠", title, prefix_url, link)
        notice_list.append(data)

    return notice_list
