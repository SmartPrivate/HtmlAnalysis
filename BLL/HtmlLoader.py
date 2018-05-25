import logging
from ENV import Env
from BLL import HtmlParser
import requests.exceptions
import time
import random

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class HtmlLoader(object):

    def __init__(self, url: str):
        self._url = url

    def _get_response(self, url, cookies=None, headers=None, proxies=None):
        retry = 0
        while True:
            if retry < Env.RetryCount:
                try:
                    self._r = requests.get(url=url, headers=headers, cookies=cookies, proxies=proxies,
                                           timeout=Env.TimeOut)
                    self._r.encoding = Env.RequestEncode
                except requests.exceptions.ReadTimeout:
                    retry = retry + 1
                    continue
            else:
                print('以重试{0}次，始终TimeOut，请检查网络连接状况！'.format(str(Env.TimeOut)))
                self._r = None


class WeChatListLoader(HtmlLoader):

    def load_one_page(self, page) -> requests.Response:
        one_page_url = '{0}&page={1}'.format(self._url, str(page))
        if page <= 10:
            self._get_response(one_page_url, headers=Env.RequestHeaderDic)
        else:
            self._get_response(one_page_url, headers=Env.RequestHeaderDic, cookies=Env.RequestCookieDic)
        return self._r

    def load_all_pages(self) -> [requests.Response]:
        """
        获取所有查询结果页面
        :return:网页ResponseList
        """
        self.load_one_page(1)
        parser = HtmlParser.WeChatListParser(self._r)
        page_index = int(parser.article_count / 10) + 1
        __response_list = []
        for i in range(1, page_index + 1):
            self.load_one_page(page=i)
            __response_list.append(self._r)
            time.sleep(random.randint(10, 30))
        return __response_list


class WeChatArticleLoader(HtmlLoader):
    def load_one_article_page(self):
        self._get_response(self._url)
        return self._r
