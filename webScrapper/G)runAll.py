from .AgetCompanyUrls import getCompanyUrls
from .BgetViewUrls import getViewUrls
from .CgetBalanceLinks import getBalanceLinks
from .DTechAnalysis import getTechnicalIndicators
from .EgetValuation import getValuation
from .FgetBalanceSheets import getBalSheet
from time import sleep

getCompanyUrls()
print("Company Urls Generated")
sleep(2)
getViewUrls()
print("View Urls Generated")
sleep(2)
getBalanceLinks(50)
print("Balance Links Generated")
sleep(2)
getBalSheet(50)
print("Balance Sheets Generated")
sleep(2)
getValuation(50)
print("Done")