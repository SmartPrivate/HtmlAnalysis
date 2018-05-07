import logging
from ENV import Env
from BLL import HtmlLoader, HtmlParser

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

loader = HtmlLoader.WeChatListLoader()
page1 = loader.load_by_condition(query='德国', tsn=Env.Tsn.CustomTime, ft='2018-04-01', et='2018-04-02', page=11)

cookie=loader.get_cookies()

print(cookie)
#parser = HtmlParser.WeChatListParser(page1)

#list1 = parser.get_article_list()
#print(list1)