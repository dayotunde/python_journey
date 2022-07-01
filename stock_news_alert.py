import requests
import os
import pprint
import os
from twilio.rest import Client
import time


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# print(message.sid)
mangos = open("masterlist.txt","r")
for pineapple in mangos.readlines():
    print(pineapple)
    STOCK = pineapple.strip()
    COMPANY_NAME = STOCK
    # API_KEY = "H69NKHZJ82Z437WE"
    # news_api_key = "2e804ec6a5044fc2adede74f2abe018e"
    API_KEY = os.environ.get("API_KEY")
    news_api_key = os.environ.get("news_api_key")

    STOCK_ENDPOINT = "https://www.alphavantage.co/query"
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    parameters_stock = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": API_KEY
    }

    news_api = "https://newsapi.org/v2/everything"
    news_parameters = {
        "q":STOCK,
        "language":"en",
        "apiKey": news_api_key
    }

    ## STEP 1: Use https://newsapi.org/docs/endpoints/everything
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    #HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
    #HINT 2: Work out the value of 5% of yerstday's closing stock price.

    stock_data = requests.get(url=STOCK_ENDPOINT,params=parameters_stock)
    status = stock_data.raise_for_status()
    # print(status)
    # print(stock_data.json())
    # print(stock_data.json()["Time Series (Daily)"])
    closes = stock_data.json()["Time Series (Daily)"][list((stock_data.json()["Time Series (Daily)"].keys()))[1]]["4. close"]
    opens = stock_data.json()["Time Series (Daily)"][list((stock_data.json()["Time Series (Daily)"].keys()))[0]]["1. open"]
    # print(closes, opens)
    diff = float(opens)/float(closes) - 1
    print(f"{round(diff*100,2)}%")
    diff_100 = diff *100

    if abs(diff_100) > 5:
        file1 = open(f"{STOCK}", "a")
        news_data = requests.get(url=news_api,params=news_parameters)
        news = (news_data.json()["articles"])
        # print(news)
        news_items = {}


        for element in range(3):
            # print(element)
            news_headline = news[element]["title"]
            news_body = news[element]["content"]
            # print(news_body)
            # print(news_headline)
            news_items[f"Headline: {news_headline}"] = (f"Brief: {news_body}")

        for finger,thumb in list(news_items.items()):
            file1.writelines(f"\n{STOCK}{diff_100}\n{finger}\n\n{thumb[0:90]}\n")

        file1.close()
        file2 = open(f"{STOCK}.txt", "r")
        # for item in file2.readlines():
        #     print(item)
        a = file2.read()
        print(a)

        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=a,
            from_='+19784806092',
            to='+447500979132'
        )

        file2.close()
    time.sleep(60)




        # pprint.pprint(news_headline)
        # print(news_items)

mangos.close()


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

