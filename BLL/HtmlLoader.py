import logging
from urllib import parse
from typing import Dict

from ENV import Env
from BLL import Antispider
import requests
from requests import Response, cookies

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class HtmlLoader(object):
    r: Response

    def load_by_url(self, url: str) -> Response:
        """
        获取网页request
        :param url: 网址
        :return: request
        """
        self.r = requests.get(url)
        self.r.encoding = Env.RequestEncode
        return self.r

    def load_by_url_with_header(self, url: str, header: Dict[str, str] = None) -> Response:
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
        return self.r

    def load_by_url_with_header_and_cookie(self, url: str, cookie: cookies.RequestsCookieJar = None,
                                           header: Dict[str, str] = None) -> Response:
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
        return self.r


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
        url = Env.DomainStr + query_encoded
        r = self.load_by_url_with_header(url, header=header)
        if 'http://www.sogou.com/antispider/?' in r.url:
            anti_spider_cookie = Antispider.SNUIDPool().get_singleton()
            new_cookie = requests.utils.add_dict_to_cookiejar(r.cookies, anti_spider_cookie)
            r = self.load_by_url_with_header_and_cookie(url, header=header, cookie=new_cookie)
        if page <= 10:
            return r
        else:
            new_cookie = requests.utils.add_dict_to_cookiejar(r.cookies, Env.CookieInsertDic)
            return self.load_by_url_with_header_and_cookie(url, cookie=new_cookie, header=header)


class WeChatArticleLoader(HtmlLoader):
    pass
