import requests

def get_temperature(city, api_key):
    """
    Fetches the current temperature of a city using OpenWeatherMap API.

    Args:
        city (str): Name of the city.
        api_key (str): Your OpenWeatherMap API key.

    Returns:
        str: Temperature information or an error message.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()

        # Extracting temperature details
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        city_name = data['name']
        return f"The current temperature in {city_name} is {temp}°C with {weather}."
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Request error: {req_err}"
    except KeyError:
        return "Could not retrieve temperature. Please check the city name and try again."

# Replace 'your_api_key_here' with your actual API key from OpenWeatherMap
api_key = c601ef2a92251add92fa81a351a197d6
city = input("Enter the city name: ")
print(get_temperature(city, api_key))
