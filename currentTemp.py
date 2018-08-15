#! python3
# currentTemp.py - display the current temperature

import webbrowser, requests, sys, bs4

# Download url
print("Retrieving Current Temperature...")
res = requests.get("https://forecast.weather.gov/MapClick.php?lat=40.380220000000065&lon=-111.98801999999995#.W3J2bNJKibg")
res.raise_for_status()

# Convert into BeautifulSoup object
soup = bs4.BeautifulSoup(res.text, "html.parser")
tempElem = soup.select('#current_conditions-summary p')
print(tempElem[1].getText())

print("Hello World")
