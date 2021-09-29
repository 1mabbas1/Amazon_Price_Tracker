#import required modules
import requests as requests
from bs4 import BeautifulSoup as BS
import smtplib
import lxml

"""Enter the email address and password of the account you want to send from, 
the address you want to send an email to,
the url of the product whose price you want to track
"""

from_address = 'email address from'
password = 'password of email address from'
to_address = 'email address to'
url = 'url of the item you want to track'

headers= {'Accept-Language':'en-GB,en-US;q=0.9,en;q=0.8',
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
response = requests.get(url, headers = headers)

soup = BS(response.content,'lxml')
price = soup.find(id="priceblock_ourprice").get_text()
title = soup.find(id='productTitle').get_text().strip()
price_float = float(price.split('£')[1])

mesg = f"{title} is now {price}"

if price_float <= 180:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=from_address, password=password)
        connection.sendmail(from_addr=from_address, to_addrs=to_address,
                            msg = f'Subject: Amazon Price Alert!\n\n{mesg}\n\n{url}'.encode('utf-8'),)







