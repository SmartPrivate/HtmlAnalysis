import logging
import datetime
from ENV import Env
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from DAL import DBOperator
from MODEL import OrmData

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

proxy=DBOperator.db_select_ip_address()
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--proxy-server={}'.format(proxy))
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=Env.ChromeDir)

one_day_url_list = DBOperator.db_select_date_list_url()[171:300]
for item in one_day_url_list:
    driver.get(item.DateURL)
    date_str = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[1]/ul/li[3]/a').text
    date = datetime.datetime.strptime(date_str, '%Y年%m月%d日')
    for i in range(1, 21):
        copyright_id = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div/div[1]/div[3]/ul/li[{0}]/span'.format(i)).text
        element = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[3]/ul/li[{0}]/a'.format(i))
        url = element.get_attribute('href')
        company_name_and_software_name = element.text.split(' ')
        company_name = company_name_and_software_name[0]
        software_name = company_name_and_software_name[2]
        model = OrmData.SoftwareCopyrightContent()
        model.CompanyName = company_name
        model.CopyrightID = copyright_id
        model.CopyrightName = software_name
        model.URL = url
        # temp_str = company_name + ',' + software_name + ',' + url + ',' + copyright_id + ',' + date_str + '\n'
        model.RegistrationDate = date
        DBOperator.db_writer(model)

