import pandas as pd
import unicodedata

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


url = "https://www.lds.org/temples/list?lang=eng"
driver = webdriver.Chrome("/Users/danemorgan/chromedriver")

def scrape(url):
    driver.get(url)
    driver.implicitly_wait(5)
#pulling out the data by html tag, seperate by "/n", returns elements as a very long string
    nameData = "/n".join([i.text for i in driver.find_elements_by_xpath('//*[@class="templeName-2MBmf"]',)])
    locData = "/n".join([i.text for i in driver.find_elements_by_xpath('//span[@class="templeLocation-27z9P"]')])
    dateData = "/n".join([i.text for i in driver.find_elements_by_xpath('//span[@class="dedicated-2xVdg"]')])

#print nameData,locData,dateData
    driver.close()
  
#normalize char type
    nameData = unicodedata.normalize("NFKD", nameData).encode("UTF-8")
    locData = unicodedata.normalize("NFKD", locData).encode("UTF-8")
#split data, one very long string into a list of smaller strings
    name = nameData.split("/n")
    loc = locData.split("/n")
    date = dateData.split("/n")
  
#start making DFs with column names
    DF = pd.DataFrame({"Name":name})
    locDF = pd.DataFrame({"Location":loc})
    dateDF = pd.DataFrame({"Date":date})
  
#clean date dataframe
    dateDF = dateDF.shift(1)
#add dataframes together
    DF["Location"]= locDF
    DF["Date"]= dateDF
#more cleanup
    DF.loc[182,"Location"]="April 22, 2001"
    DF = DF.drop([0,0])
  
  #save DF to CSV
    DF.to_csv("LDS-temples.csv")
    DF.to_json("LDS-temples.json")
    print "DONE!"

scrape(url)
