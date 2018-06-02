import logging
import requests.exceptions
from BLL import HtmlParser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from ENV import Env
from DAL import DBOperator
from MODEL import OrmData
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

model=DBOperator.db_select_user_agent()
print(model[1].UserAgent)