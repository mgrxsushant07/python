import requests

placename = input("Enter the place name: ")

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={placename}&appid=e91dae090ec26a4f8474a5ecbe2cc61c")
data =  response.json()

temp = data["main"]["temp"]
status = data["weather"][0]["main"]

# Temperature in Kelvin. Convert it to Celsius
temp_celsius = temp - 273.15

print(f"Temperature in {placename} is {(temp_celsius)} degrees Celsius")
print(f"The weather in {placename} is {status}")

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

def get_essay_by_title(api_url, api_key, title):
    """
    Generate an essay by passing the title.

    Args:
        api_url (str): The API endpoint URL.
        api_key (str): The API authentication key.
        title (str): The topic or title of the essay.

    Returns:
        str: The generated essay content.
    """
    return generate_essay(api_url, api_key, title)


API_URL = "https://api.x.ai/v1/chat/completions"
API_KEY = "xai-deZJiuQEXJbLC6oYZRty61joqJ8J0xTmGdOLloh4bGoZAUan1lebvmlZtQ0BJxXmXuWE9V3pnAqM9Tcu"


try:
    essay = get_essay_by_title(API_URL, API_KEY, placename)
    print("Generated Essay:\n")
    print(essay)
except Exception as e:
    print(f"Failed to generate essay: {e}")