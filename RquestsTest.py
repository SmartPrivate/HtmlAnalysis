
import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

web_url = 'http://weixin.sogou.com/weixin?type=2&ie=utf8&query=%E7%BE%8E%E5%9B%BD&tsn=5&ft=2018-04-01&et=2018-04-05&interation=&wxid=&usip='

r=requests.get(web_url)
r.encoding='utf-8'
print(r.text)