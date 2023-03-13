import requests
from datetime import datetime
from table import Table
import sqlite3

# https://api.stock.us/api/v1/research/report-list?category=2&sub_category=0&dates=1m&q=&rating=all&revision=all&org_name=&author=&xcf_years=&search_fields=title&groupby=date&page=1&page_size=100


Headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,lb;q=0.6',
    'Referer': 'https://stock.us/cn/report/strategy',
}


CATEGORY = (
    ('strategy', '2'),
    ('industry', '3'),
    ('macro', '1'),
    ('bond', '9'),
    ('future', '10'),
    ('brief', '4'),
)


def report_api(page='1'):
    # 策略报告
    data = datetime.now().strftime("%Y-%m-%d")
    params = (
        # 2:策略报告
        ('category', '2'),
        ('sub_category', '0'),
        ('dates', '1m'),
        ('q', ''),
        ('rating', 'all'),
        ('revision', 'all'),
        ('org_name', ''),
        ('author', ''),
        ('xcf_years', ''),
        ('search_fields', 'title'),
        ('groupby', 'date'),
        ('page', page),
        ('page_size', '100'),
    )

    url = f'https://api.stock.us/api/v1/research/report-list'
    res = requests.get(url=url, params=params, headers=Headers)
    return res.json()


class Datebase():
    conn = None
    cursor = None

    table = 'yb_stockus_industry'

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


db = Datebase()


def get_data(num):
    data = report_api(num)['data']

    for item in data:
        info_code = item['id']
        title = item["title"]
        orgSName = item['org_name']
        date = item["pub_date"].split('T')[0]
        pdf_link = item["file_url"]

        # 如果已经有
        res = db.select([info_code])

        if res == None:
            print(f'新增:{num},{date},{title},{pdf_link}')
            db.add((info_code, title, pdf_link, date, orgSName,))
        else:
            print(f'已存在:{num},{date},{info_code},{title}')

    if num == 2:
        return []
    else:
        return get_data(num+1)


def cell(fields):
    return f'<td>{fields[0]}</td><td>{fields[1]}</td><td><a href="{fields[3]}" target="_blank" title="{fields[2]}">{fields[2]}</a></td>'


# 写入数据库中
dd = get_data(1)
# # 从数据库中查询所以的列表
dd = db.select_all()


Table(['日期', '机构名称', '报告名称'],
      dd).to_html('./html/stock_report/strategy_stockus', '策略报告', cell)
