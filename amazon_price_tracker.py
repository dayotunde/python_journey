import requests
from smtplib import *
from bs4 import BeautifulSoup
from pprint import pprint
import lxml
import smtplib
host = "smtp.gmail.com"
# urls = "https://www.amazon.co.uk/Sony-WH-1000XM5-Cancelling-Wireless-Headphones-Black/dp/B09Y2MYL5C/ref=sr_1_1_mod_primary_new?keywords=sony%2Bwh1000xm5&qid=1655570460&s=receiver-speakers&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=1-1&th=1"
urls = "https://www.amazon.co.uk/Portable-Transistor-Excellent-Reception-Emergencies-Black/dp/B08FJ46B15/ref=sr_1_1?_encoding=UTF8&brr=1&content-id=amzn1.sym.d191d14d-5ea3-4792-ae6c-e1de8a1c8780&pd_rd_r=673e5c64-cb69-4eeb-bda3-882283ee4ea8&pd_rd_w=DHX8Z&pd_rd_wg=hfNt0&pf_rd_p=d191d14d-5ea3-4792-ae6c-e1de8a1c8780&pf_rd_r=7BM8ESG58GH8PBDZRBS8&qid=1655572970&rd=1&s=network-media&sr=1-1"
webbing = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
lang = "en-GB,en-US;q=0.9,en;q=0.8"

pot = requests.get(url=urls, headers={"User-Agent": webbing, "Accept-Language": lang})
soup = BeautifulSoup(pot.text,"lxml")
ipad = soup.find_all(class_="a-price-whole")
tablet = soup.find_all(class_="a-price-fraction")
whole = int(ipad[0].text.strip("."))
fraction = int(tablet[0].text)
price = float(f"{whole}.{fraction}")
print(price)

def checking_price():
    hosts = "smtp.gmail.com"
    server = SMTP(host=hosts)
    server.starttls()
    print(server)
    server.login(user='randoyellow@gmail.com', password='redacted')
    server.sendmail(from_addr="randoyellow@gmail.com", to_addrs="redated.com",
                    msg=f"Subject:Price Alert \n\nThe price is below desired ")

if price < 400:
    checking_price()

# salary = pot.text

# print(soup.text)
