import logging
from ENV import Env
from BLL import HtmlLoader, HtmlParser

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

query_word = '英国'
ft = '2018-05-01'
et = '2018-05-07'

loader = HtmlLoader.WeChatListLoader()

r = loader.load_one_page_by_condition(query=query_word, tsn=Env.Tsn.CustomTime, ft=ft, et=et, page=11)

parser = HtmlParser.WeChatListParser(r.text, r.url, query_word)
article_list = parser.get_article_list()

for item in article_list:
    loader = HtmlLoader.WeChatArticleLoader()
    r = loader.load_by_url(item)
    parser = HtmlParser.WeChatContentParser(r.text, r.url, query_word)
    article = parser.assemble_model()
    parser.save_model(article)
