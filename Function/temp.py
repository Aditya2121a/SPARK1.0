import requests
import json
from Head.Mouth import *
from Head.Ear import listen

def get_temperature_openweather(city):
    api_key = ""
    endpoint = "https://api.openweathermap.org/data/2.5/weather"

    response = requests.get(endpoint, params={"q": city, "appid": api_key, "units": "metric"})

    if response.status_code == 200:
        data = json.loads(response.text)

        if 'main' in data:
            temperature_celsius = data["main"]["temp"]
            return temperature_celsius
        else:
            print("Error: 'main' key not found in API response")
    else:
        print(f"Error: Failed to fetch data from API, Status code: {response.status_code}")

    return None

def temp():
      # Spark asks for input
    city = listen()  # Listen to user's voice input for city/state name
    if city:
        temperature_celsius = get_temperature_openweather(city)
        if temperature_celsius is not None:
            speak(f"The current temperature in {city} is {temperature_celsius} degrees Celsius")
        else:
            speak("Sorry, I couldn't fetch the temperature data at the moment.")
    else:
        speak("I didn't catch the city name. Please try again.")



