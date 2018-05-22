import logging
from typing import Dict
from ENV import Env
from BLL import Antispider, HtmlParser
import requests
import time

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class HtmlLoader(object):

    def __init__(self, url: str, headers: Dict[str, str] = None, cookies: Dict[str, str] = None,
                 proxies: Dict[str, str] = None):
        self._anti_spider = Antispider.Anti_Pool()
        self._r = requests.get(url=url, headers=headers, cookies=cookies, proxies=proxies)
        self._r.encoding = Env.RequestEncode

    def get_response(self):
        return self._r


class WeChatListLoader(HtmlLoader):

    def __init__(self, url: str, load_all_pages: bool = False, page: int = 1):
        self.__url = url
        if not load_all_pages:
            self.__url = '{0}&page={1}'.format(url, str(page))
            super().__init__(self.__url, headers=Env.HeaderDic)
            if page > 10:
                super().__init__(self.__url, headers=Env.HeaderDic, cookies=Env.RequestCookieDic)
        else:
            self.__load_all_pages()

    def __load_all_pages(self):
        """
        获取所有查询结果页面
        :return:
        """
        anti_spider = Antispider.Anti_Pool()
        super().__init__(self.__url, headers=Env.HeaderDic)
        parser = HtmlParser.WeChatListParser(self.get_response())
        page_index = int(parser.article_count / 10) + 1
        self.__response_list = []
        for i in range(1, page_index + 1):
            url = '{0}&page={1}'.format(self.__url, str(i))
            try_max = 5
            for try_count in range(try_max):
                try:
                    proxies = anti_spider.get_singleton_ip_dic()
                    r = requests.get(url, headers=Env.HeaderDic, cookies=Env.RequestCookieDic, proxies=proxies)
                    self.__response_list.append(r)
                    time.sleep(3)
                except requests.exceptions.ProxyError:
                    if try_count <= try_max:
                        continue
                    else:
                        print('代理服务器重试5次均失败，尝试增加重试次数')
                        r = None
                        self.__response_list.append(r)

    def get_response_list(self):
        return self.__response_list


class WeChatArticleLoader(HtmlLoader):
    pass
