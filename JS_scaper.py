#js to csv
#https://stackoverflow.com/questions/34798397/scraping-asp-and-java-script-generated-table-with-python-2-7-beautiful-soup-and
#import requests
#import pandas as pd

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.lds.org/temples/list?lang=eng"

def scrape(url):
    driver = webdriver.Chrome("/Users/danemorgan/chromedriver")
    htmlElem = "li"
    x = "//" + htmlElem + "*[@class='filterResult-1Hx44']"
    #print x

    driver.get(url)

    driver.implicitly_wait(5)
    element =  driver.find_element_by_xpath(x)
    print element.text
    
    try:
        for elm in element:
            print "working..."
            print element.txt

        driver.quit()
    except:
        print "fail"
        driver.quit()

scrape(url)
#elem.send_keys()
#for option in select.options[1:]:
#    print option.text
