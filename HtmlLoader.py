import logging
import requests, Env
from urllib import parse
from enum import Enum

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


def get_we_chat_query_url_list(url: str):
    r = requests.get(url, headers=Env.header)
    r.encoding = 'utf-8'
    return r.text


def set_new_query_by_condition(query: str, tsn: Enum, ft: str, et: str) -> str:
    query_list = []
    head_str = 'http://weixin.sogou.com/weixin?type=2'
    query_list.append(head_str)
    encode_str = 'ie=utf8'
    query_list.append(encode_str)
    query_encoded = 'query='+parse.quote(query)
    query_list.append(query_encoded)
    tsn_code = tsn.value
    tsn_str = 'tsn=' + str(tsn_code)
    query_list.append(tsn_str)
    if tsn_code == Env.Tsn.CustomTime.value:
        ft_str = 'ft=' + ft
        et_str = 'et=' + et
    else:
        ft_str = 'ft='
        et_str = 'et='
    query_list.append(ft_str)
    query_list.append(et_str)
    interation_str = 'interation='
    query_list.append(interation_str)
    wxid_str = 'wxid='
    query_list.append(wxid_str)
    usip_str = 'usip='
    query_list.append(usip_str)
    return '&'.join(query_list)
