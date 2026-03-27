import requests

# https://api.weather.gov/points/{lat},{lon}
# NY=39.7456,-97.0892

response = requests.get('https://api.weather.gov/points/39.7456,-97.0892')
data = response.json()

forecast_url = data['properties']['forecast']

forecast_response = requests.get(forecast_url)
forecast_url_dict = forecast_response.json()

print(forecast_url_dict['properties']['periods'][0]['temperature'])
