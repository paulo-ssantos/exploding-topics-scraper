import scrapper
from dataManipulate import writeCsv

def __main__():
    scrapperInstancy = scrapper.Scrapper()
    trendsList = scrapperInstancy.get_trending_topics()
    writeCsv(trendsList)
    

if __name__ == "__main__":
    __main__()