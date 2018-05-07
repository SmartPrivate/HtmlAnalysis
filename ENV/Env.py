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


HeaderDic: Dict[str, str] = {
    'Referer': 'http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E7%BE%8E%E5%9B%BD&ie=utf8&_sug_=n&_sug_type_=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

CookieInsertDic: Dict[str, str] = {'sgid': '12-34818907-AVrvvXiaNYKtZk8vHm8NwdB8',
                                   'ppinf': '5|1525671531|1526881131|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0OkFsZXh8Y3J0OjEwOjE1MjU2NzE1MzF8cmVmbmljazo0OkFsZXh8dXNlcmlkOjQ0Om85dDJsdU5BYVZuS0VkckFidGp2MTlheG9XNTRAd2VpeGluLnNvaHUuY29tfA; pprdig=l5RTTxjs0_8csiNn1nk6huaul2qGKmqm8rJfSb4QpIB7Mz9aAEcBgHiebs1C7tCFkcHNYqn5YYzvPRZ6EMgqQkvdHtygoq2OH17jl21iYWWwIUqs1B_wZiZYSXhvQgsw4FgMqcGKy5tMKKW3IxRBdf7Ghw6MUpJKU3h2Gu3fdOA',
                                   'ppmdig': '15256715310000008ef982f3da6a02706f21a16bfec56df6',
                                   'pprdig': 'l5RTTxjs0_8csiNn1nk6huaul2qGKmqm8rJfSb4QpIB7Mz9aAEcBgHiebs1C7tCFkcHNYqn5YYzvPRZ6EMgqQkvdHtygoq2OH17jl21iYWWwIUqs1B_wZiZYSXhvQgsw4FgMqcGKy5tMKKW3IxRBdf7Ghw6MUpJKU3h2Gu3fdOA'
                                   }

UrlEncode: str = 'utf8'
RequestEncode: str = 'utf-8'
DomainStr: str = 'http://weixin.sogou.com/weixin?type=2&'
ChromeDir: str = 'E:\chromedriver\chromedriver.exe'

DBMySQLEngine: str = 'mysql+mysqlconnector://root:password@localhost:3306/test'
DBSQLServerEngine: str = 'mssql+pyodbc://sa:900807@192.168.22.190:1433/ContriesWechatDB?driver=ODBC+Driver+17+for+SQL+Server'


@unique
class DBName(Enum):
    MySQL = 0
    MSSQLSERVER = 1


DBNameDic: Dict[int, str] = {0: 'mysql', 1: 'mssql'}
