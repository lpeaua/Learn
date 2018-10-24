#! python3
# Quick_map.py - Quickest way to serach an address on Google Maps. Easy as copying the desired address and then running 
# the quick_map.py app.

# Will be using the webbrowser, sys, and pyperclip modules

import webbrowser, sys, pyperclip

# Add a commandline option to input an address
if len(sys.argv) > 1:
    # Join sys.argv arguments into a single string
    address = '-'.join(sys.argv[1:])
else:
    # Use address in clipboard.
    address = pyperclip.paste()
    
# Use address copied to clipboard or entered via CLI in Google Maps URL
webbrowser.open('https://www.google.com/maps/place/' + address)

