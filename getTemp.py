#! python3
# currentTemp.py - display the current temperature

#! python3
# currentTemp.py - display the current temperature

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

# Prompt for location of desired temperature
print("Please enter city and state:\n")
city = input('City: ')
state = input("State: ")
country = input("Country: ")
# Open National Weather website and grab location search bar
browser = webdriver.Firefox()
browser.get("https://www.weather.gov/")
linkElem = browser.find_element_by_id('inputstring')

# Clear existing text in search bar, insert inputted location and navigate to location site
linkElem.clear()
linkElem.send_keys(city.title() + ', ' + state.upper() + ', ' +country.upper()).click()
#linkElem.send_keys(Keys.ENTER)
buttonElem = browser.find_element_by_id('btnSearch').click()
#buttonElem.send_keys(Keys.ENTER)
