from ast import Try
from errno import EEXIST
from http.server import executable
from lib2to3.pgen2 import driver
from tkinter.font import names
from turtle import title
from unicodedata import name
from attr import attrs
from numpy import transpose
from selenium import webdriver
from bs4 import BeautifulSoup
import requests as rq
import pandas as pd
from time import sleep
import re
import csv
import pandas as pd 



#-----------blank List --------------
rating=[]
reviews=[]
cust_name=[]
district=[]
titles=[]
link=[]

# ======= Gating info from landing page=========
url=input('Enter URL: ')
driver=webdriver.Chrome(executable_path="C:\selenium driver\chromedriver.exe")
driver.maximize_window()
driver.get(url)
r1=rq.get(url)
soup1=BeautifulSoup(r1.text, 'html.parser')
driver.execute_script('window.scroll(0,2500)')
sleep(2)
for t in soup1.findAll('a', attrs={'href': re.compile("/product-reviews/")}):
    q=t.get('href')
    link.append(q)
print(link)
for i in link:
    if 'LSTVSLFZT4GJSJWZAZA6TI8AD' in i:
        print(i)
        aa=i
f_url=('https://www.flipkart.com'+str(i))

# ========= Itarating through each pages ================
i=1
while i<=5:
    ss=driver.get(str(f_url)+"&page="+str(i))
    qq=driver.current_url
    r2=rq.get(qq)
    soup=BeautifulSoup(r2.text,'html.parser')

    try:
        for re in soup.find_all('div' ,{'class':'_3LWZlK _1BLPMq'}):
            aa=re.get_text()
            rating.append(aa)
    except:
         for re in soup.find_all('div' ,{'class':'_3LWZlK _1BLPMq'}):
            aa=re.get_text()
            rating.append(aa)

    for re in soup.find_all('p' ,{'class':'_2sc7ZR _2V5EHH'}):
        bb=re.get_text()
        cust_name.append(bb)

    for re in soup.find_all('p' ,{'class':'_2mcZGG'}):
        cc=re.get_text()
        district.append(cc) 
 
    for re in soup.find_all('p' ,{'class':'_2-N8zT'}):
        dd=re.get_text()
        titles.append(dd) 

    for co in soup.find_all('div' ,{'class':'t-ZTKy'}):
        ee=co.get_text()
        reviews.append(ee)
   
    sleep(i)
    i+=1   

    df=pd.DataFrame([cust_name,district,rating,titles,reviews]).transpose()
    df.to_csv('E:\Important data\kkkk_review.csv') 















