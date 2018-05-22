import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

r = requests.get('https://www.kuaidaili.com/free/inha/1')
soup = BeautifulSoup(r.text, 'lxml')
ips = soup.tbody.find_all('tr')
ip_list = []
for item in ips:
    ip = item.text.split('\n')
    ip_list.append(ip[1] + ':' + ip[2])

HeaderDic = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

pro = {'http': 'socks5://127.0.0.1:1080'}
print(pro)
req = requests.get('http://www.google.com', proxies=pro)
req.encoding = 'utf-8'
print(req.text)
