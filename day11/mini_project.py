#to generate a weather report
import requests
city=input("Enter Your City:")
api_key="19aa6a07145a7688887170138c2efe53"
url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response=requests.get(url)
if response.status_code==200:
    data=response.json()
    temperature=data["main"]["temp"]
    humidity=data["main"]["humidity"]
    weather=data["weather"][0]["description"]

    print(f'Temperature:{temperature} K')
    print(f'Humidity: {humidity}%')
    print(f'Condition:{weather}')

else:
    print("Error",response.status_code)