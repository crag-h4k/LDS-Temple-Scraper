#js to csv
#https://stackoverflow.com/questions/34798397/scraping-asp-and-java-script-generated-table-with-python-2-7-beautiful-soup-and
#import requests
#import pandas as pd

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

url = "https://www.lds.org/temples/list?lang=eng"

def scrape(url):
    driver = webdriver.Chrome("/Users/danemorgan/chromedriver")
    driver.get(url)

    driver.implicitly_wait(5)
    temples = "/n".join([i.text for i in driver.find_elements_by_xpath('//li[@class="filterResult-1Hx44"]')])
    print temples  
    driver.close()
#content = driver.find_elements_by_class_name('filterResult-1Hx44').text_content()
    #print content
#    xelements =  driver.find_elements_by_xpath(x)
#    elements =  driver.find_elements_by_xpath('//*[@class]')
#    print xelements
#     print elements

#    try:
#    for ii in content:
#        content.get_attribute('href')
#   #         print "for loop here"
#    #        print ii.get_attribute('class').text()
#   # except:
#    #    print "fail"
#     #   driver.quit()

scrape(url)
#elem.send_keys()
#for option in select.options[1:]:
#    print option.text
