from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = "https://kashaf.pk/collections/summer-collection?gad_source=1&gad_campaignid=23969148609&gbraid=0AAAAA9aBXDc08cMrFF8VTxyjMN0m1JSax&gclid=Cj0KCQjwnIDUBhDrARIsAJDGwSuujM2lOuoGkPqB8B980vCfWF2GYBKj3vrvCnOBN4bXb_ygWyNuadIaAhMwEALw_wcB"

cService = webdriver.ChromeService(executable_path=r'C:\\Users\ALPHA TECH\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe') # '/Users/bpfalz/Downloads/chromedriver' for my macbook
driver = webdriver.Chrome(service=cService)

driver.get(url)

qouestList=[]
qoutesDiv = driver.find_elements(By.XPATH, "//li[contains(@class, 'product scroll-trigger animate--slide-in')]")
for p in range(len(qoutesDiv) -1):
    quote = {}
    innerImg = qoutesDiv[p+1].find_element(By.TAG_NAME, "img")
    innera = qoutesDiv[p+1].find_element(By.TAG_NAME, "a")
    quote["img"] =innerImg.get_attribute('src') 
    quote["lines"] =innerImg.get_attribute('alt') 
    quote['url'] = innera.get_attribute('href')
    qouestList.append(quote)

filename = 'Cloth inspirational_quotesMethod1.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['url','img','lines','author'])
    w.writeheader()
    for quote in qouestList:
        w.writerow(quote)

driver.close()