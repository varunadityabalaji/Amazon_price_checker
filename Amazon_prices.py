# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 18:21:17 2020

@author: varun
"""

import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Sony-WH-1000XM3-Wireless-Cancellation-Headphones/dp/B07HZ8JWCL/ref=sr_1_1?crid=30OIDFT8C8AAW&keywords=sony+wx1000&qid=1580035054&smid=A14CZOWI0VEHLG&sprefix=sony+wmx%2Caps%2C340&sr=8-1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"    }

def check_price():
    page = requests.get(URL, headers = headers)
    
    soup = BeautifulSoup(page.content,'html.parser')
    
    title = soup.find(id = "productTitle")
    price = soup.find(id = "priceblock_dealprice").get_text()
    converted_price = float(price.replace(",",".")[2:8])
    
    if(converted_price<21):
        send_mail()
        
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('varunbaditya@gmail.com','jkssgftekyxunlsg')
    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Sony-WH-1000XM3-Wireless-Cancellation-Headphones/dp/B07HZ8JWCL/ref=sr_1_1?crid=30OIDFT8C8AAW&keywords=sony+wx1000&qid=1580035054&smid=A14CZOWI0VEHLG&sprefix=sony+wmx%2Caps%2C340&sr=8-1'
    
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('varunbaditya@gmail.com','varunbaditya@gmail.com',msg)
    print("Email Sent")
    server.quit()
    
while(True):
    check_price()
    time.sleep(60*60)
    
    
    
    


    

