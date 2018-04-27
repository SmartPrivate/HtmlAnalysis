import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


def get_html_text_split_by_tab(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    for script in soup(["script", "style"]):
        script.extract()
    soup.title.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\t'.join(chunk for chunk in chunks if chunk)
    texts = text.split('\t')
    result = ''
    for item in texts:
        if len(item) < 20:
            continue
        result += item
    return result
