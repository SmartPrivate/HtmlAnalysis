import logging

import re
from requests import Response
from bs4 import BeautifulSoup
from MODEL.OrmData import WeChatContent
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from ENV import Env
from MODEL import OrmData

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class HtmlParser(object):
    def __init__(self, r: Response):
        self._soup = BeautifulSoup(r.text, 'lxml')

    def _search_soup(self):
        pass

    def get_data(self):
        pass


class WeChatContentParser(HtmlParser):
    def __init__(self, r: Response, keyword: str):
        super().__init__(r)
        self.__keyword = keyword
        self.__url = r.url
        self.__init_chrome_driver()
        self._search_soup()

    def __init_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.__driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=Env.ChromeDir)
        self.__driver.get(self.__url)

    def _search_soup(self):
        for script in self._soup(["script", "style"]):
            script.extract()

    def __get_article_title(self) -> str:
        return self.__driver.find_element_by_id('activity-name').text

    def __get_origin_tag(self) -> bool:
        return self._soup.find(id='copyright_logo') is not None

    def __get_post_date(self) -> datetime:

        while True:
            try:
                date_str = self.__get_post_date_by_chrome_driver()
                return datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                continue

    def __get_post_user_name(self) -> str:
        return self._soup.find('strong', 'profile_nickname').text

    def __get_post_user_id(self) -> str:
        return self._soup.find_all('span', 'profile_meta_value')[0].text

    def __get_post_user_introduction(self) -> str:
        return self._soup.find_all('span', 'profile_meta_value')[1].text

    def __get_article_content(self) -> str:
        result = self._soup.find_all(id='js_content')
        result_str_list = []
        for item in result:
            result_str_list.append(item.text)
        return '\t'.join(result_str_list)

    def __get_url(self):
        return self.__url

    def __get_keyword(self):
        return self.__keyword

    def get_data(self):

        model = WeChatContent()
        model.Title = self.__get_article_title()
        model.URL = self.__get_url()
        model.Article = self.__get_article_content()
        model.OriginTag = self.__get_origin_tag()
        model.PostDate = self.__get_post_date()
        model.PostUserID = self.__get_post_user_id()
        model.PostUserName = self.__get_post_user_name()
        model.QueryKeyword = self.__get_keyword()
        self.__driver.close()
        return model

    def __get_post_date_by_chrome_driver(self):
        """
        使用无窗口Chrome浏览器处理publish_time
        微信对publish_time进行了修改，变为动态加载，无法通过requests获取
        :return:
        """
        publish_time_element = self.__driver.find_element_by_id('publish_time')
        ActionChains(self.__driver).click(publish_time_element).perform()
        return publish_time_element.text


class WeChatListParser(HtmlParser):

    def _search_soup(self):
        return self._soup.find_all('a', uigs=re.compile('article_title_*'))

    def get_data(self):
        article_list = []
        for item in self._search_soup():
            article_list.append(item['href'])
        return article_list

    @property
    def article_count(self):
        count = self._soup.find('div', 'mun').text[3:-3].replace(',', '')
        return int(count)


class SoftwareCopyrightListParser(HtmlParser):
    def write_software_copyright_info_to_db(self):
        date: str = self._soup.title.text.split('_')[0].replace('\n', '').replace('\t', '')
        for item in self._soup.find('div', 'news_college_list').find_all('li'):

            copyright_id = item.find('span', 'date').text
            detail_url = item.find('a')
            url = Env.SoftwareCopyrightHostUrl + detail_url['href']
            company_texts = detail_url.text.split(' ')
            company_name = company_texts[0]
            copyright_name = company_texts[-1]
            model = OrmData.SoftwareCopyrightContent()
            model.CompanyName = company_name
            model.CopyrightID = copyright_id
            model.CopyrightName = copyright_name
            model.URL = url
            model.RegistrationDate=datetime.strptime()
