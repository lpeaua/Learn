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
# Open National Weather website and grab location search bar
browser = webdriver.Firefox()
browser.get("https://weather.com/")
linkElem = browser.find_element_by_class_name('theme__inputElement__4bZUj input__inputElement__1GjGE')

# Clear existing text in search bar,  insert inputted location and navigate to location site
linkElem.clear()
linkElem.send_keys(city.title() + ', ' + state.upper(), Keys.ENTER)
#linkElem.submit()
#buttonElem = browser.find_element_by_name('getForecast')
#buttonElem.submit()
