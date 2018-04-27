import logging

import requests
from bs4 import BeautifulSoup

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

web_url = 'https://mp.weixin.qq.com/s?src=11&timestamp=1524792154&ver=841&signature=3F4aWex8Rv*iK6E5QktYDiof9GCPg3smsM9WixcA9Noq8WLLtwEiy4-CtZe*ZauH9q6b11FNoLhUyjHtNLBJsLPmhV9HmvAWaOeSCVhtd5cZmWXZHudoRcLvEwuJOM2n&new=1'


def get_html_text_split_by_tab(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    for script in soup(["script", "style"]):
        script.extract()
    alltext = soup.get_text()
    lines = (line.strip() for line in alltext.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\t'.join(chunk for chunk in chunks if chunk)
    return text


result=get_html_text_split_by_tab(web_url).split('\t')
print(result)
