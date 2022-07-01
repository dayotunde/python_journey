import requests
from pprint import pprint
import os
import time
from twilio.rest import Client
user = os.environ.get('USER')
print(user)
# TWILIO_ACCOUNT_SID = "redacted"
# TWILIO_AUTH_TOKEN = "redacted"

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# print(TWILIO_ACCOUNT_SID)
# print(TWILIO_AUTH_TOKEN)


urls = "https://api.openweathermap.org/data/2.5/onecall?&&"

parameters = {
    "lat": -36.848461,
    "lon": 174.763336,
    "appid":"548fdc49445dbfddbf1582df223df1d9"
}

data = requests.get(url=urls,params=parameters)
weather_data = []
# print(data.json()["hourly"])
for element in range(13):
    rain_or_no_rain = (data.json()["hourly"][element]["weather"][0]["id"])
    print(rain_or_no_rain)
    weather_data.append(rain_or_no_rain)

for item in weather_data:
    if item < 700:
        message = client.messages \
            .create(
            body="Please Bring 3 Umbrella",
            from_='+19784806092',
            to='+447500979132'
        )
        break





# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ[TWILIO_ACCOUNT_SID]
# auth_token = os.environ[TWILIO_AUTH_TOKEN]

time.sleep(20)
print(message.status)
