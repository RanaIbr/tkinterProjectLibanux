from tkinter import *
import tkinter as tk
import requests
import json
from tkinter import messagebox
r = tk.Tk()
r.title("Weather Forecast")
r.geometry("500x400")

def get_weather(city):
    api_key = '506c58bb97b97f3e30fb646a2bee3785'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def fetch_weather(city):
    data = get_weather(city)
    if data:
        weather_description = data['weather'][0]['description'].capitalize()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_info = f"Weather: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
        return weather_info
    else:
        return None

def fetch_weather_entry():
    city = entry.get().strip()
    if city:
        weather_info = fetch_weather(city)
        if weather_info:
            weather_display.config(state='normal')
            weather_display.delete(1.0, END)
            weather_display.insert(END, weather_info)
            weather_display.config(state='disabled')
        else:
            messagebox.showerror("Error", "Failed to fetch weather data. Please try again.")
    else:
        messagebox.showwarning("Warning", "Please enter a city name.")

def calculate_statistics(city):
    data = get_weather(city)
    if data:
        temperatures = []
        humidities = []

        for _ in range(5):
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperatures.append(temperature)
            humidities.append(humidity)

        avg_temp = sum(temperatures) / len(temperatures)
        max_humidity = max(humidities)

        statistics_info = f"Average Temperature: {avg_temp:.2f}°C\nMax Humidity: {max_humidity}%"
        return statistics_info
    else:
        return None

def display_statistics_entry():
     city = entry.get().strip()
     if city:
         statistics_info = calculate_statistics(city)
         if statistics_info:
             messagebox.showinfo("Statistics", statistics_info)
         else:
             messagebox.showwarning("Warning", "failed to calculate statistics.")
     else:
         messagebox.showwarning("Warning", "Please enter a city name.")


def save_data():
    city = entry.get().strip()
    if city:
        data = get_weather(city)
        if data:
            try:
                saved_data = load_saved_data()
                saved_data[city] = data
                # Save updated data to the file
                with open("weather.json", 'w') as file:
                    json.dump(saved_data, file)

                messagebox.showinfo("Success", "Data saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save data: {e}")
        else:
            messagebox.showwarning("Warning", "Failed to save data.")
    else:
        messagebox.showwarning("Warning", "Please enter a city name.")

def load_data():
    city = entry.get().strip()
    if city:
        try:
            saved_data = load_saved_data()
            if city in saved_data:
                weather_info = fetch_weather(city)
                if weather_info:
                    weather_display.config(state='normal')
                    weather_display.delete(1.0, tk.END)
                    weather_display.insert(tk.END, weather_info)
                    weather_display.config(state='disabled')
                else:
                    messagebox.showerror("Error", "Failed to fetch weather data.")
            else:
                messagebox.showwarning("Warning", f"No saved data found for {city}.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter a city name.")


# Function to load saved data from the JSON file
def load_saved_data():
    try:
        with open("weather.json", 'r') as file:
            saved_data = json.load(file)
        return saved_data
    except FileNotFoundError:
        return {}
    except Exception as e:
        raise e


label = tk.Label(r, text="Enter City Name:")
label.pack(pady=10)

entry = tk.Entry(r, width=30)
entry.pack(pady=5)

fetch_button = tk.Button(r, text="Fetch Weather", command=fetch_weather_entry)
fetch_button.pack(pady=10)

statistics_button = tk.Button(r, text="Display Statistics", command=display_statistics_entry)
statistics_button.pack(pady=5)

save_button = tk.Button(r, text="Save Data", command=save_data)
save_button.pack(pady=5)

load_button = tk.Button(r, text="Load Data", command=load_data)
load_button.pack(pady=5)

weather_display = tk.Text(r, height=10, width=50, wrap='word', state='disabled')
weather_display.pack(pady=10)


r.mainloop()




