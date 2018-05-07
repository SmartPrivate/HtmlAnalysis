import logging
import HtmlParser,HtmlLoader,Env,ContentData

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

querystr=HtmlLoader.set_new_query_by_condition('英国', Env.Tsn.CustomTime, '2017-04-01', '2017-04-05')

r=HtmlLoader.get_we_chat_query_url_list(querystr)

parser=HtmlParser.WeChatListParser(r)
data=parser.get_soup()
print(data)
