import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
load_dotenv()
import os

#--------------------------------------------------Constants-----------------------------------------------------------#
username="mathew.shane98@gmail.com"
#--------------------------------------------------Getting the Page data-----------------------------------------------#
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

website= requests.get(url= "https://appbrewery.github.io/instant_pot/", headers= header)
data = website.text


soup= BeautifulSoup(data, "html.parser")
price_block = soup.find( class_= "aok-offscreen")
price = price_block.get_text()
price = price.replace("$", "")
price = float(price)

#
# password = os.getenv("password")
# print(username)
# print(password)

#----------------------------------Send email when value is below a number---------------------------------------------#



if price<int(100):
    connection =smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user =username,
                     password = os.getenv("password")

                     )
    connection.sendmail(from_addr=username,
                        to_addrs=username,
                        msg= "Ting is cheap"
                        )

    connection.close()



