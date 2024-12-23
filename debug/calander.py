import calendar
import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Function to display the calendar
class NepaliCalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nepali Calendar")
        self.root.geometry("600x700")
        self.root.configure(bg="white")

        # Current year and month for navigation
        self.current_year = 2081  # Default Nepali year
        self.current_month = 1  # Baishakh

        # Nepali Month Names
        self.nepali_months = [
            "बैशाख", "जेष्ठ", "आसार", "श्रावण", "भाद्र", 
            "अश्विन", "कार्तिक", "मंसिर", "पौष", "माघ", "फाल्गुण", "चैत्र"
        ]

        # Top Navigation Bar
        nav_frame = tk.Frame(self.root, bg="white")
        nav_frame.pack(pady=10)
        
        self.year_label = tk.Label(nav_frame, text=f"Year: {self.current_year}", font=("Helvetica", 16), bg="white")
        self.year_label.grid(row=0, column=1, padx=20)
        
        prev_button = ttk.Button(nav_frame, text="<< Previous", command=self.prev_year)
        prev_button.grid(row=0, column=0)

        next_button = ttk.Button(nav_frame, text="Next >>", command=self.next_year)
        next_button.grid(row=0, column=2)

        # Calendar Display Frame
        self.calendar_frame = tk.Frame(self.root, bg="white")
        self.calendar_frame.pack(fill="both", expand=True)
        self.display_calendar()

    def display_calendar(self):
        # Clear the current frame
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        # Display months with days
        for idx, month in enumerate(self.nepali_months):
            month_frame = tk.Frame(self.calendar_frame, borderwidth=2, relief="ridge", bg="white")
            month_frame.grid(row=idx // 3, column=idx % 3, padx=10, pady=10)

            # Month Title
            month_label = tk.Label(month_frame, text=month, font=("Helvetica", 14, "bold"), bg="white")
            month_label.pack(pady=5)

            # Generate days (1 to 30 for now, static example)
            days_frame = tk.Frame(month_frame, bg="white")
            days_frame.pack()

            for day in range(1, 31):
                day_label = tk.Label(days_frame, text=f"{day:02d}", font=("Helvetica", 10), width=4, bg="white", relief="groove")
                day_label.grid(row=(day-1) // 7, column=(day-1) % 7, padx=2, pady=2)

    def prev_year(self):
        self.current_year -= 1
        self.year_label.config(text=f"Year: {self.current_year}")
        self.display_calendar()

    def next_year(self):
        self.current_year += 1
        self.year_label.config(text=f"Year: {self.current_year}")
        self.display_calendar()

if __name__ == "__main__":
    root = tk.Tk()
    app = NepaliCalendarApp(root)
    root.mainloop()
