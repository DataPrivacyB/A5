from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd

def getBalSheet(n):
    urls3 = pd.read_csv('.\\dataFiles\\urls3.csv')
    print(1)
    year1 = urls3["Companyurls"][0] + "," + urls3["viewUrl"][0]
    year2 = urls3["Companyurls"][0] + "," + urls3["viewUrl"][0]
    year3 = urls3["Companyurls"][0] + "," + urls3["viewUrl"][0]
    year4 = urls3["Companyurls"][0] + "," + urls3["viewUrl"][0]
    year5 = urls3["Companyurls"][0] + "," + urls3["viewUrl"][0]

    filename1 = ".\\dataFiles\\balanceSheet15.csv"
    filename2 = ".\\dataFiles\\balanceSheet16.csv"
    filename3 = ".\\dataFiles\\balanceSheet17.csv"
    filename4 = ".\\dataFiles\\balanceSheet18.csv"
    filename5 = ".\\dataFiles\\balanceSheet19.csv"
    f1 = open(filename1, "w")
    print(2)
    f2 = open(filename2, "w")
    print(3)
    f3 = open(filename3, "w")
    print(4)
    f4 = open(filename4, "w")
    print(5)
    f5 = open(filename5, "w")
    print(6)
    i = 0
    url = "https://www.moneycontrol.com/financials/housingdevelopmentfinancecorporation/balance-sheetVI/HDF#HDF"
    for ind in range(0,n):#urls3.index:
        year1 = urls3["Companyurls"][ind] + "," + urls3["viewUrl"][ind]
        year2 = urls3["Companyurls"][ind] + "," + urls3["viewUrl"][ind]
        year3 = urls3["Companyurls"][ind] + "," + urls3["viewUrl"][ind]
        year4 = urls3["Companyurls"][ind] + "," + urls3["viewUrl"][ind]
        year5 = urls3["Companyurls"][ind] + "," + urls3["viewUrl"][ind]

        url = urls3["BalanceSheetUrl"][ind]
        uClient = uReq(url)
        compSoftPage = uClient.read()
        uClient.close()
        print(url)
        cSoup = soup(compSoftPage, "html.parser")
        cBalLink = cSoup.find_all("table", {"class": "mctable1"})
        cBalRows = cBalLink[0].find_all('tr', class_=lambda x: x != 'darkbg')
        cBalRows.pop(0)
        cBalRows.pop(0)
        if i == 0:
            print("i = 0")
            headers = "Companyurls,viewUrl"
            for row in cBalRows:
                Datas = (row.find_all("td"))
                headers += "," + Datas[0].text.strip().replace(",", "|")
            headers += "\n"
            print(headers)
            f1.write(headers)
            f2.write(headers)
            f3.write(headers)
            f4.write(headers)
            f5.write(headers)
            i = 1

        for row in cBalRows:
            datas = ((row.find_all("td")))
            year1 += "," + datas[1].text.strip().replace(",", "")
            year2 += "," + datas[2].text.strip().replace(",", "")
            year3 += "," + datas[3].text.strip().replace(",", "")
            year4 += "," + datas[4].text.strip().replace(",", "")
            year5 += "," + datas[5].text.strip().replace(",", "")
        year1 += "\n"
        year2 += "\n"
        year3 += "\n"
        year4 += "\n"
        year5 += "\n"
        print(year1)
        f1.write(year1)
        f2.write(year2)
        f3.write(year3)
        f4.write(year4)
        f5.write(year5)

