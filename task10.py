from tkinter import *
import tkinter as tk
import requests
from tkinter import messagebox
r = tk.Tk()
r.title("Weather Forecast")
r.geometry("500x200")


def get_weather(city):
    api_key = '506c58bb97b97f3e30fb646a2bee3785'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description'].capitalize()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_info = f"Weather: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
        return weather_info
    else:
        return None


def fetch_weather(city):
    weather_info = get_weather(city)
    if weather_info:
        messagebox.showinfo("Weather Forecast", weather_info)
    else:
        messagebox.showerror("Error", "Failed to fetch weather data. Please try again.")


def fetch_weather_entry():
    city = entry.get().strip()
    if city:
        fetch_weather(city)
    else:
        messagebox.showwarning("Warning", "Please enter a city name.")



weather_icon = PhotoImage(file="C:\\Users\\User\\OneDrive\\Desktop\\weather_icon.jpg.png")

resized_icon = weather_icon.subsample(10, 10)
image_label = tk.Label(r, image=resized_icon, text="Weather Forecast")
image_label.pack(pady=10)

label = tk.Label(r, text="Enter City Name:")
label.pack(pady=10)

entry = tk.Entry(r, width=30)
entry.pack(pady=5)

fetch_button = tk.Button(r, text="Fetch Weather", command=fetch_weather_entry)
fetch_button.pack(pady=10)

r.mainloop()


