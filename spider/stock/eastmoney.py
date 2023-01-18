

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json


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


def industry_api(pageNo='1'):
    '''
    行业研报
    @页面：https://data.eastmoney.com/report/industry.jshtml
    @目标：https://reportapi.eastmoney.com/report/list?cb=datatable3457433&industryCode=*&pageSize=50&industry=*&rating=*&ratingChange=*&beginTime=2021-01-14&endTime=2023-01-14&pageNo=2&fields=&qType=1&orgCode=&rcode=&p=2&pageNum=2&pageNumber=2&_=1673674403059
    '''
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

    url = f'https://reportapi.eastmoney.com/report/list'
    res = requests.get(url=url, params=params, headers=EastmoneyHeaders)
    return loads_jsonp(res.text)


def industry_pdf_page(infoCode):
    url = f'https://data.eastmoney.com/report/zw_industry.jshtml?infocode={infoCode}'
    res = requests.get(url=url, headers=EastmoneyHeaders)
    try:
        html = BeautifulSoup(res.text, 'html.parser')
        return html.select('.pdf-link')[0].get('href')
    except:
        return ''


def strategy_api(pageNo='1'):
    # 策略报告
    # url = 'https://reportapi.eastmoney.com/report/jg?cb=datatable3569085&pageSize=50&beginTime=2021-01-06&endTime=2023-01-06&pageNo=2&fields=&qType=2&orgCode=&author=&p=2&pageNum=2&pageNumber=2&_=1672973717319'

    data = datetime.now().strftime("%Y-%m-%d")
    params = (
        ('pageNo', pageNo),
        ('pageSize', '50'),
        ('beginTime', '2021-01-01'),
        # ('endTime', '2023-01-04'),
        ('endTime', data),
        ('cb', 'datatable3569085'),
        ('qType', '2'),
    )

    url = f'https://reportapi.eastmoney.com/report/jg'
    res = requests.get(url=url, params=params, headers=EastmoneyHeaders)
    return loads_jsonp(res.text)


def strategy_pdf_page(encodeUrl):
    url = f'https://data.eastmoney.com/report/zw_strategy.jshtml?encodeUrl={encodeUrl}'
    res = requests.get(url=url, headers=EastmoneyHeaders)
    html = BeautifulSoup(res.text, 'html.parser')
    return html.select('.pdf-link')[0].get('href')


def get_pdf_code(code):
    # https://pdf.dfcfw.com/pdf/H3_AP202301111581866526_1.pdf?1673446413000.pdf
    return f'https://pdf.dfcfw.com/pdf/H3_{code}_1.pdf'


def macresearch_api(pageNo='1'):
    '''
    券商晨报
    目标：https://reportapi.eastmoney.com/report/jg?cb=datatable7948150&pageSize=50&beginTime=2021-01-06&endTime=2023-01-06&pageNo=2&fields=&qType=4&orgCode=&author=&p=2&pageNum=2&pageNumber=2&_=1672976057256
    '''
    data = datetime.now().strftime("%Y-%m-%d")
    params = (
        ('pageNo', pageNo),
        ('pageSize', '50'),
        ('beginTime', '2021-01-01'),
        # ('endTime', '2023-01-04'),
        ('endTime', data),
        ('cb', 'datatable7948150'),
        ('qType', '4'),
    )

    url = f'https://reportapi.eastmoney.com/report/jg'
    print('执行次数', pageNo)
    res = requests.get(url=url, params=params)
    return loads_jsonp(res.text)


def macresearch_pdf_page(encodeUrl):
    url = f'https://data.eastmoney.com/report/zw_brokerreport.jshtml?encodeUrl={encodeUrl}'
    res = requests.get(url=url)
    html = BeautifulSoup(res.text, 'html.parser')
    return html.select('.pdf-link')[0].get('href')


def choice_yb_api(page='1'):
    fields = (
        ('S103001', '24小时热门研报'),
        ('S103002', '近一周热门研报'),
        ('S103003', '近一月热门研报'),
        ('S004024', '公众号文章'),
        ('T004001001', '晨会纪要'),
        ('T004001002', '早间资讯'),
        ('T004002001', '宏观研究'),
        ('T004002002', '投资策略'),
        ('T004021001', '宏观资讯'),
        # 1990-00-00T00:00:00Z TO 9999-99-99T99:99:99Z
        ('S005008', '全部研报'),
        # 2022-01-17T00:00:00Z TO 9999-99-99T99:99:99Z
        ('S005007', '近一年研报'),
    )

    params = (
        ('id', 'S005008'),
        ('request', 'simpleSearch'),
        ('cid', '2278064648495130'),
        ('vipIds', ''),
        ('gridTitle', '全部研报'),
        ('type', '8'),
        ('requestAction', '0'),
        ('date', '1990-00-00T00:00:00Z TO 9999-99-99T99:99:99Z'),
        ('types', 'S005008'),
        ('securitycodes', ''),
        ('columnType', ''),
        ('isShow', 'false'),
        ('isSelectStock', 'false'),
        ('pageIndex', page),
        ('limit', '500'),
        ('sort', 'datetime'),
        ('order', 'desc'),
    )

    headers = {
        'token': '',
        'Origin': 'https://choicewzp1.eastmoney.com',
        'Referer': 'https://choicewzp1.eastmoney.com/',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'
    }

    # http://choicewzp1.eastmoney.com/Report/Search.do?title=&cid=2278064648495130&pageIndex=1&limit=10&sort=datetime&order=desc
    # https://choicewzp1.eastmoney.com/Report/Search.do?&cid=2278064648495130&vipIds=&permssionReport=1
    url = 'https://choicewzp1.eastmoney.com/Report/GetReportByTreeNode.do'
    res = requests.get(url=url, params=params, headers=headers)
    return res.json()
