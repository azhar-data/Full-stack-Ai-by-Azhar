from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv 
import pandas as pd

url="https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2"

cService=webdriver.ChromeService(executable_path=r'C:\Users\ALPHA TECH\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')

driver = webdriver.Chrome (service=cService)
driver.get(url)

product_name=[]
product_price=[]
product_reviews=[]

products = driver.find_elements(
    By.XPATH,
    "//div[contains(@class,'ucw-widget-product-card')]"
)

print("Total products:", len(products))

for i, product in enumerate(products):
    print("\n========== PRODUCT", i + 1, "==========")
    print(product.text)

    print("\n----- IMAGES -----")

    images = product.find_elements(By.TAG_NAME, "img")

    for img in images:
        print("ALT:", img.get_attribute("alt"))

    print("\n----- LINKS -----")

    links = product.find_elements(By.TAG_NAME, "a")

    for link in links:
        print("TEXT:", link.text)
        print("HREF:", link.get_attribute("href"))
AmazonSmartHomeProducts=pd.DataFrame({
    'Product_Name':product_name,
    'Product_Price':product_price,
    'Product_Reviews':product_reviews
})
AmazonSmartHomeProducts.to_csv ('Amzon_Mobiles3_selenium.csv',index=False)
print("Data Saved")