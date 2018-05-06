import logging

import requests
from bs4 import BeautifulSoup
from ContentData import WeChatArticleData
from datetime import datetime

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class WeChatParser(object):

    def __init__(self, url):
        r = requests.get(url)
        r.encoding = 'utf-8'
        self.__soup = BeautifulSoup(r.text, 'lxml')
        for script in self.__soup(["script", "style"]):
            script.extract()

    def __get_article_title(self) -> str:
        return self.__soup.title.text

    def __get_origin_tag(self) -> bool:
        return self.__soup.find(id='copyright_logo') is not None

    def __get_post_date(self) -> datetime:
        date_str = self.__soup.find(id='post-date').text
        result = datetime.strptime(date_str, '%Y-%m-%d')
        return result

    def __get_post_user_name(self) -> str:
        return self.__soup.find(id='post-user').text

    def __get_post_user_id(self) -> str:
        return self.__soup.find_all('span', 'profile_meta_value')[0].text

    def __get_post_user_introduction(self) -> str:
        return self.__soup.find_all('span', 'profile_meta_value')[1].text

    def __get_article_content(self) -> str:
        result = self.__soup.find_all(id='js_content')
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
