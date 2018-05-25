import logging
import requests.exceptions
from BLL import HtmlParser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from ENV import Env

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

HeaderDic = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Referer': 'http://weixin.sogou.com/weixin?type=2&ie=utf8&query=%E7%BE%8E%E5%9B%BD%E9%98%9F%E9%95%BF&tsn=5&ft=2018-05-01&et=2018-05-02&interation=&wxid=&usip='
}

url = 'https://mp.weixin.qq.com/s?src=11&timestamp=1527233406&ver=897&signature=oog4efCHKPMaEPmpIVndNVKoaF6PyVFakY4n711GbHCSq2pGDtv-bcUgmXie7GE-flfDctv5Qpy6twSJEialNP*TzDqf8Ktu8YwJAwU*TA9PQeLAhWk3OoyLow4rpb9I&new=1'

r = requests.get(url)
r.encoding = 'utf-8'
parser = HtmlParser.WeChatContentParser(r, '美国队长')
model=parser.get_data()
print(model.PostDate)