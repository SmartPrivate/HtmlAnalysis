import requests
from bs4 import BeautifulSoup


def get_html_text_split_by_tab(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    for script in soup(["script", "style"]):
        script.extract()
    all_text = soup.get_text()
    lines = (line.strip() for line in all_text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\t'.join(chunk for chunk in chunks if chunk)
    return text.split('\t')