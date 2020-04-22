import numpy as np
import pandas as pd
import pickle
from nsepy import get_history
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\Akshay Bali\\Desktop\\A5\\userRegistration\\FinanceA5-4cec9ccde82f.json', scope)
client = gspread.authorize(creds)
sheet = client.open('A5_Finance').sheet1

#df = get_history(symbol = Name,start=startDate,end=EndDate)

niftyData = sheet.get_all_values()
headers = niftyData.pop(0)
df = pd.DataFrame(niftyData, columns=headers)
df.to_csv(r'', index = False)
print(df.columns)