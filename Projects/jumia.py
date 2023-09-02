import requests
import random
import random
import requests
import urllib.request
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
from csv import writer

#url = "https://www.jumia.co.ke/"

#class JumiaScrapper:
    #pageContent =[]
    #productName = []
    #brandName = []
    #price = []
    #reviews = []
    #rating = []
url = "https://www.jumia.co.ke/"

#get page content
def get_pagecontent(url):
    url = "https://www.jumia.co.ke/"    
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

#get product name
def getproductname(soup):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    #product_name = soup.find_all('div', {'class': 'itm'})
    product_name = ()
    for product in soup.find_all('div', {'class': '- df -j-bet'}):
        soup.append(product)
        return product_name
#get brand name   
def getproductbrand(soup):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    product_brand =()
    for product in soup.find_all('div',{'class':'col6-phs-pvxs'}):
        soup.append(product)
        return product_brand
#get price
def getproductprice(soup):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    product_price =()
    for product in soup.find_all('div',{'class':'-b -ltr -tal -fs24'}):
        soup.append(product)
        return product_price
    
#get discount
def getproductdiscount(soup):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    product_discount =()
    for product in soup.find_all('div', {'class':'bdg_dsct_dyn-mls'}):
        soup.append(product)
        return product_discount
    
#get number of reviews
def getproductreviewcnt(soup):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    product_review =()
    for product in soup.find_all('div', {'class':'cola -phm -df -d -co'}):
        soup.append(product)
        return product_review
    
#get ratings
def getproductratings(soup):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    product_rating =()
    for product in soup.find_all('div', {'class':'-ptxs -mts -pbm'}):
        soup.append(product)
        return product_rating
    
soup = get_pagecontent(url)
name = getproductname(soup)
brand = getproductbrand(soup)
price = getproductprice(soup)
discount = getproductdiscount(soup)
review = getproductreviewcnt(soup)
rating = getproductratings(soup)

list_of_lists = [soup, name, brand, price, discount, review, rating]
#save and review the product data
with open('jumia_products.csv', 'w') as jumia_file:
    fieldnames = ["name", "brand", "price", "discount", "reviews", "rating"]
    
    csvwriter = writer(jumia_file)
    csvwriter.writerow(fieldnames)
    
    #loop through product list to update csv file
    def __init__(soup):
        for product in soup.find_all:
            csvwriter.writerow(product)
        
    print("Done! All products have been added to CSV file")
    
jumia = pd.read_csv('jumia_products.csv')
jumia.head(10)




    





    


        
        

           




