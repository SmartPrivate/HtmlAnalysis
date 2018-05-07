import logging
from datetime import datetime

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class WeChatContent(object):

    def __init__(self, title: str, origin_tag: bool, post_date: datetime, post_user_name: str, post_user_id: str, post_user_introduction: str, url: str,
                 article: str):
        self.__title = title
        self.__origin_tag = origin_tag
        self.__post_date = post_date
        self.__post_user_name = post_user_name
        self.__post_user_id = post_user_id
        self.__post_user_introduction = post_user_introduction
        self.__url = url
        self.__article = article

    @property
    def title(self):
        return self.__title

    @property
    def origin_tag(self):
        return self.__origin_tag

    @property
    def post_date(self):
        return self.__post_date

    @property
    def post_user_name(self):
        return self.__post_user_name

    @property
    def post_user_id(self):
        return self.__post_user_id

    @property
    def post_user_introduction(self):
        return self.__post_user_introduction

    @property
    def url(self):
        return self.__url

    @property
    def article(self):
        return self.__article

    @title.setter
    def title(self, value):
        self.__title = value

    @origin_tag.setter
    def origin_tag(self, value):
        self.__origin_tag = value

    @post_date.setter
    def post_date(self, value):
        self.__post_date = value

    @post_user_name.setter
    def post_user_name(self, value):
        self.__post_user_name = value

    @post_user_id.setter
    def post_user_id(self, value):
        self.__post_user_id = value

    @post_user_introduction.setter
    def post_user_introduction(self, value):
        self.__post_user_introduction = value

    @url.setter
    def url(self, value):
        self.__url = value

    @article.setter
    def article(self, value):
        self.__article = value
