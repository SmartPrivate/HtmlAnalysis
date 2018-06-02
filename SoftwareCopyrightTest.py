import logging, time, random
from ENV import Env
from BLL import HtmlLoader, HtmlParser
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from DAL import DBOperator
from MODEL import OrmData

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

one_day_url = 'http://www.ipyear.cn/copyright/list_20161121.html'
host_url = 'http://www.ipyear.cn'


def load_by_chrome_webdriver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=Env.ChromeDir)
    date_list_url = DBOperator.db_select_date_list_url()
    for i in range(0, 50):
        date_url = date_list_url[i].DateURL
        driver.get(date_url)
        copyright_id = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[3]/ul/li[1]/span')
        element = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[3]/ul/li[1]/a')
        url = element.get_attribute('href')
        company_text = element.text.split(' ')
        company_name = company_text[0]
        copyright_name = company_text[-1]
        print(company_name)
        print(copyright_name)
        break


# load_by_chrome_webdriver()

