import logging

import re
from bs4 import BeautifulSoup
from MODEL.ContentData import WeChatArticleData
from datetime import datetime

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class WeChatParser(object):
    def __init__(self, request_get):
        self.soup = BeautifulSoup(request_get, 'lxml')

    def get_soup(self):
        pass


class WeChatContentParser(WeChatParser):
    def get_soup(self):
        for script in self.soup(["script", "style"]):
            script.extract()

    def __get_article_title(self) -> str:
        return self.soup.title.text

    def __get_origin_tag(self) -> bool:
        return self.soup.find(id='copyright_logo') is not None

    def __get_post_date(self) -> datetime:
        date_str = self.soup.find(id='post-date').text
        result = datetime.strptime(date_str, '%Y-%m-%d')
        return result

    def __get_post_user_name(self) -> str:
        return self.soup.find(id='post-user').text

    def __get_post_user_id(self) -> str:
        return self.soup.find_all('span', 'profile_meta_value')[0].text

    def __get_post_user_introduction(self) -> str:
        return self.soup.find_all('span', 'profile_meta_value')[1].text

    def __get_article_content(self) -> str:
        result = self.soup.find_all(id='js_content')
        return '\t'.join(result)

    def get_parsed_article(self) -> WeChatArticleData:
        return WeChatArticleData(
            self.__get_article_title(),
            self.__get_origin_tag(),
            self.__get_post_date(),
            self.__get_post_user_name(),
            self.__get_post_user_id(),
            self.__get_post_user_introduction(),
            self.__get_article_content()
        )


class WeChatListParser(WeChatParser):

    def get_soup(self):
        return self.soup.find_all('a', uigs=re.compile('article_title_*'))

    def get_article_list(self):
        article_list = []
        for item in self.get_soup():
            article_list.append(item['href'])
        return article_list
