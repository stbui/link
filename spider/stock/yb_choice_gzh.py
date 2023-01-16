
from table import Table
import json

# file_path = 'T004023001.json'
# output_path = 'html/stock_report/hycl'
# title = '2023-01-16行业策略'

# file_path = 'T004023002.json'
# output_path = 'html/stock_report/hysj'
# title = '2023-01-16行业数据'

# file_path = 'T004023004.json'
# output_path = 'html/stock_report/hyzt'
# title = '2023-01-16行业专题'

file_path = 'T004023003.json'
output_path = 'html/stock_report/hyyj'
title = '2023-01-16行业深度研究'

file_path = 'T004023006.json'
output_path = 'html/stock_report/hydp'
title = '2023-01-16 行业点评'

file_path = 'T004023005.json'
output_path = 'html/stock_report/hyzx'
title = '2023-01-16 行业资讯'

file_path = 'T004023007.json'
output_path = 'html/stock_report/hydy'
title = '2023-01-16 行业调研'

file_path = 'T004023008.json'
output_path = 'html/stock_report/hyrb'
title = '2023-01-16 行业日报'

file_path = 'T004023009.json'
output_path = 'html/stock_report/hyzb'
title = '2023-01-16 行业周报'

file_path = 'T004023010.json'
output_path = 'html/stock_report/hyyb'
title = '2023-01-16 行业月报'

file_path = 'T004023011.json'
output_path = 'html/stock_report/hyjb'
title = '2023-01-16 行业季报'

file_path = 'T004023012.json'
output_path = 'html/stock_report/hy2b'
title = '2023-01-16 行业半年报'

file_path = 'T004023013.json'
output_path = 'html/stock_report/hynb'
title = '2023-01-16 行业年度策略'

# file_path = 'T004005002.json'
# output_path = 'html/stock_report/hyzt'
# title = '2023-01-16 基金投资策略'

file_path = 'T004006001.json'
output_path = 'html/stock_report/kzz'
title = '2023-01-16 可转债研究'

file_path = 'S004011.json'
output_path = 'html/stock_report/tzzh'
title = '2023-01-16 投资组合报告'

file_path = 'T004012003.json'
output_path = 'html/stock_report/lhfx'
title = '2023-01-16 量化分析'

file_path = 'S103003.json'
output_path = 'html/stock_report/rmyb'
title = '2023-01-16 近一月热门研报'

file_path = 'S103001.json'
output_path = 'html/stock_report/rm24'
title = '2023-01-16 24小时热门研报'


new_data = []

data = []
with open(f'spider/stock/choice/{file_path}', 'r') as f:
    data = json.loads(f.read())['records']


def get_data():
    for item in data:
        title = item["title"]
        id = item["id"]
        orgSName = item['org']
        industryName = item['rtype']
        date = item["date"]
        link = f'https://pdf.dfcfw.com/pdf/H301_{id}_1.pdf'
        pdf_link = item['sourceurl'] if item['sourceurl'] else link

        row = (date, orgSName, industryName, title, pdf_link)
        new_data.append(row)

    return new_data


def cell(fields):
    return f'<td>{fields[0]}</td><td>{fields[1]}</td><td>{fields[2]}</td><td><a href="{fields[4]}" target="_blank" title="{fields[3]}">{fields[3]}</a></td>'


dd = get_data()

Table(['日期', '机构名称', '报告类型', '报告名称'],
      dd).to_html(output_path, title, cell)
