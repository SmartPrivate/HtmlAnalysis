import logging
import time
from ENV import Env
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from DAL import DBOperator
from MODEL import OrmData

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=Env.ChromeDir)

for page in range(1, 11):
    driver.get('http://www.xicidaili.com/nn/{0}'.format(page))
    for i in range(2, 102):
        ip = driver.find_element_by_xpath('//*[@id="ip_list"]/tbody/tr[{0}]/td[2]'.format(i)).text
        port = driver.find_element_by_xpath('//*[@id="ip_list"]/tbody/tr[{0}]/td[3]'.format(i)).text
        model = OrmData.IpPoolContent()
        model.IP = ip
        model.PORT = port
        DBOperator.db_writer(model)
    time.sleep(5)
