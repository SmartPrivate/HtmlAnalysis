import logging, random
from typing import Dict
from ENV import Env
import requests
from bs4 import BeautifulSoup

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class Anti_Pool(object):
    __snuid_list: {str, str}
    __ip_list: {str, str}

    def __init__(self):
        self.__init_snuid_suid_list()
        self.__init_ip_list()

    def __init_snuid_suid_list(self):
        self.__snuid_list = []
        for i in range(0, 10):
            self.__snuid_list.append(self.__get_snuid_suid())

    def __init_ip_list(self):
        self.__ip_list = []
        ip_request=requests.get('http://www.xicidaili.com/nn/1')


    def __get_snuid_suid(self):
        request = requests.get(Env.DomainQueryStr)
        suid = request.cookies['SUID']
        try:
            snuid = request.cookies['SNUID']
        except TypeError:
            snuid = None
            while snuid is None:
                snuid = self.__get_snuid()
        return {'SUID': suid, 'SNUID': snuid}

    def __get_snuid(self):
        ip = self.get_singleton_ip_dic()
        try:
            snuid_request = requests.get(Env.DomainQueryStr, proxies=ip)
            snuid = snuid_request.cookies['SNUID']
        except requests.exceptions.ConnectTimeout:
            snuid = None
        return snuid

    def get_singleton_snuid_dic(self) -> Dict[str, str]:
        total = len(self.__snuid_list)
        if total == 0:
            self.__init_snuid_suid_list()
        index = random.randint(0, total - 1)
        item = self.__snuid_list[index]
        self.__snuid_list.pop(index)
        return item

    def get_singleton_ip_dic(self) -> Dict[str, str]:
        pass
