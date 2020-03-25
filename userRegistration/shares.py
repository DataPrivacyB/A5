scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\Akshay Bali\\Desktop\\A5\\userRegistration\\FinanceA5-4cec9ccde82f.json', scope)
client = gspread.authorize(creds)
sheet = client.open('A5_Finance').sheet1

niftyData = sheet.get_all_records()

pp = pprint.PrettyPrinter()
for data in niftyData :
    print(data['TICKER'])
    s = Shares(Name = data['TICKER'])
    S.save()