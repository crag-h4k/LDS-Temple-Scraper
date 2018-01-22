#js to csv
#import requests
#import pandas as pd
import unicodedata
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#url = input("Which webpage do you want to scrape for data?")
#filename = input("What do you want to name your data set?")
url = "https://www.lds.org/temples/list?lang=eng"

def scrape(url):
    driver = webdriver.Chrome("/Users/danemorgan/chromedriver")

    driver.get(url)
    driver.implicitly_wait(5)

    data = "/n".join([i.text for i in driver.find_elements_by_xpath('//li[@class="filterResult-1Hx44"]')])
    data = unicodedata.normalize("NFKD", data).encode("UTF-8")
    print data 
    driver.close()

    file = open("rawText.txt","w")
    file.write(data)
    file.close()

scrape(url)
'''
import csv
txtLoc = '/Users/danemorgan/Documents/DataScience/Scraping-Scripts/rawText.txt'
csvLoc = '/Users/danemorgan/Documents/DataScience/Scraping-Scripts/rawText.csv'

rawTxt = txtFile
rawCsv = csvFile

in_txt = csv.reader(open(rawTxt, "rb"), delimiter = '\n')
out_csv = csv.writer(open(rawCsv, 'wb'))

df = pd.read_csv(csvLoc)
'''

