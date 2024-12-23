import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather data
def get_weather():
    placename = place_entry.get()

    if not placename:
        messagebox.showwarning("Input Error", "Please enter a place name.")
        return

    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={placename}&appid=e91dae090ec26a4f8474a5ecbe2cc61c")
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "Could not find the place. Please check the name and try again.")
            return

        # Extracting weather information
        temp = data["main"]["temp"]
        status = data["weather"][0]["main"]

        # Temperature in Kelvin to Celsius
        temp_celsius = round(temp - 273.15, 2)

        # Update weather display
        weather_label.config(text=f"The temperature in {placename} is {temp_celsius}°C\nStatus: {status}")

        # Generate an essay based on the place name
        generate_essay(placename)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network Error", f"Failed to retrieve weather data: {str(e)}")

# Function to generate an essay based on the location
def generate_essay(placename):
    essay_text = f"Essays about {placename}:\n\n"
    essay_text += f"{placename} is a fascinating place known for its unique culture, history, and geography. "
    essay_text += f"Located in a beautiful part of the world, {placename} has much to offer visitors and locals alike. "
    essay_text += f"The climate of {placename} varies depending on the season, but it is often characterized by its "
    essay_text += f"pleasant temperatures and occasional changes in weather. Whether you're a tourist or a resident, "
    essay_text += f"there's always something new to discover in {placename}. From its iconic landmarks to its hidden gems, "
    essay_text += f"{placename} never fails to leave a lasting impression on those who visit."

    essay_text_box.config(state=tk.NORMAL)  # Enable editing of text box
    essay_text_box.delete(1.0, tk.END)  # Clear previous text
    essay_text_box.insert(tk.END, essay_text)  # Insert new essay
    essay_text_box.config(state=tk.DISABLED)  # Disable editing of text box

# Set up the main window
root = tk.Tk()
root.title("Weather and Essay Generator")

# Set up the place name input
place_label = tk.Label(root, text="Enter the place name:")
place_label.pack(pady=10)

place_entry = tk.Entry(root, width=30)
place_entry.pack(pady=5)

# Set up the "Get Weather" button
weather_button = tk.Button(root, text="Get Weather & Essay", command=get_weather)
weather_button.pack(pady=20)

# Label to display weather info
weather_label = tk.Label(root, text="", font=("Helvetica", 12))
weather_label.pack(pady=10)

# Text box to display the essay
essay_text_box = tk.Text(root, height=10, width=50, wrap=tk.WORD, font=("Helvetica", 10))
essay_text_box.pack(padx=20, pady=10)
essay_text_box.config(state=tk.DISABLED)  # Make text box non-editable

# Run the application
root.mainloop()