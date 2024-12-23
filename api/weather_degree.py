import tkinter as tk
import requests

# Function to fetch weather data
def get_weather():
    placename = entry.get()  # Get the place name from the entry field

    # API call to fetch weather data
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={placename}&appid=e91dae090ec26a4f8474a5ecbe2cc61c")
    data = response.json()

    # Extract temperature and weather status
    if data.get("main"):
        temp = data["main"]["temp"]
        status = data["weather"][0]["main"]

        # Convert temperature from Kelvin to Celsius
        temp_celsius = temp - 273.15

        # Update the labels with the fetched data
        temp_label.config(text=f"Temperature in {placename} is {temp_celsius:.2f}°C")
        status_label.config(text=f"The weather in {placename} is {status}")
    else:
        # Handle the case where no data is returned (e.g., invalid place name)
        temp_label.config(text="Error: Place not found.")
        status_label.config(text="Please enter a valid place name.")

# Create the main window
window = tk.Tk()
window.title("Weather App")

# Create a label and an entry box for the place name
place_label = tk.Label(window, text="Enter place name:")
place_label.pack()

entry = tk.Entry(window)
entry.pack()

# Create a button to fetch the weather
search_button = tk.Button(window, text="Get Weather", command=get_weather)
search_button.pack()

# Create labels to display the temperature and weather status
temp_label = tk.Label(window, text="Temperature will be displayed here.")
temp_label.pack()

status_label = tk.Label(window, text="Weather status will be displayed here.")
status_label.pack()

# Start the Tkinter event loop
window.mainloop()
