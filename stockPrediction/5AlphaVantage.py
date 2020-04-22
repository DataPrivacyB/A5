from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from time import sleep
import pytz
key = '0L76EQQCB0D44VSB'
ts = TimeSeries(key, output_format='pandas')

nameDf = pd.read_csv('.\\DataSets\\ind_nifty500list.csv')
tickers = nameDf["Symbol"]
i = 460
for ticker in tickers[460:500]:
    ticker1 = ticker + ".ns"
    print(ticker1)
    sleep(15)
    data, meta_data = ts.get_intraday(symbol=ticker1,interval='1min',outputsize='full')
    data.to_csv(".\\DataSets\\minuteData\\{}{}.csv".format(i+50,ticker))
    print("got",ticker)
    i += 1

