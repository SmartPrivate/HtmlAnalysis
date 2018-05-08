import logging
from urllib import parse
from typing import Dict

from ENV import Env
from BLL import Antispider, HtmlParser
import requests
from requests import Response, cookies

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class HtmlLoader(object):
    r: Response

    def __init__(self):
        self._anti_spider = Antispider.SNUID_IP_Pool()

    def load_by_url(self, url: str):
        """
        获取网页request
        :param url: 网址
        :return: request
        """
        self.r = requests.get(url)
        self.r.encoding = Env.RequestEncode

    def load_by_url_with_header(self, url: str, header: Dict[str, str] = None):
        """
        只传递header获取网页request
        :param url: 网址
        :param header: header
        :return: request
        """
        if header is not None:
            self.r = requests.get(url, headers=header)
        else:
            self.r = requests.get(url, headers=Env.HeaderDic)
        self.r.encoding = Env.RequestEncode

    def load_by_url_with_header_and_cookie(self, url: str, cookie: cookies.RequestsCookieJar = None,
                                           header: Dict[str, str] = None):
        """
        同时传递header和cookie获取网页request
        :param url: 网址
        :param cookie: cookie jar
        :param header: header
        :return: request
        """
        if header is not None and cookie is not None:
            self.r = requests.get(url, cookies=cookie, headers=header)
        elif header is not None and cookie is None:
            self.r = requests.get(url, headers=header)
        elif header is None and cookie is not None:
            self.r = requests.get(url, cookies=cookie, headers=Env.HeaderDic)
        else:
            self.r = requests.get(url, headers=Env.HeaderDic)
        self.r.encoding = Env.RequestEncode

    def load_by_url_with_proxy(self, url: str, proxy: Dict[str, str]):
        self.r = requests.get(url, proxies=proxy)
        self.r.encoding = Env.RequestEncode


class WeChatListLoader(HtmlLoader):
    def load_one_page_by_condition(self, query: str, tsn: Env.Tsn = Env.Tsn.All, ft: str = '', et: str = '',
                                   page: int = 1, header: Dict[str, str] = None) -> Response:
        """
        根据搜索条件，获取一页搜索页的request
        :param query: 搜索关键词
        :param tsn: 日期参数
        :param ft: 起始日期
        :param et: 结束日期
        :param page: 搜索页面
        :param header: header
        :return: 一页搜索页的request
        """
        query_list = dict(query=query, tsn=tsn.value, ie=Env.UrlEncode, interation='', wxid='', usip='', ft=ft, et=et,
                          page=page)
        query_encoded = parse.urlencode(query_list)
        url = Env.DomainQueryStr + query_encoded
        self.load_by_url_with_header(url, header=header)
        if Env.SogouAntiSpider in self.r.url:
            anti_spider_cookie = self._anti_spider.get_singleton_snuid()
            if anti_spider_cookie['SNUID'] == 'no_snuid':
                self.load_by_url_with_proxy(self._anti_spider.get_singleton_ip())
            else:
                new_cookie = requests.utils.add_dict_to_cookiejar(r.cookies, anti_spider_cookie)
                self.load_by_url_with_header_and_cookie(url, header=header, cookie=new_cookie)
        if page > 10:
            new_cookie = requests.utils.add_dict_to_cookiejar(r.cookies, Env.CookieInsertDic)
            self.load_by_url_with_header_and_cookie(url, cookie=new_cookie, header=header)
        return self.r

    def load_all_pages_by_condition(self, query: str, tsn: Env.Tsn = Env.Tsn.All, ft: str = '', et: str = '',
                                    header: Dict[str, str] = None) -> [Response]:
        r = self.load_one_page_by_condition(query=query, tsn=tsn, ft=ft, et=et, header=header)
        parser = HtmlParser.WeChatListParser(r)
        count = parser.get_article_count()
        response = []
        page_count = int(count / 10)
        for i in range(1, page_count + 1):
            res = self.load_one_page_by_condition(query=query, tsn=tsn, ft=ft, et=et, header=header, page=i)
            response.append(res)
        return response


class WeChatArticleLoader(HtmlLoader):
    pass
