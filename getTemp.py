#! python3
# currentTemp.py - display the current temperature

from selenium import webdriver
browser = webdriver.Firefox()

browser.get("http://inventwithpython.com")

try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that call name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
