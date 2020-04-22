from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd


def getBalanceLinks(n):
    urls1 = pd.read_csv('.\\dataFiles\\urls1.csv')
    siteUrl = "https://www.moneycontrol.com"

    filename = ".\\dataFiles\\urls3.csv"
    f = open(filename, "a")

    headers = "Companyurls,viewUrl,BalanceSheetUrl\n"
    f.write(headers)

    for ind in range(0,n):#urls1.index:
        data = siteUrl + urls1["Companyurls"][ind] + "," + urls1["viewUrl"][ind]
        url = siteUrl + urls1["Companyurls"][ind]
        uClient = uReq(url)
        compSoftPage = uClient.read()
        uClient.close()
        cSoup = soup(compSoftPage, "html.parser")
        cBalLink = cSoup.find_all("div" ,{"class" : "prof_txt midview"})
        cLinks = cBalLink[0].find_all("a")
        if len(cLinks) >= 1:
            data += "," + cLinks[0]["href"]
            data += "\n"
            print(cLinks[0]["href"])
        else:
            print("in else")
            data += "," + " "
            data += "\n"
        f.write(data)

