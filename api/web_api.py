import requests

# Replace with your API key from OpenWeather
api_key = 'YOUR_API_KEY'
city = 'London'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# Sending a GET request to the API
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the JSON response
    data = response.json()
    print(f"Weather in {city}: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}K")
else:
    print(f"Error: Unable to fetch data (status code: {response.status_code})")
