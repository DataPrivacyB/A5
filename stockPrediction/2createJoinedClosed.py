import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from os import path
# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\Akshay Bali\\Desktop\\A5\\userRegistration\\FinanceA5-4cec9ccde82f.json', scope)
# client = gspread.authorize(creds)
# sheet = client.open('A5_Finance').sheet1
#
# niftyData = sheet.get_all_values()
# headers = niftyData.pop(0)
# df = pd.DataFrame(niftyData, columns=headers)
main_df = pd.DataFrame()
#for count,ticker in enumerate(df["TICKER"]):

df1 = pd.read_csv('.\\DataSets\\ind_nifty500list.csv')
for ticker in df1.iloc[0:400,2]:
    print(ticker)
    if(path.exists(".\\DataSets\\Nifty4YearsData\\{}.csv".format(ticker))):
        df = pd.read_csv(".\\DataSets\\Nifty4YearsData\\{}.csv".format(ticker))
        df.set_index('Date',inplace = True)
        df.rename(columns={'Close' : ticker},inplace = True)
        df.drop(['Symbol','Series','Prev Close',
                   'Open','High','Low','Last',
                   'VWAP','Volume','Turnover','Trades',
                   'Deliverable Volume','%Deliverble'],1,inplace=True)
        df = df.dropna(axis=1, how='all')
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df,how='outer')
        #print(count)
main_df = main_df.dropna(axis=1, how='all')

print(main_df.head())
main_df.to_csv(".\\DataSets\\niftyJoinedCloses.csv")
