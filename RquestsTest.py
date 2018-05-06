import logging
import requests, re
from bs4 import BeautifulSoup
import pachong

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

web_url = 'http://weixin.sogou.com/weixin?type=2&ie=utf8&query=%E7%BE%8E%E5%9B%BD&tsn=5&ft=2018-04-01&et=2018-04-05&interation=&wxid=&usip='

header = {
    'Referer': 'http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E7%BE%8E%E5%9B%BD&ie=utf8&_sug_=n&_sug_type_=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
r = requests.get(web_url, headers=header)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'lxml')
result = soup.find_all('a', uigs=re.compile('article_title_*'))
for item in result:
    text=pachong.get_html_text_split_by_tab(item['href'])
    print(text.split('\t'))
