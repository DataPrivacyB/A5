import pandas as pd
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def getValuation(n):
    filename = ".\\dataFiles\\dataset.csv"
    import time
    f = open(filename,"w")
    headers = "Companyurls,viewUrl,Market Cap (Rs Cr.),P/E,Book Value (Rs),Dividend (%),Market Lot,Industry P/E,EPS (TTM),P/C,Price/Book,Dividend Yield.(%),Face Value (RS),Deliverables (%)\n"
    f.write(headers)
    siteUrl = "https://www.moneycontrol.com"
    urls2 = pd.read_csv('.\\dataFiles\\urls1.csv')

    for ind in range(0,n):#urls2.index:
        compTechUrl = siteUrl + urls2["Companyurls"][ind]
        data = compTechUrl +"," + urls2["viewUrl"][ind]
        time.sleep(4)
        uClient = uReq(compTechUrl)
        compTechPage = uClient.read()
        uClient.close()
        cTSoup = soup(compTechPage, "html.parser")
        cTTable = cTSoup.find_all("ul", {"class": "clearfix value_list"})
        valueList = (cTTable[0].find_all("li"))
        x = valueList[0].find_all("div", {"class": "value_txtfr"})
        x1 = valueList[5].find_all("div", {"class": "value_txtfr"})
        x2 = valueList[10].find_all("div", {"class": "value_txtfr"})
        x = x + x1 + x2
        for value in x[0:len(x)-1]:
            data += "," + value.text.replace(",","")
        data+="\n"
        print(data)
        f.write(data)
        data = ""

