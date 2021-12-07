import requests
import os
from datetime import *
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
USER_NAME = os.getenv('USER_NAME')
PROJECT_NAME = os.getenv('PROJECT_NAME')
SHEET_NAME = os.getenv('SHEET_NAME')

end_point = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/b92cd03a1abe1e5baea51d691366a176/workoutTracking/workouts'

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

body = {
    "query": input("What's the exercise you did? "),
    "gender": "female",
    "weight_kg": 45,
    "height_cm": 160,
    "age": 20

}

nutrionix_response = requests.post(url=end_point, json=body, headers=headers)
data = nutrionix_response.json()

exercise_did = data['exercises'][0]['name']

duration = data['exercises'][0]['duration_min']

calories = data['exercises'][0]['nf_calories']

today = datetime.now().date().strftime('%d/%m/%Y')
time = datetime.now().time().strftime('%H:%M:%S')

sheety_body = {
    'workout': {
        "date": f"{today}",
        "time": f"{time}",
        "exercise": f"{exercise_did}".title(),
        "duration": f"{duration}",
        "calories": f"{calories}"
    }
}

sheety_header = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

sheety_response = requests.post(url=sheety_endpoint, json=sheety_body, headers=sheety_header)
print(sheety_response.status_code)
