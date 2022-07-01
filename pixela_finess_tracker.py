import requests
from pprint import pprint
import os
import datetime as dt

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
Bears = os.environ.get("Authorization_bearer")
sheety_auths = {"Authorization": Bears}

user_input = input("So what exercise would you like to track? ")
ID_DELETE =2
url_ep = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheets_ep = "https://api.sheety.co/f7da57ee6b1ea2ddf092b2545f07c3d7/myWorkouts/workouts"
sheets_ep_get = "https://api.sheety.co/f7da57ee6b1ea2ddf092b2545f07c3d7/myWorkouts/workouts"
delete_url = f"https://api.sheety.co/f7da57ee6b1ea2ddf092b2545f07c3d7/myWorkouts/workouts/{ID_DELETE}"

new_header = {
    "x-app-id":APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json"
}



new_params = {
    "query" : user_input,
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 180,
    "age": 32
}

sheeter = requests.get(url=sheets_ep_get,headers=sheety_auths)
# pprint(sheeter.json()["workouts"][0])
exercise_data = requests.post(url=url_ep,json=new_params,headers=new_header)
exercise_data = exercise_data.json()
# pprint(exercise_data)
# print(exercise_data["exercises"][0])
final_data = exercise_data["exercises"][0]
# pprint(final_data)
date_time = (dt.datetime.now().strftime("%d/%m/%Y"))
now_time = dt.datetime.now().strftime("%H:%M:%S")
# print(now_time)

WTF = {
    'workout': {'calories': final_data["nf_calories"],
               'date': date_time,
               'duration': final_data["duration_min"],
               'exercise': (final_data["name"]).title(),
               'time': now_time
                 }
       }


sheetly_up = requests.post(url=sheets_ep,json=WTF,headers=sheety_auths)
print(sheetly_up.status_code)





# delete_row = requests.delete(url=delete_url,headers=sheety_auths)