import streamlit as st
import requests

st.set_page_config(page_title="Weather App", page_icon="⛅", layout="centered")

st.title("⛅ Simple Weather App")
st.write("Enter a city name below to check the current weather.")


city = st.text_input("City Name", placeholder="e.g., Cairo, London, Tokyo")

if st.button("Get Weather") and city:
    url = f"https://wttr.in/{city}?format=j1"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            current = data['current_condition'][0]
            
            
            st.subheader(f"Weather in {city.capitalize()}")
            st.metric(label="Temperature", value=f"{current['temp_C']} °C")
            st.write(f"**Condition:** {current['weatherDesc'][0]['value'].capitalize()}")
            st.write(f"**Humidity:** {current['humidity']}%")
            st.write(f"**Wind Speed:** {current['windspeedKmph']} km/h")
        else:
            st.error("Could not find weather data for that city.")
    except Exception as e:
        st.error("An error occurred while connecting to the weather service.")