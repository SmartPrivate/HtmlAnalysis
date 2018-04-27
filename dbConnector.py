import logging
import pyodbc
import RquestsTest

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

conn = pyodbc.connect(r"DRIVER={ODBC Driver 13 for SQL Server};SERVER=192.168.22.190,1433;"
                      r"DATABASE=ContriesWechatDB;UID=sa;PWD=900807")
cursor = conn.cursor()
cursor.execute("select TOP 100 URL from ContriesWechatDB.dbo.T_CountriesWechatDataSource")
urls = cursor.fetchall()
for row in urls:
    text = RquestsTest.get_html_text_split_by_tab(row.URL)
    sqlStr = "insert into ContriesWechatDB.dbo.T_CountriesWechatDataSource(URLText) VALUES (" + "'" + text + "'"+")"
    cursor.execute(sqlStr)
conn.commit()
