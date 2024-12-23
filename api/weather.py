import tkinter as tk
from tkinter import messagebox
import requests

# Replace with your OpenWeather API key
api_key = 'YOUR_API_KEY'

# Function to fetch weather data
def get_weather():
    city = city_entry.get()  # Get the city name from the input field
    
    if not city:
        messagebox.showerror("Error", "Please enter name!")
        return
    
    # Set up the API URL and parameters
    base_url = "https://api.openweathermap.org/data/2.5/weather?q={placename}&appid=e91dae090ec26a4f8474a5ecbe2cc61c"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Celsius temperature
        'lang': 'en'
    }
    
    # Send the GET request to OpenWeather API
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        
        # Extract relevant data from the response
        city_name = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        
        # Display the weather information in the label
        weather_info = (f"Weather in {city_name}:\n"
                        f"Temperature: {temperature}°C\n"
                        f"Humidity: {humidity}%\n"
                        f"Description: {description.capitalize()}")
        result_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", f"City not found or API error. Status code: {response.status_code}")

# Create the main window
window = tk.Tk()
window.title("Weather App")

# Create and place the city entry label and input field
city_label = tk.Label(window, text="Enter City Name:")
city_label.pack(pady=5)

city_entry = tk.Entry(window)
city_entry.pack(pady=5)

# Create and place the Get Weather button
get_weather_button = tk.Button(window, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

# Create and place the result label to display weather info
result_label = tk.Label(window, text="", font=("Helvetica", 12), justify="left")
result_label.pack(pady=10)

# Run the application
window.mainloop()
