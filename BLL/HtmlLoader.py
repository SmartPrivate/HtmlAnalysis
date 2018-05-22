import logging

from ENV import Env
from BLL import Antispider, HtmlParser
import requests

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class HtmlLoader(object):

    def __init__(self, url: str):
        self._r = requests.get(url=url, headers=Env.HeaderDic)
        self._r.encoding = Env.RequestEncode


class WeChatListLoader(HtmlLoader):

    def __init__(self, url: str, load_all_pages: bool = False, page: int = 1):
        self.__anti_spider = Antispider.Anti_Pool()
        self.__url = url
        if not load_all_pages:
            self.__url = '{0}&page={1}'.format(url, str(page))
            super().__init__(self.__url)
        else:
            self.__load_all_pages(self.__url)

    @property
    def article_url_list(self):
        if Env.SogouAntiSpider in self._r.url:
            ip_dic = self.__anti_spider.get_singleton_ip_dic()
            self._r = requests.get(self.__url, proxies=ip_dic)
            self._r.encoding = Env.RequestEncode
        return self._r

    def __load_all_pages(self, url: str):
        pass


class WeChatArticleLoader(HtmlLoader):
    pass
