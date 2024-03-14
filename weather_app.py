import requests
import json

def fetch_weather_data(city):
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'YOUR_API_KEY'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def display_weather_data(data):
    if data['cod'] == 200:
        print(f"Weather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print(f"Error: {data['message']}")

def main():
    city = input("Enter city name: ")
    weather_data = fetch_weather_data(city)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()
