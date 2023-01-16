
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from table import Table
import sqlite3
import re
import json


# https://data.eastmoney.com/report/industry.jshtml


class Datebase():
    conn = None
    cursor = None

    table = 'yb_industry'

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
            info_code       TEXT    NOT NULL    UNIQUE,
            title           TEXT    NOT NULL,
            org_name        TEXT    ,
            industry_name   TEXT    ,
            pdf_link        TEXT    NOT NULL,
            date            TEXT
        );'''.format(self.table))
        print("数据表创建成功")

    def add(self, params):
        self.cursor.execute(
            f"INSERT INTO {self.table} (title,info_code,org_name,industry_name,pdf_link,date) \
                VALUES (?, ?, ?, ? ,?, ?)", params)
        self.conn.commit()

    def select(self, params):
        self.cursor.execute(
            f"SELECT info_code FROM {self.table} WHERE info_code=?", params)
        return self.cursor.fetchone()

    def select_all(self):
        # where title like '%月报%'
        # where title like '%周报%'
        self.cursor.execute(
            f"SELECT date,org_name,industry_name,title,pdf_link FROM {self.table} ORDER BY date DESC limit 10000")
        return self.cursor.fetchall()


def loads_jsonp(_jsonp):
    try:
        return json.loads(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
    except:
        raise ValueError('Invalid Input')


EastmoneyHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,lb;q=0.6',
    'Referer': 'https://data.eastmoney.com/',
}


def start_page(pageNo='1'):
    data = datetime.now().strftime("%Y-%m-%d")
    params = (
        ('pageNo', pageNo),
        ('pageSize', '50'),
        ('beginTime', '2021-01-01'),
        # ('endTime', '2023-01-04'),
        ('endTime', data),
        ('cb', 'datatable7532024'),
        ('qType', '1'),
    )

    # https://reportapi.eastmoney.com/report/list?cb=datatable3457433&industryCode=*&pageSize=50&industry=*&rating=*&ratingChange=*&beginTime=2021-01-14&endTime=2023-01-14&pageNo=2&fields=&qType=1&orgCode=&rcode=&p=2&pageNum=2&pageNumber=2&_=1673674403059
    url = f'https://reportapi.eastmoney.com/report/list'
    res = requests.get(url=url, params=params, headers=EastmoneyHeaders)
    return loads_jsonp(res.text)


def query_pdf_page(infoCode):
    url = f'https://data.eastmoney.com/report/zw_industry.jshtml?infocode={infoCode}'
    res = requests.get(url=url, headers=EastmoneyHeaders)
    try:
        html = BeautifulSoup(res.text, 'html.parser')
        return html.select('.pdf-link')[0].get('href')
    except:
        return ''


def get_pdf_by_code(code):
    # https://pdf.dfcfw.com/pdf/H3_AP202301111581866526_1.pdf?1673446413000.pdf
    return f'https://pdf.dfcfw.com/pdf/H3_{code}_1.pdf'


new_data = []

db = Datebase()


def get_data(num):
    data = start_page(num)['data']

    for item in data:
        info_code = item['infoCode']
        title = item["title"]
        orgSName = item['orgSName']
        industryName = item['industryName']
        date = item["publishDate"].split(' ')[0]
        pdf_link = ''

        # 如果已经有
        res = db.select([info_code])

        if res == None:
            # pdf_link = query_pdf_page(info_code)
            pdf_link = get_pdf_by_code(info_code)
            print(f'新增:{num},{date},{title},{pdf_link}')

            db.add((title, info_code, orgSName,
                   industryName, pdf_link, date))
        else:
            print(f'已存在:{num},{date},{info_code},{title}')

    if num == 10:
        return new_data
    else:
        return get_data(num+1)


def cell(fields):
    return f'<td>{fields[0]}</td><td>{fields[1]}</td><td>{fields[2]}</td><td><a href="{fields[4]}" target="_blank" title="{fields[3]}">{fields[3]}</a></td>'


# 写入数据库中
dd = get_data(1)
# # 从数据库中查询所以的列表
dd = db.select_all()

Table(['日期', '机构名称', '行业名称', '报告名称'],
      dd).to_html('./html/stock_report/industry', '行业研报', cell)
