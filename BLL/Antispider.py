import logging, random
from typing import Dict
from ENV import Env
import requests.cookies
import requests
from bs4 import BeautifulSoup
import time

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class Anti_Pool(object):
    __snuid_list: {str, str}
    __ip_list: {str, str}

    def __init__(self):
        self.__init_ip_list()
        # self.__init_snuid_suid_list()

    def __init_snuid_suid_list(self):
        self.__snuid_list = []
        for i in range(0, 10):
            self.__snuid_list.append(self.__get_snuid_suid())

    def __init_ip_list(self):
        self.__ip_list = []
        for i in range(1, 11):
            self.__get_ip_list(i)

    def __get_ip_list(self, i: int):
        r = requests.get('{0}/{1}/'.format('https://www.kuaidaili.com/free/inha', str(i)))
        soup = BeautifulSoup(r.text, 'lxml')
        ips = soup.tbody.find_all('tr')
        for item in ips:
            ip = item.text.split('\n')
            self.__ip_list.append('http://'+ip[1] + ':' + ip[2])
        time.sleep(3)

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
            jar.set('SUID', suid)
            snuid_request = requests.get(Env.DomainStr, proxies=ip, cookies=jar, headers=Env.HeaderDic)
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
        return {'http': item}
