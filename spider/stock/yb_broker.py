
from table import Table
import sqlite3
import eastmoney


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
            info_code       TEXT    UNIQUE      NOT NULL,
            title           TEXT                NOT NULL,
            org_name        TEXT                    ,
            pdf_link        TEXT                NOT NULL,
            date            TEXT
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

    def select_all(self):
        # where title like '%月报%'
        # where title like '%周报%'
        self.cursor.execute(
            f"SELECT date,org_name,title,pdf_link FROM {self.table} ORDER BY date DESC limit 10000")
        return self.cursor.fetchall()


db = Datebase()


def get_data(num):
    data = eastmoney.macresearch_api(num)['data']
    print(data)
    for item in data:
        info_code = item['encodeUrl']
        title = item["title"]
        orgSName = item['orgSName']
        date = item["publishDate"].split(' ')[0]

        # 如果已经有
        r = db.select([info_code])

        pdf_link = ''
        if r == None:
            pdf_link = eastmoney.macresearch_pdf_page(info_code)
            print(f'新增:{num},{date},{title},{pdf_link}')

            db.add((title, info_code, orgSName, pdf_link, date))
        else:
            print(f'已存在:{num},{date},{info_code},{title}')

    if num == 10:
        return []
    else:
        return get_data(num+1)


def cell(fields):
    return f'<td>{fields[0]}</td><td>{fields[1]}</td><td><a href="{fields[2]}" target="_blank" title="{fields[2]}">{fields[2]}</a></td>'


# 写入数据库中
dd = get_data(1)
# # 从数据库中查询所以的列表
dd = db.select_all()
Table(['日期', '机构名称', '报告名称'], dd).to_html(
    './html/stock_report/broker', '券商晨报', cell)
