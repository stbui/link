
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

    table = 'yb_strategy'

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
            info_code       CHAR(50)    NOT NULL    UNIQUE,
            title           TEXT        NOT NULL,
            org_name        CHAR(50)            ,
            pdf_link        TEXT        NOT NULL,
            date            CHAR(50)
        );'''.format(self.table))
        print("数据表创建成功")

    def add(self, params):
        self.cursor.execute(
            f"INSERT INTO {self.table} (info_code,title,pdf_link,date,org_name) \
                VALUES (?, ?, ?, ?, ? )", params)
        self.conn.commit()

    def select(self, params):
        self.cursor.execute(
            f"SELECT info_code FROM {self.table} WHERE info_code=?", params)
        return self.cursor.fetchone()

    def select_all(self):
        self.cursor.execute(
            f"SELECT date,org_name,title,pdf_link FROM {self.table} ORDER BY date DESC limit 10000")
        return self.cursor.fetchall()


def loads_jsonp(_jsonp):
    try:
        return json.loads(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
    except:
        raise ValueError('Invalid Input')


EastmoneyHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Referer': 'https://data.eastmoney.com/',
}


def start_page(pageNo='1'):
    # 策略报告
    # url = 'https://reportapi.eastmoney.com/report/jg?cb=datatable3569085&pageSize=50&beginTime=2021-01-06&endTime=2023-01-06&pageNo=2&fields=&qType=2&orgCode=&author=&p=2&pageNum=2&pageNumber=2&_=1672973717319'

    data = datetime.now().strftime("%Y-%m-%d")
    params = (
        ('pageNo', pageNo),
        ('pageSize', '50'),
        ('beginTime', '2021-01-01'),
        # ('endTime', '2023-01-04'),
        ('endTime', data),
        ('cb', 'datatable3569085'),
        ('qType', '2'),
    )

    url = f'https://reportapi.eastmoney.com/report/jg'
    res = requests.get(url=url, params=params, headers=EastmoneyHeaders)
    return loads_jsonp(res.text)


def query_pdf_page(encodeUrl):
    url = f'https://data.eastmoney.com/report/zw_strategy.jshtml?encodeUrl={encodeUrl}'
    res = requests.get(url=url, headers=EastmoneyHeaders)
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
        date = item["publishDate"].split(' ')[0]
        pdf_link = ''

        # 如果已经有
        res = db.select([info_code])

        if res == None:
            pdf_link = query_pdf_page(info_code)
            # pdf_link = get_pdf_by_code(info_code)
            print(f'新增:{num},{date},{title},{pdf_link}')

            db.add((info_code, title, pdf_link, date, orgSName,))
        else:
            print(f'已存在:{num},{date},{info_code},{title}')

    if num == 2:
        return new_data
    else:
        return get_data(num+1)


def cell(fields):
    return f'<td>{fields[0]}</td><td>{fields[1]}</td><td><a href="{fields[3]}" target="_blank" title="{fields[2]}">{fields[2]}</a></td>'


# 写入数据库中
dd = get_data(1)
# # 从数据库中查询所以的列表
dd = db.select_all()


Table(['日期', '机构名称', '报告名称'],
      dd).to_html('./html/stock/strategy', '策略报告', cell)
