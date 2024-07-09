import akshare as ak

stock_zh_a_hist_df = ak.stock_zh_a_hist(
    symbol="002253",
    period="daily",
    start_date="20230731",
    end_date='20230731',
    adjust=""
)
print(stock_zh_a_hist_df)
# 开盘价、收盘价、最高价、最低价、成交量、成交额、涨跌幅和换手率

print(f"开盘价：{list(stock_zh_a_hist_df['开盘'].values)}")
print(f"收盘价：{list(stock_zh_a_hist_df['收盘'].values)}")
print(f"最高价：{list(stock_zh_a_hist_df['最高'].values)}")
print(f"最低价：{list(stock_zh_a_hist_df['最低'].values)}")
print(f"成交量：{list(stock_zh_a_hist_df['成交量'].values)}")
print(f"成交额：{list(stock_zh_a_hist_df['成交额'].values)}")
print(f"涨跌幅：{list(stock_zh_a_hist_df['涨跌幅'].values)}")
print(f"换手率：{list(stock_zh_a_hist_df['换手率'].values)}")

