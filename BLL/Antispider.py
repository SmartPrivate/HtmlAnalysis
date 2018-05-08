from selenium import webdriver
import logging, random
from typing import Dict
from ENV import Env

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class Anti_Pool(object):
    __options: webdriver.ChromeOptions
    __driver: webdriver.Chrome
    __snuid_list: [str]
    __ip_list: [str]

    def __init__(self):
        self.__setup_chrome()
        self.__init_snuid_suid_list()
        self.__init_ip_list()

    def __setup_chrome(self):
        self.__options = webdriver.ChromeOptions()
        self.__options.set_headless()
        self.__options.add_argument('--disable-gpu')
        self.__driver = webdriver.Chrome(Env.ChromeDir, options=self.__options)

    def __init_snuid_suid_list(self):
        self.__snuid_list = []
        for i in range(1, 10):
            suid, snuid = self.__get_snuid_suid()
            resource = suid + '\t' + snuid
            self.__snuid_list.append(resource)

    def __init_ip_list(self):
        self.__ip_list = []

    def __get_ip(self):
        pass

    def __get_snuid_suid(self):
        self.__driver.get(Env.DomainQueryStr)
        suid = self.__driver.get_cookie('SUID')['value']
        try:
            snuid = self.__driver.get_cookie('SNUID')['value']
        except TypeError:
            ip = self.get_singleton_ip()
            snuid = self.__get_snuid(ip)
        return suid, snuid

    def __get_snuid(self, ip: Dict[str, str] = None):
        self.__options.add_argument('--proxy-server=http://{0}'.format(ip['http']))
        self.__driver.get(Env.DomainQueryStr)
        return self.__driver.get_cookie('SNUID')['value']

    def get_singleton_snuid(self) -> Dict[str, str]:
        total = len(self.__snuid_list)
        if total == 0:
            self.__init_snuid_suid_list()
        index = random.randint(0, total - 1)
        item: str = self.__snuid_list[index]
        self.__snuid_list.pop(index)
        suid = item.split('\t')[0]
        snuid = item.split('\t')[1]
        return {'SUID': suid, 'SNUID': snuid}

    def get_singleton_ip(self) -> Dict[str, str]:
        pass
