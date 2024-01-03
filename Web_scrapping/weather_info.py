import requests
from bs4 import BeautifulSoup

url = "https://weather.com/ro-RO/vreme/astazi/l/ROXX0003:1:RO"

webpage = requests.get(url)
soup = BeautifulSoup(webpage.text, "html.parser")

# Temperature info
temperature_element = soup.find(class_="CurrentConditions--tempValue--MHmYY")

if temperature_element:
    temperature = temperature_element.get_text().strip()
    print(f"The current temperature in Bucharest: {temperature}")
else:
    print("Unable to fetch weather data")

# Conditions info
conditions_element = soup.find(class_="CurrentConditions--phraseValue--mZC_p")

if conditions_element:
    conditions = conditions_element.get_text().strip()
    print(f"The weather conditions in Bucharest: {conditions}")
else:
    print("Unable to fetch weather conditions")