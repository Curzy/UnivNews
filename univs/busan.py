
from bs4 import BeautifulSoup

from utils.http import fetch
from utils.univ import univ_info2dict


async def get_list(session):
    prefix_url = "http://go.pusan.ac.kr"
    notice_url = "/college_2016/pages/index.asp?p=50&b=B_1_1&bn=&m=list&nPage=1&ct=2&con_cate_02=&f=ALL&s="
    html = await fetch(session, prefix_url + notice_url)
    bs = BeautifulSoup(html, "lxml")
    notice_list = list()
    for notice in bs.find('ul', {'class': 'clearfix mg-b40'}).find_all('li'):
            anchor = notice.find('a')
            data = univ_info2dict("부산대", anchor.text.strip(), prefix_url, notice_url)

            notice_list.append(data)

    return notice_list
