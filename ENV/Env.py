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

UrlEncode = 'utf8'
RequestEncode='utf-8'
DomainStr = 'http://weixin.sogou.com/weixin?type=2&'
