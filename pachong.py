import logging

import requests
from bs4 import BeautifulSoup

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

web_url = 'http://weixin.sogou.com/weixin?type=2&ie=utf8&query=%E7%BE%8E%E5%9B%BD&tsn=5&ft=2018-04-01&et=2018-04-05&interation=&wxid=&usip='


def get_html_text_split_by_tab(url):
    r = requests.get(url)
    r.encoding='utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    for script in soup(["script", "style"]):
        script.extract()
    alltext = soup.get_text()
    lines = (line.strip() for line in alltext.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\t'.join(chunk for chunk in chunks if chunk)
    return text

