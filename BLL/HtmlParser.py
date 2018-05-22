import logging

import re
from requests import Response
from bs4 import BeautifulSoup
from MODEL.OrmData import WeChatContent
from datetime import datetime

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class HtmlParser(object):
    def __init__(self, r: Response):
        self._soup = BeautifulSoup(r.text, 'lxml')

    def search_soup(self):
        pass

    def get_data(self):
        pass


class WeChatContentParser(HtmlParser):
    def __init__(self, r: Response, keyword: str):
        super().__init__(r)
        self.keyword = keyword
        self.url = r.url
        self.search_soup()

    def search_soup(self):
        for script in self._soup(["script", "style"]):
            script.extract()

    def __get_article_title(self) -> str:
        return self._soup.title.text

    def __get_origin_tag(self) -> bool:
        return self._soup.find(id='copyright_logo') is not None

    def __get_post_date(self) -> datetime:
        date_str = self._soup.find(id='post-date').text
        result = datetime.strptime(date_str, '%Y-%m-%d')
        return result

    def __get_post_user_name(self) -> str:
        return self._soup.find(id='post-user').text

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
        return self.url

    def __get_keyword(self):
        return self.keyword

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
        return model


class WeChatListParser(HtmlParser):

    def search_soup(self):
        return self._soup.find_all('a', uigs=re.compile('article_title_*'))

    def get_data(self):
        article_list = []
        for item in self.search_soup():
            article_list.append(item['href'])
        return article_list

    @property
    def article_count(self):
        count = self._soup.find('div', 'mun').text[3:-3].replace(',', '')
        return int(count)
