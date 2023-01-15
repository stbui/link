#

import requests
from datetime import datetime
data = datetime.now().strftime("%Y%m%d")


def lhb_stock_trade(code, date=None):
    '''
    查询龙虎榜营业厅交易明细

    code: 股票代码

    date：日期，格式 20221205

    示例：https://api.duishu.com/lhbapp/stock/detail?date=20221205&code=002150&pagecount=20&page=1
    '''
    url = f'https://api.duishu.com/lhbapp/stock/detail?code={code}&pagecount=20&page=1'
    res = requests.get(url=url)
    return res.text


def lhb_list_today():
    url = 'https://api.duishu.com/dxwapp/lhb/index'
    res = requests.get(url=url)
    with open(f'web/public/lhb/{data}.json', 'w+') as f:
        f.write(res.text)
    return res.json()


def lhb_list_history(date):
    '''
    查询历史龙虎榜数据

    date: 20221205

    return: json

    示例：https://api.duishu.com/dxwapp/lhb/index?date=20221205
    '''

    url = 'https://api.duishu.com/dxwapp/lhb/index?date={}'.format(date)
    res = requests.get(url=url)
    return res.text


def to_json(code, path, content):
    with open(f'{path}/{code}.json', 'w+') as f:
        f.write(content)


list = lhb_list_today()

for codes in list['data']['stock_list']['list']:
    code = codes[0]['param']['code']
    print(code)
    stock = lhb_stock_trade(code)
    with open(f'web/public/lhb/{code}.json', 'w+') as f:
        f.write(stock)
