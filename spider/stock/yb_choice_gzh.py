

from table import Table
import MongoDBService
import eastmoney
import time


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

    if num == 1000:
        return

    return main(num+1)


main(966)

# def cell(fields):
#     return f'<td>{fields[0]}</td><td>{fields[1]}</td><td>{fields[2]}</td><td><a href="{fields[4]}" target="_blank" title="{fields[3]}">{fields[3]}</a></td>'


# dd = test_db.on_select()

# Table(['日期', '机构名称', '报告类型', '报告名称'],
#       dd).to_html(output_path, title, cell)
