import logging, time, random
from ENV import Env
from BLL import HtmlLoader, HtmlParser
import requests
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from DAL import DBOperator
from MODEL import OrmData
import re

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

one_day_url = 'http://www.ipyear.cn/copyright/list_20161121.html'
host_url = 'http://www.ipyear.cn'

reader = open('2016.html', 'r')
page = reader.read()
soup = BeautifulSoup(page, 'lxml')

date: str = soup.title.text.split('_')[0]
date = date.replace('\n', '').replace('\t', '')
print(date)
