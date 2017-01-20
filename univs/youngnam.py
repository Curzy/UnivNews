from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "https://enter.yu.ac.kr/board/"
    notice_url = "noticeList.php?bo_table=notice"
    html = await fetch(session, prefix_url + notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()
    for notice in bs.find('div', {'class': 'sub_bbs_table_3'}).find_all('ul'):
        anchor = notice.find_all('a')[0]
        link = anchor.attrs['href']
        data = univ_info2dict("영남", anchor.text.strip(), prefix_url, notice_url)
        notice_list.append(data)

    return notice_list
