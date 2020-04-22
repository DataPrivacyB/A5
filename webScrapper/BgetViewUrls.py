import pandas as pd
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def getViewUrls():
    siteUrl = "https://www.moneycontrol.com"
    urls = pd.read_csv('.\\dataFiles\\urls.csv')
    urlsNew = pd.read_csv('.\\dataFiles\\urls.csv')

    filename = ".\\dataFiles\\urls1.csv"
    f = open(filename,"w")
    headers = "Companyurls,viewUrl\n"
    f.write(headers)

    for url in urls['urls'] :
        compAnalysisUrl = siteUrl + url
        uClient = uReq(compAnalysisUrl)
        compAnalysisPage = uClient.read()
        uClient.close()
        cASoup = soup(compAnalysisPage, "html.parser")
        viewMore = (cASoup.find_all("div", {"class": "viewmore"}))
        viewUrl = viewMore[0].a["href"]
        print(viewUrl)
        f.write(url + "," + viewUrl + "\n")
