
from table import Table
import sqlite3
import eastmoney

# https://data.eastmoney.com/report/industry.jshtml


class Datebase():
    table = 'yb_industry'

    def __init__(self,) -> None:
        self.db_client = None
        self.cursor = None
        self.connected = False

        self.conncet()
        self.init_table()

    def conncet(self):
        if not self.db_client:
            self.db_client = sqlite3.connect('yb.db')
            print("数据库打开成功")
            self.cursor = self.db_client.cursor()
            self.connected = True

    def close(self):
        """数据服务关闭"""
        self.connected = False
        if self.db_client:
            self.db_client.close()
        self.db_client = None

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
        """数据库插入数据操作"""
        self.cursor.execute(
            f"INSERT INTO {self.table} (title,info_code,org_name,industry_name,pdf_link,date) \
                VALUES (?, ?, ?, ? ,?, ?)", params)
        self.db_client.commit()

    def on_select(self, params):
        """数据库查询操作"""
        self.cursor.execute(
            f"SELECT info_code FROM {self.table} WHERE info_code=?", params)
        return self.cursor.fetchone()

    def on_select_all(self):
        # where title like '%月报%'
        # where title like '%周报%'
        self.cursor.execute(
            f"SELECT date,org_name,industry_name,title,pdf_link FROM {self.table} ORDER BY date DESC limit 10000")
        return self.cursor.fetchall()


db = Datebase()


def get_data(num):
    data = eastmoney.industry_api(num)['data']

    for item in data:
        info_code = item['infoCode']
        title = item["title"]
        orgSName = item['orgSName']
        industryName = item['industryName']
        date = item["publishDate"].split(' ')[0]
        pdf_link = ''

        # 如果已经有
        res = db.on_select([info_code])

        if res == None:
            # pdf_link = query_pdf_page(info_code)
            pdf_link = eastmoney.industry_pdf_page(info_code)
            print(f'新增:{num},{date},{title},{pdf_link}')

            db.add((title, info_code, orgSName,
                   industryName, pdf_link, date))
        else:
            print(f'已存在:{num},{date},{info_code},{title}')

    if num == 10:
        return []
    else:
        return get_data(num+1)


def cell(fields):
    return f'<td>{fields[0]}</td><td>{fields[1]}</td><td>{fields[2]}</td><td><a href="{fields[4]}" target="_blank" title="{fields[3]}">{fields[3]}</a></td>'


# 写入数据库中
dd = get_data(1)
# # 从数据库中查询所以的列表
dd = db.on_select_all()

Table(['日期', '机构名称', '行业名称', '报告名称'],
      dd).to_html('./html/stock_report/industry', '行业研报', cell)
