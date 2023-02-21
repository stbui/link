
import efinance as ef
from datetime import datetime
from sqlalchemy import create_engine


# 股票龙虎榜
# billboard = ef.stock.get_daily_billboard('2022-01-01', '2022-07-22')
# billboard.to_csv('data/2022/龙虎榜2022.csv')

data = datetime.now().strftime("%Y%m%d")

# # 股票龙虎榜
# billboard = ef.stock.get_daily_billboard()
# billboard.to_csv('data/billboard/{}.csv'.format(data))
# sleep(1)
# # # # 可转债整体行情
# bond_realtime = ef.bond.get_realtime_quotes()
# bond_realtime.to_csv('data/bond/{}.csv'.format(data))
# sleep(1)

# # # # 沪深市场 A 股最新状况
# stock_realtime = ef.stock.get_realtime_quotes('ETF')
# stock_realtime.to_csv('etf/{}.csv'.format(data))

# engine = create_engine('sqlite:///bond.db')
# df = pandas.read_sql("SELECT * from bond", engine)

# bond_realtime = ef.bond.get_realtime_quotes()
# codes = bond_realtime['债券代码'].tolist()
# for code in codes:
#     bond_history = ef.bond.get_quote_history(code)
#     engine = create_engine('sqlite:///bond.db')
#     bond_history.to_sql(code, engine, None, 'replace')
#     print(code)
# # print(codes)

# 沪深市场 A 股最新状况
# stock_realtime = ef.stock.get_realtime_quotes('ETF')
# codes = stock_realtime['股票代码'].tolist()
# for code in codes:
#     stock_history = ef.stock.get_quote_history(code)
#     engine = create_engine('sqlite:///stock.db')
#     stock_history.to_sql(code, engine, None, 'replace')
#     print(code)

# 龙虎榜详情数据
# billboard = ef.stock.get_daily_billboard()
# billboard.to_csv('billboard/{}.csv'.format(data))
# print('龙虎榜详情数据')

bond_realtime = ef.bond.get_realtime_quotes()
bond_realtime.to_csv('{}.csv'.format(data))
print('沪深市场全部债券实时行情信息')

# stock_etf = ef.stock.get_realtime_quotes('ETF')
# stock_etf.to_csv('etf/{}.csv'.format(data))
# print('ETF')

# # 沪深市场 A 股最新状况
# stock_realtime = ef.stock.get_realtime_quotes()
# stock_realtime.to_csv('stock/{}.csv'.format(data))
# print('沪深')

# stock_realtime = ef.stock.get_realtime_quotes('行业板块')
# stock_realtime.to_csv('bk/{}.csv'.format(data))
# print('行业板块')

# stock_realtime = ef.stock.get_realtime_quotes('概念板块')
# stock_realtime.to_csv('gn/{}.csv'.format(data))
# print('概念板块')

print('收工')
