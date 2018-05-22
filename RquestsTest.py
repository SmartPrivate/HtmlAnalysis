import logging
from ENV import Env
from BLL import HtmlLoader, HtmlParser,Antispider
from DAL import DBOperator
from selenium import webdriver
from TOOL import QueryAssembler
from bs4 import BeautifulSoup
import requests
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

query_word = '中国'
ft = '2018-05-01'
et = '2018-05-02'

# 初始化list_loader
query_str=QueryAssembler.we_chat_query_assembler(query=query_word,tsn=Env.Tsn.CustomTime,ft=ft,et=et,page=11)
loader=HtmlLoader.WeChatListLoader(query_str)
r=loader.article_url_list
print(r.text)

