import pandas as pd
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def getTechnicalIndicators(n):

    filename = ".\\dataFiles\\V.csv"
    f = open(filename,"w")

    siteUrl = "https://www.moneycontrol.com"
    urls1 = pd.read_csv('.\\dataFiles\\urls1.csv')
    i = 0
    for ind in range(0,n):#urls1.index:
        print(urls1["Companyurls"][ind] , urls1["viewUrl"][ind] )
        companyUrl = siteUrl + urls1["Companyurls"][ind]
        compTechUrl = urls1["viewUrl"][ind]
        uClient = uReq(compTechUrl)
        compTechPage = uClient.read()
        uClient.close()
        cTSoup = soup(compTechPage, "html.parser")
        cTTable = cTSoup.find_all("div", {"class": "mt20"})
        tbodys = (cTTable[3].find_all("tbody"))
        tRows = (tbodys[0].tbody.find_all("tr"))
        if i == 0:
            headers = "Companyurls,viewUrl"
            for row in tRows:
                tDatas = (row.find_all("td"))
                headers += "," + tDatas[0].text.strip().replace(",","|")

            headers += "\n"
            print(headers)
            f.write(headers)
            i = 1
        data = companyUrl + "," + urls1["viewUrl"][ind]
        for row in tRows:
            tDatas = (row.find_all("td"))
            data += "," + (tDatas[1].strong.text.replace(",","|"))

        data+="\n"
        f.write(data)
        print(data)
        data = ""
