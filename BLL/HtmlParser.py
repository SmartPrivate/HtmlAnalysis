import logging

import re
from bs4 import BeautifulSoup
from MODEL.OrmData import WeChatContent
from datetime import datetime
from DAL import DBOperator

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class WeChatParser(object):
    def __init__(self, r_text: str, r_url: str=None, keyword: str='未定义'):
        self.soup = BeautifulSoup(r_text, 'lxml')
        self.url = r_url
        self.keyword = keyword

    def get_soup(self):
        pass

    def assemble_model(self):
        pass

    @staticmethod
    def save_model(model):
        DBOperator.db_writer(model)


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
        result_str_list=[]
        for item in result:
            item.text
            result_str_list.append(item.text)
        return '\t'.join(result_str_list)

    def __get_url(self):
        return self.url

    def __get_keyword(self):
        return self.keyword

    def assemble_model(self):
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


class WeChatListParser(WeChatParser):

    def get_soup(self):
        return self.soup.find_all('a', uigs=re.compile('article_title_*'))

    def get_article_list(self):
        article_list = []
        for item in self.get_soup():
            article_list.append(item['href'])
        return article_list
