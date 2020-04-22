import pandas as pd
from nsepy import get_history
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime as dt
import os
from time import sleep
startDate = dt.datetime(2016,1,1)
endDate = dt.datetime(2020,1,1)


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\Akshay Bali\\Desktop\\A5\\userRegistration\\FinanceA5-4cec9ccde82f.json', scope)
client = gspread.authorize(creds)
sheet = client.open('A5_Finance').sheet1


#df = get_history(symbol = Name,start=startDate,end=EndDate)

# niftyData = sheet.get_all_values()
# headers = niftyData.pop(0)
#
# df = pd.DataFrame(niftyData, columns=headers)
# df.to_csv('.\\DataSets\\niftyShareNames.csv', index = False)
df = pd.read_csv('.\\DataSets\\ind_nifty500list.csv')
for ind in range(412,500):
#for ticker in df["Symbol"]:
    ticker = df["Symbol"][ind]
    print("geting Ticker ",ind,ticker)
    if not os.path.exists(".\\DataSets\\Nifty4YearsData\\{}.csv".format(ticker)):
        print("3 sec Sleep")
        sleep(5)
        print("3 sec Sleep Done")
        shareData = get_history(symbol = ticker,start=startDate,end=endDate)
        shareData.to_csv(".\\DataSets\\Nifty4YearsData\\{}.csv".format(ticker))
        print("got Ticker ", ticker)
    else:
        print("already Have ",ticker)

