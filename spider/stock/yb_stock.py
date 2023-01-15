
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

    table = 'yb_stock'

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
            info_code       TEXT    NOT NULL,
            stock_name      TEXT    ,
            stock_code      TEXT    ,
            title           TEXT    NOT NULL,
            org_name        TEXT    ,
            industry_name   TEXT    ,
            pdf_link        TEXT    NOT NULL,
            date            TEXT
        );'''.format(self.table))
        print("数据表创建成功")

    def add(self, params):
        self.cursor.execute(
            f"INSERT INTO {self.table} (title,stock_code,stock_name,info_code,org_name,pdf_link,industry_name,date) \
                VALUES (?, ?, ?, ? ,?, ?,?,?)", params)
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

    data = datetime.now().strftime("%Y-%m-%d")
    params = (
        ('pageNo', pageNo),
        ('pageSize', '100'),
        ('beginTime', '2021-01-01'),
        # ('endTime', '2023-01-04'),
        ('endTime', data),
        ('cb', 'datatable7280156'),
        ('qType', '0'),
    )

    url = f'https://reportapi.eastmoney.com/report/list'
    print('执行次数', pageNo)
    res = requests.get(url=url, params=params)
    return loads_jsonp(res.text)


def query_pdf_page(infoCode):
    url = f'https://data.eastmoney.com/report/info/{infoCode}.html'
    res = requests.get(url=url)
    html = BeautifulSoup(res.text, 'html.parser')
    return html.select('.rightlab')[0].get('href')


new_data = []

db = Datebase()


def get_data(num):
    data = start_page(num)['data']

    for item in data:
        info_code = item['infoCode']
        title = item["title"]
        orgSName = item['orgSName']
        stockCode = item['stockCode']
        stockName = item['stockName']
        indvInduName = item['indvInduName']

        # 如果已经有
        r = db.select([info_code])

        pdf_link = ''
        if r == None:
            pdf_link = query_pdf_page(info_code)
            print(pdf_link)

        date = item["publishDate"].split(' ')[0]

        row = [date, stockCode, stockName,
               f'<a href="{pdf_link}" target="_blank" title="{title}">{title}</a>']

        try:
            db.add((info_code, title, stockCode, stockName,
                   info_code, orgSName, pdf_link, indvInduName, date))
        except Exception as error:
            print(f'已存在：{info_code}, {error}')

        new_data.append(row)

    if num == 1:
        return new_data
    else:
        return get_data(num+1)


Table(['日期', '股票代码', '股票简称', '行业', '报告名称'],
      get_data(1)).to_html('./个股研报', '个股研报')
