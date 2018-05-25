from enum import Enum, unique
import logging
from typing import Dict

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


@unique
class Tsn(Enum):
    All = 0
    OneDay = 1
    OneWeek = 2
    OneMonth = 3
    OneYear = 4
    CustomTime = 5


RequestHeaderDic: Dict[str, str] = {
    'Referer': 'http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E7%BE%8E%E5%9B%BD&ie=utf8&_sug_=n&_sug_type_=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

RequestCookieDic: Dict[str, str] = dict(
    ppinf='5|1526963435|1528173035|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0OkFsZXh8Y3J0OjEwOjE1MjY5NjM0MzV8cmVmbmljazo0OkFsZXh8dXNlcmlkOjQ0Om85dDJsdU5BYVZuS0VkckFidGp2MTlheG9XNTRAd2VpeGluLnNvaHUuY29tfA',
    pprdig='naiDGgEBWwMVxjaoXfAp6-2dFKPm-lCLMf4Ek6GmAmS-izf0arUClGvDWbu50KEdQk4wGxCnxxCuSvXCo5jmmnnlBY5OEFzG3GrB4lDWT4GKeQWZJA5Ro5-ayVqJobY5c5jNkJqFUU2F_CNLGfP2DRecMAAwMSbXVhVOQYLbnSY',
    sgid='12-34818907-AVsDnOshdiaabbbq4mSmQKlY; ppmdig=15269634370000007c2d14be73fbee1523a81932a9080a02')

UrlEncode: str = 'utf8'
RequestEncode: str = 'utf-8'
DomainStr: str = 'http://weixin.sogou.com/'
DomainQueryStr: str = 'http://weixin.sogou.com/weixin?type=2&'

DBMySQLEngine: str = 'mysql+mysqlconnector://dbuser:Mc2460022.@192.168.22.197:3306/mysql'
DBSQLServerEngine: str = 'mssql+pyodbc://sa:900807@192.168.22.190:1433/ContriesWechatDB?driver=ODBC+Driver+17+for+SQL+Server'


@unique
class DBName(Enum):
    MySQL = 0
    MSSQLSERVER = 1


DBNameDic: Dict[int, str] = {0: 'mysql', 1: 'mssql'}

IPListBaseUrl: str = 'http://www.xicidaili.com/nn/'

ChromeDir: str = r'E:\chromedriver\chromedriver.exe'
