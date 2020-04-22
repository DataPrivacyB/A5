from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def getCompanyUrls():
    mainUrls = \
        ["https://www.moneycontrol.com/stocks/sectors/banks-private-sector.html",
        "https://www.moneycontrol.com/stocks/sectors/banks-public-sector.html",
        "https://www.moneycontrol.com/stocks/sectors/finance-housing.html",
    "https://www.moneycontrol.com/stocks/sectors/telecommunications-service.html",
        "https://www.moneycontrol.com/stocks/sectors/computers-software.html"]

    filename = ".\\dataFiles\\urls.csv"
    f = open(filename, "w")
    headers = "urls\n"
    f.write(headers)

    for compSoftwareUrl in mainUrls:
        print(compSoftwareUrl)
        uClient = uReq(compSoftwareUrl)
        compSoftPage = uClient.read()
        uClient.close()
        cSoup = soup(compSoftPage, "html.parser")
        #print(cSoup.find_all("div",{"class":"top_gain_table"}))
        cTable = cSoup.find_all("div", {"class": "top_gain_table"})
        cRows = cTable[0].table.find_all("tr")
        cRows.pop(0)
        for row in cRows:
            f.write(row.td.a.get("href") + "\n")