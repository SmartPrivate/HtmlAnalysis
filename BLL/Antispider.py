from selenium import webdriver
import logging, random
from typing import Dict
from ENV import Env

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class SNUIDPool(object):
    __options: webdriver.ChromeOptions
    __driver: webdriver.Chrome
    __resource_list: [str]

    def __init__(self):
        self.__setup_chrome()
        self.__init_snuid_suid_list()

    def __setup_chrome(self):
        self.__options = webdriver.ChromeOptions()
        self.__options.set_headless()
        self.__options.add_argument('--disable-gpu')
        self.__driver = webdriver.Chrome(Env.ChromeDir, options=self.__options)

    def __init_snuid_suid_list(self):
        self.__resource_list.clear()
        for i in range(1, 10):
            suid, snuid = self.__get_snuid_suid()
            resource = suid + '\t' + snuid
            self.__resource_list.append(resource)

    def __get_snuid_suid(self):
        self.__driver.get(Env.DomainStr)
        return self.__driver.get_cookie('SUID')['value'], self.__driver.get_cookie('SNUID')['value']

    def get_singleton(self) -> Dict[str, str]:
        total = self.__resource_list.len()
        if total == 0:
            self.__init_snuid_suid_list()
            print('已重新生成资源池:)')
        index = random.randint(0, total - 1)
        item: str = self.__resource_list[index]
        self.__resource_list.pop(index)
        suid = item.split('\t')[0]
        snuid = item.split('\t')[1]
        return {'SUID': suid, 'SNUID': snuid}
