# UnivNews
대학들의 공지사항을 긁어다가 새로운 글이 생기면 메일로 노티해주는 알리미 

Usage
-----
settings.py 파일 생성
```
GMAIL_ID = 'your gmail id'
GMAIL_PW = 'your gmail pw'
```
최초 실행시 DB init
```
>>> python crawl.py init
```
이후 크롤링시
```
>>> python crawl.py crawl
```

