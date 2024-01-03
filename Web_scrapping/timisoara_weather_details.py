import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/weather/665087"
webpage = requests.get(url)

soup = BeautifulSoup(webpage.text, "html.parser")

# Time of observation
observation_el = soup.find(class_="wr-c-observations__timestamp gel-long-primer gs-u-mt--")

if observation_el:
    observation = observation_el.get_text().strip()
    print(observation)
    print("-----------------")
else:
    print("Unable to fetch observation data")

# Current temperature
temp_el = soup.find(class_="wr-value--temperature--c")

if temp_el:
    temp = temp_el.get_text().strip()
    print(f"Current temperature in Timisoara: {temp}\n")
else:
    print("Unable to fetch temperature data")

# Info
info_el = soup.find(class_="wr-c-station-data gs-u-pl0 gs-u-mv0").find_all("li")
if info_el:
    info = "\n".join(info.get_text(strip=True) for info in info_el)
    print(f"Info:\n\n{info}")
else:
    print("Unable to fetch info")

# Description
description_el = soup.find(
    class_="wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque")

if description_el:
    description = description_el.get_text().strip()
    print("\n" + description)
else:
    print("Unable to fetch description")