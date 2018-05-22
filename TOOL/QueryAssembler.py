from urllib import parse
import logging
from ENV import Env

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


def we_chat_query_assembler(query: str, tsn: Env.Tsn = Env.Tsn.All, ft: str = '', et: str = '', interation: str = ''):
    query_list = dict(query=query, tsn=tsn.value, ie=Env.UrlEncode, interation=interation, wxid='', usip='', ft=ft,
                      et=et)
    query_encode = parse.urlencode(query_list)
    return Env.DomainQueryStr + query_encode
