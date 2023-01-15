
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from table import Table
import sqlite3
import json

new_data = []

data = []
with open(f'choice_gzh.json', 'r') as f:
    data = json.loads(f.read())['records']


def get_data():
    # data = []

    for item in data:
        title = item["title"]
        orgSName = item['org']
        industryName = item['rtype']
        date = item["date"]
        pdf_link = item['sourceurl']

        row = (date, orgSName, industryName, title, pdf_link)
        new_data.append(row)

    return new_data


def cell(fields):
    return f'<td>{fields[0]}</td><td>{fields[1]}</td><td>{fields[2]}</td><td><a href="{fields[4]}" target="_blank" title="{fields[3]}">{fields[3]}</a></td>'


dd = get_data()

Table(['日期', '机构名称', '行业名称', '报告名称'],
      dd).to_html('./公众号', '2023-01-12公众号', cell)
