#===============================================================================
# Robert Mitchell
#
# Scrape Stock prices for a given list of stock symbols.
#===============================================================================
from lxml import html
import requests

#===============================================================================
# Website path to scrape:
sitePath = 'http://www.nasdaq.com/symbol/'
# Specific Query
domQuery = '//div[@id="qwidget_lastsale"]/text()'
#===============================================================================
class industry:
    name = None
    stockSymbolsFilepath = None
    stockSymbols = []

    # Populate list of stock symbols for which scraping will occur.
    def populateStockSymbols(self):
        symbolsFile = open(self.stockSymbolsFilePath, 'r')
        for symbol in symbolsFile:
            self.stockSymbols.append(symbol.strip())
        symbolsFile.close()

    def __init__(self, name, stockSymbolsFilePath):
        self.name = name
        self.stockSymbolsFilePath = stockSymbolsFilePath
        self.populateStockSymbols()

#===============================================================================
# Grab a single stockprice
def getStockPrice(stockSymbol):
    link = sitePath + stockSymbol
    page = requests.get(link)
    tree = html.fromstring(page.content)
    stockPriceRaw = tree.xpath(domQuery)
    if stockPriceRaw:
        return str(stockPriceRaw[0]).replace('$', '')
    else:
        return NULL
#===============================================================================
# Get stock prices for every entity in an industry and save them.
def scrapeStocks(industry):
    for symbol in industry.stockSymbols:
        stockFile = open('./scraped_data/'+industry.name+'/'+symbol+'.dat','a')
        stockPrice = getStockPrice(symbol)
        stockFile.write(symbol+', '+stockPrice)
        stockFile.write('\n')
        #TODO write as .JSON file? What format is best for machine learning in node?
        stockFile.close()
#===============================================================================
                                    # Main
scrapeStocks(industry('solar', './stock_symbols/solar.txt'))
#scrapeStocks(industry('fossil', './stock_symbols/fossil.txt'))
#scrapeStocks(industry('nuclear', './stock_symbols/nuclear.txt'))
#===============================================================================
