import tkinter as tk
from tkinter import messagebox
import requests
import json

def generate_essay(api_url, api_key, topic, model="grok-beta", temperature=0.7):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    messages = [
        {"role": "system", "content": "You are an essay-writing assistant who writes essays in 50 words."},
        {"role": "user", "content": f"Write a detailed essay on the topic: {topic}."}
    ]

    payload = {
        "messages": messages,
        "model": model,
        "temperature": temperature
    }

    response = requests.post(api_url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()
        return result.get("choices", [{}])[0].get("message", {}).get("content", "")
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

def generate_essay_gui():
    topic = topic_entry.get()
    if not topic:
        messagebox.showerror("Error", "Please enter a topic.")
        return

    try:
        essay = generate_essay(API_URL, API_KEY, topic)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, essay)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate essay: {e}")

# Constants
API_URL = "https://api.x.ai/v1/chat/completions"
API_KEY = "xai-deZJiuQEXJbLC6oYZRty61joqJ8J0xTmGdOLloh4bGoZAUan1lebvmlZtQ0BJxXmXuWE9V3pnAqM9Tcu"

# Create the main window
root = tk.Tk()
root.title("Essay Generator")

# Create and place widgets
tk.Label(root, text="Enter the topic for the essay:").pack(pady=5)
topic_entry = tk.Entry(root, width=50)
topic_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Essay", command=generate_essay_gui)
generate_button.pack(pady=10)

result_text = tk.Text(root, wrap=tk.WORD, width=60, height=15)
result_text.pack(pady=5)

# Run the main event loop
root.mainloop()