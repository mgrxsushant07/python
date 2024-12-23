import tkinter as tk
import time

# Flag to toggle between 12-hour and 24-hour formats
is_12hr_format = True

# Function to update the time and date
def update_time():
    global is_12hr_format
    current_time = time.strftime("%I:%M:%S %p" if is_12hr_format else "%H:%M:%S")
    current_date = time.strftime("%A, %B %d, %Y")  # Format for full date
    time_label.config(text=current_time)
    date_label.config(text=current_date)

    # Update background color based on time
    hour = int(time.strftime("%H"))
    if 6 <= hour < 18:
        root.config(bg="white")  # Daytime (6 AM - 6 PM)
    else:
        root.config(bg="white")   # Nighttime (6 PM - 6 AM)

    # Call the update_time function every 1000ms (1 second)
    time_label.after(1000, update_time)

# Toggle between 12-hour and 24-hour formats
def toggle_format(event):
    global is_12hr_format
    is_12hr_format = not is_12hr_format
    update_time()  # Update the time display when toggling

# Function to minimize the window
def minimize_window():
    root.iconify()  # Minimizes the window

# Create the main window
root = tk.Tk()
root.title("Sushant Gaha Magar")  # Set window title

# Set the window to full screen
root.attributes("-fullscreen", True)

# Create labels to display time and date with updated colors
time_label = tk.Label(root, font=("Helvetica", 80), fg="black", bg="white")
time_label.pack(anchor="center", padx=20, pady=20)

date_label = tk.Label(root, font=("Helvetica", 30), fg="black", bg="white")
date_label.pack(anchor="center", padx=20, pady=10)

# Create a "Minimize" button
minimize_button = tk.Button(root, text="Minimize", font=("Helvetica", 15), fg="black", bg="white", command=minimize_window)
minimize_button.pack(side="bottom", pady=20)

# Bind the key 't' to toggle between 12-hour and 24-hour formats
root.bind('t', toggle_format)

# Start the clock
update_time()

# Start the Tkinter event loop
root.mainloop()
