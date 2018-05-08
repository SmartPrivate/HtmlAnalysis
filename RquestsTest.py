import logging
from ENV import Env
from BLL import HtmlLoader, HtmlParser,Antispider
from DAL import DBOperator
from selenium import webdriver
from TOOL import QueryAssembler
import requests
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

query_word = '中国'
ft = '2018-05-01'
et = '2018-05-02'

# 初始化list_loader
#loader = HtmlLoader.WeChatListLoader()

# 按条件搜索一页
#r=loader.load_one_page_by_condition(query=query_word,tsn=Env.Tsn.CustomTime, ft=ft, et=et)
#r = loader.load_all_pages_by_condition(query=query_word, tsn=Env.Tsn.CustomTime, ft=ft, et=et)
#print(r)
# 初始化list_parser
#parser = HtmlParser.WeChatListParser(r)

# 获取文章url列表
#article_list = parser.get_data()

# 遍历列表并解析，并将数据存入数据库
# for item in article_list:
#    loader = HtmlLoader.WeChatArticleLoader()
#    r = loader.load_by_url(item)
#    parser = HtmlParser.WeChatContentParser(r, query_word)
#    article = parser.get_data()
#    DBOperator.db_writer(article)

r=QueryAssembler.we_chat_query_assembler(query=query_word,tsn=Env.Tsn.CustomTime,ft=ft,et=et)
print(r)