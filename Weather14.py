  # Set your API key as an environment variable

import streamlit as st
import requests

# OpenWeatherMap API key (replace with your own)
API_KEY = "440c61a06e5598eda87987319849dac9"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "City": city,
            "Temperature": f"{data['main']['temp']}°C",
            "Humidity": f"{data['main']['humidity']}%",
            "Weather": data['weather'][0]['description'].capitalize(),
            "Wind Speed": f"{data['wind']['speed']} m/s"
        }
        return weather
    else:
        return None


# Streamlit UI
st.set_page_config(page_title="Weather Checker", page_icon="🌤️", layout="centered")

st.title("🌤️ Weather Checker")
st.subheader("Enter a city name to get the current weather")

city = st.text_input("City Name", placeholder="Enter city...")

if st.button("Check Weather"):
    if city:
        weather_info = get_weather(city)
        if weather_info:
            st.success(f"📍 {weather_info['City']}")
            st.write(f"🌡 Temperature: {weather_info['Temperature']}")
            st.write(f"💧 Humidity: {weather_info['Humidity']}")
            st.write(f"☁️ Condition: {weather_info['Weather']}")
            st.write(f"🌬 Wind Speed: {weather_info['Wind Speed']}")
        else:
            st.error("❌ City not found. Please check the spelling and try again.")
    else:
        st.warning("⚠️ Please enter a city name!")

# Footer
st.write("---")
st.info("📌 Data provided by OpenWeatherMap API.")

