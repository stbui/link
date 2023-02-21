

from table import Table
import MongoDBService
import eastmoney
import json

output_path = 'html/stock_report/choice'
title = '全部研报'


test_db = MongoDBService.MongoDBService('127.0.0.1', 27017)
test_db.connect_db()


def main(num):
    data = eastmoney.choice_yb_api(num)['records']
    # test_db.on_insert_many(data)
    for row in data:
        result = test_db.on_query_one({'id': row['id']})
        if result == None:
            test_db.on_insert(row)
            print(f"新增:{num},{row['id']},{row['sortTime']},{row['title']}")
        else:
            print(f"已存在:{num},{row['id']}")

    if num == 50:
        return

    return main(num+1)


def cell(fields):
    url = fields['sourceurl'] if fields['sourceurl'] else fields["attach"][0]["url"]
    return f'<td>{fields["sortTime"]}</td><td>{fields["org"]}</td><td>{fields["rtype"]}</td><td><a href="{url}" target="_blank" title="{fields["title"]}">{fields["title"]}</a></td>'


def start():
    flt = {'title': {'$regex': "2023年投资策略"}}
    result = test_db.on_select().sort('reportDate', -1).limit(20000)
    Table(['日期', '机构名称', '报告类型', '报告名称'],
          result).to_html(output_path, title, cell)


# main(10)
start()
