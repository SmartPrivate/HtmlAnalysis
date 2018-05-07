import logging
from datetime import datetime
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class WeChatArticleData(object):
    def __init__(self, title: str,
                 origin_tag: bool,
                 post_date: datetime,
                 post_user_name: str,
                 post_user_id: str,
                 post_user_introduction: str,
                 article: str):
        """

        :string title: 公众号标题
        :bool origin_tag: 原创标记
        :string post_date: 发布日期，如2018-05-05
        :string post_user_name: 公众号名称
        :string post_user_id: 公众号ID
        :string post_user_introduction: 公众号简介
        :string article: 公众号正文
        """
        self.__title = title
        self.__origin_tag = origin_tag
        self.__post_date = post_date
        self.__post_user_name = post_user_name
        self.__post_user_id = post_user_id
        self.__post_user_introduction = post_user_introduction
        self.__article = article

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value
