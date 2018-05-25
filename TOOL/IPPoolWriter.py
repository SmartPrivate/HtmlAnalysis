import logging
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains

from MODEL import OrmData
from DAL import DBOperator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests.exceptions
from ENV import Env
import time
from BLL import Antispider
from TOOL import QueryAssembler

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


def write_ip_pool():
    for i in range(1, 11):
        html_dir = r'C:\Users\macha\Desktop\IP\{0}.html'.format(str(i))
        html_reader = open(html_dir, 'r', encoding='utf-8')
        html_doc = html_reader.read()

        soup = BeautifulSoup(html_doc, 'lxml')
        ips = soup.find_all('tr', 'odd')
        for ip in ips:
            item = ip.text.split('\n')
            model = OrmData.IpPoolContent()
            model.IP = item[2]
            model.PORT = item[3]
            model.IPArea = item[5]
            model.IPModel = item[7]
            model.IPType = item[8]
            DBOperator.db_writer(model)


def write_snuid_pool():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--proxy')
    bin_path = r'E:\chromedriver\chromedriver.exe'

    web_requester = webdriver.Chrome(chrome_options=chrome_options, executable_path=bin_path)
    query_word = '德国'
    ft = '2018-05-01'
    et = '2018-05-01'

    url = QueryAssembler.we_chat_query_assembler(query=query_word, tsn=Env.Tsn.CustomTime, ft=ft, et=et)
    web_requester.get(url)

    print(web_requester.get_cookies())


