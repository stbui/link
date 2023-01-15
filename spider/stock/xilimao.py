"""
https://www.xilimao.com/fupan/
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

# url = 'https://www.xilimao.com/fupan/'
# res = requests.get(url=url)
# print(res.text)


def parse_content():
    url = 'https://www.xilimao.com/fupan/'
    res = requests.get(url=url)
    return BeautifulSoup(res.text, 'html.parser')


soup = parse_content()
table = soup.find('table')
tbody = table.find('tbody')

data = []
for tr in tbody.find_all('tr'):
    row = []
    for td in tr.find_all('td'):
        row.append(td.text)
    data.append(row)

df = pd.DataFrame(data, columns=['股票', '板', '涨停', '原因', '价格', '成交', '流通'])


tr = []
for row in range(6):
    if row < 6-1:
        stock = df[df['板'] == str(6-row)]['股票'].tolist()
        tr.append('''<tr><td>{}</td></tr>'''.format("<br/>".join(stock)))

tpl_css = '''<style>*{margin: 0}</style>'''
html = f'<html><head><title>xilimao</title><style></style></head><body><table border="1">{"".join(tr)}</table></body></html>'.replace(
    '<style></style>', tpl_css)

with open('xilimao.html', 'w+') as f:
    f.write(html)
