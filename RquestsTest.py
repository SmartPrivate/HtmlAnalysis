import logging
from ENV import Env
from BLL import HtmlLoader, HtmlParser
from TOOL import QueryAssembler
from DAL import DBOperator

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

query_word = '韩国'
ft: str = '2018-05-25'
et = '2018-05-25'

url = QueryAssembler.we_chat_query_assembler(query=query_word, tsn=Env.Tsn.CustomTime, ft=ft, et=et)
loader = HtmlLoader.WeChatListLoader(url)
r_list = loader.load_all_pages()
for r in r_list:
    if r is None:
        continue
    list_parser = HtmlParser.WeChatListParser(r)
    url_list = list_parser.get_data()
    for url in url_list:
        article_loader = HtmlLoader.WeChatArticleLoader(url)
        article_r = article_loader.load_one_article_page()
        content_parser = HtmlParser.WeChatContentParser(article_r, query_word)
        DBOperator.db_writer(content_parser.get_data())
