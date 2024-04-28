import tkinter as tk
from tkinter import messagebox
import requests
import random

def extract_wind_and_wave(weather_data):
    wind_speed = weather_data.get('wind', {}).get('speed')  # Wind speed in meter/sec
    wave_height = weather_data.get('main', {}).get('sea_level')  # Sea level pressure in hPa, approximate proxy for wave height
    return wind_speed, wave_height

def assess_safety(wind_speed, wave_height):
    # Adjust these thresholds as needed based on safety guidelines
   
    if wind_speed <= 8 and wind_speed >=1 and wave_height <= 1101:
        return True, "Success: Safe conditions for fishing."
    else:
        return False, "Alert: Unsafe conditions for fishing. High wind speed or wave height detected."

def get_weather_data(latitude, longitude, api_key):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat': latitude,
        'lon': longitude,
        'appid': api_key,
        'units': 'metric'  # Using metric units for wind speed and wave height
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

if __name__ == "__main__":
    latitude = random.uniform(0,180)
    longitude = random.uniform(-180,180)
    api_key = 'YOUR API KEY'

    weather_data = get_weather_data(latitude, longitude, api_key)
    
    if 'cod' in weather_data and weather_data['cod'] == '404':
        messagebox.showerror("Error", "Location not found.")
    elif 'cod' in weather_data and weather_data['cod'] == '401':
        messagebox.showerror("Error", "Invalid API key.")
    else:
        wind_speed = weather_data.get('wind', {}).get('speed', 'N/A')
        air_pressure = weather_data.get('main', {}).get('pressure', 'N/A')
        humidity = weather_data.get('main', {}).get('humidity', 'N/A')
        temperature = weather_data.get('main', {}).get('temp', 'N/A')
        weather_description = weather_data.get('weather', [{}])[0].get('description', 'N/A')

        print("Wind Speed:", wind_speed, "m/s")
        print("Air Pressure:", air_pressure, "hPa")
        print("Humidity:", humidity, "%")
        print("Temperature:", temperature, "°C")
        print("Weather Description:", weather_description)
        wind_speed, wave_height = extract_wind_and_wave(weather_data)
        is_safe, message = assess_safety(wind_speed, wave_height)
        
        if is_safe:
            messagebox.showinfo("Safe Conditions", message)
        else:
            root = tk.Tk()
            root.withdraw()
            messagebox.showwarning("Unsafe Conditions", message)

        
