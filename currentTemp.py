#! python3
# currentTemp.py - display the current temperature

import webbrowser, requests, sys, bs4

print("Enter city: ")
city = input()
print("Enter State: ")
state = input()

# Download url
res = requests.get("https://www.theweathernetwork.com/us/weather/" + state + "/" + city)
res.raise_for_status()

# Convert into BeautifulSoup object
soup = bs4.BeautifulSoup(res.text,'html.parser')
tempElem = soup.select('span.temp')
print(tempElem[0].getText())

