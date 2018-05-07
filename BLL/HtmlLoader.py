import logging
from enum import Enum
from urllib import parse

from ENV import Env
import requests
from requests import Response, cookies

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class HtmlLoader(object):
    r: Response

    def load_by_url(self, url: str) -> str:
        self.r = requests.get(url, headers=Env.HeaderDic)
        self.r.encoding = Env.RequestEncode
        return self.r

    def get_cookies(self):
        return self.r.cookies

    def load_by_cookies(self, jar: cookies.RequestsCookieJar, url: str):
        self.r = requests.get(url, cookies=jar, headers=Env.HeaderDic)
        self.r.encoding = Env.RequestEncode
        return self.r.text


class WeChatListLoader(HtmlLoader):
    def load_by_condition(self, query: str, tsn: Enum = Env.Tsn.All, ft: str = '', et: str = '', page: int = 1) -> str:
        query_list = dict(query=query, tsn=tsn.value, ie=Env.UrlEncode, interation='', wxid='', usip='', ft=ft, et=et,
                          page=page)
        query_encoded = parse.urlencode(query_list)
        url = Env.DomainStr + query_encoded
        return self.load_by_url(url)


class WeChatArticleLoader(HtmlLoader):
    pass
