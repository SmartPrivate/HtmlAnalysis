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
        self.__init_ip_list()
        self.__init_snuid_suid_list()

    def __init_snuid_suid_list(self):
        self.__snuid_list = []
        for i in range(0, 10):
            self.__snuid_list.append(self.__get_snuid_suid())

    def __init_ip_list(self):
        self.__ip_list = []
        for i in range(1, 11):
            self.__get_ip_list(i)

    def __get_ip_list(self, i: int):
        ip_request = requests.get(Env.IPListBaseUrl + str(i), headers=Env.AntiSpiderHeader)
        soup = BeautifulSoup(ip_request.text, 'lxml')
        ips = soup.find_all('tr', 'odd')
        for item in ips:
            small_list = item.text.split('\n')
            if small_list[8] == 'HTTPS':
                continue
            self.__ip_list.append({'HTTP': small_list[2] + ':' + small_list[3]})

    def __get_snuid_suid(self):
        request = requests.get(Env.DomainStr, headers=Env.HeaderDic)
        suid = request.cookies['SUID']
        try:
            snuid = request.cookies['SNUID']
        except KeyError:
            snuid = None
            while snuid is None:
                snuid = self.__get_snuid(suid)
        return {'SUID': suid, 'SNUID': snuid}

    def __get_snuid(self, suid: str):
        ip = self.get_singleton_ip_dic()
        try:
            jar = requests.cookies.RequestsCookieJar()
            jar.set('SUID',suid)
            snuid_request = requests.get(Env.DomainStr, proxies=ip,cookies=jar,headers=Env.HeaderDic)
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
        total = len(self.__ip_list)
        if total == 0:
            self.__init_ip_list()
        index = random.randint(0, total - 1)
        item = self.__ip_list[index]
        self.__ip_list.pop(index)
        return item
