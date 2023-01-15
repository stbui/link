
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from table import Table
import sqlite3

import re
import json


class Datebase():
    conn = None
    cursor = None

    table = 'yq_macresearch'

    def __init__(self,) -> None:
        self.conncet()
        self.init_table()

    def conncet(self):
        self.conn = sqlite3.connect('yb.db')
        print("数据库打开成功")
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def init_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS {} (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            info_code       CHAR(50)            NOT NULL,
            title           TEXT                NOT NULL,
            org_name        CHAR(50)                    ,
            pdf_link        TEXT                NOT NULL,
            date            CHAR(50)
        );'''.format(self.table))
        print("数据表创建成功")

    def add(self, params):
        self.cursor.execute(
            f"INSERT INTO {self.table} (title,info_code,org_name,pdf_link,date) \
                VALUES (?, ?, ?, ?, ? )", params)
        self.conn.commit()

    def select(self, params):
        self.cursor.execute(
            f"SELECT id FROM {self.table} WHERE info_code=?", params)
        return self.cursor.fetchone()


def loads_jsonp(_jsonp):
    try:
        return json.loads(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
    except:
        raise ValueError('Invalid Input')


def start_page(pageNo='1'):
    # 券商晨报
    # url = 'https://reportapi.eastmoney.com/report/jg?cb=datatable7948150&pageSize=50&beginTime=2021-01-06&endTime=2023-01-06&pageNo=2&fields=&qType=4&orgCode=&author=&p=2&pageNum=2&pageNumber=2&_=1672976057256'

    data = datetime.now().strftime("%Y-%m-%d")
    params = (
        ('pageNo', pageNo),
        ('pageSize', '50'),
        ('beginTime', '2021-01-01'),
        # ('endTime', '2023-01-04'),
        ('endTime', data),
        ('cb', 'datatable7948150'),
        ('qType', '4'),
    )

    url = f'https://reportapi.eastmoney.com/report/jg'
    print('执行次数', pageNo)
    res = requests.get(url=url, params=params)
    return loads_jsonp(res.text)


def query_pdf_page(encodeUrl):
    url = f'https://data.eastmoney.com/report/zw_brokerreport.jshtml?encodeUrl={encodeUrl}'
    res = requests.get(url=url)
    html = BeautifulSoup(res.text, 'html.parser')
    return html.select('.pdf-link')[0].get('href')


new_data = []

db = Datebase()


def get_data(num):
    data = start_page(num)['data']

    for item in data:
        info_code = item['encodeUrl']
        title = item["title"]
        orgSName = item['orgSName']

        # 如果已经有
        r = db.select([info_code])

        pdf_link = ''
        if r == None:
            pdf_link = query_pdf_page(info_code)
            print(pdf_link)

        date = item["publishDate"].split(' ')[0]

        row = [date, orgSName,
               f'<a href="{pdf_link}" target="_blank" title="{title}">{title}</a>']

        try:
            db.add((title, info_code, orgSName, pdf_link, date))
        except Exception as error:
            print(f'已存在：{info_code}, {error}')

        new_data.append(row)

    if num == 10:
        return new_data
    else:
        return get_data(num+1)


Table(['日期', '机构名称', '报告名称'], get_data(1)).to_html('./html/stock/macresearch', '券商晨报')
