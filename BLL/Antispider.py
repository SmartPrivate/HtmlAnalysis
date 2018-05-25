import logging, random
from typing import Dict
from ENV import Env
import requests.cookies
import requests
from bs4 import BeautifulSoup
import time
from MODEL import OrmData
from DAL import DBOperator

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


class Anti_Pool(object):
    __snuid_list: {str, str}
    __suid_list: {str, str}
    __ip_list: [str]

    def __init__(self):
        self.__init_ip_list()
        self.__init_snuid_suid_list()

    def __init_snuid_suid_list(self):
        self.__suid_list = []
        self.__snuid_list = []
        ids = DBOperator.db_select_snuid()
        for suid_snuid in ids:
            self.__suid_list.append(suid_snuid.SUID)
            self.__snuid_list.append(suid_snuid.SNUID)

    def __init_ip_list(self):
        self.__ip_list = []
        ips = DBOperator.db_select_ip_address()
        for ip in ips:
            if ip.IPType == 'HTTP':
                self.__ip_list.append(ip.IP + ':' + str(ip.PORT))

    def get_singleton_snuid_dic(self) -> Dict[str, str]:
        return dict(SNUID=random.choice(self.__snuid_list))

    def get_singleton_ip_dic(self) -> Dict[str, str]:

        return dict(http=random.choice(self.__ip_list))
