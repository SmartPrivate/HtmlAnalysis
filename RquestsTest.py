import logging
from ENV import Env
from BLL import HtmlLoader, HtmlParser
from TOOL import QueryAssembler

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

query_word = '安哥拉'
ft = '2018-05-01'
et = '2018-05-01'

url = QueryAssembler.we_chat_query_assembler(query=query_word, tsn=Env.Tsn.CustomTime, ft=ft, et=et)
loader = HtmlLoader.WeChatListLoader(url, load_all_pages=True)
for item in loader.get_response_list():
    if item is not None:
        parser = HtmlParser.WeChatListParser(item)
        url_list = parser.get_data()
        for url in url_list:
            print(url)
