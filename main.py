"""
main driver for program
"""

from dotenv import load_dotenv
load_dotenv()

import os
from gcal import Gcal

client_id = os.environ.get('CLIENT_ID')
project_id = os.environ.get('PROJECT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

# constructor
cal_handler = Gcal()

# try authorize
cal_handler.authorize(client_id, project_id, client_secret)

print("Welcome to Launch Calendar!")
print("Filter by location: enter your country, otherwise, type 'skip'")

# Part 1: set location filters
location = None
agency = None
while True:
    loc = input()
    if loc != "skip" and loc != "" :
        location = loc
        print("Location: " + location)
    elif loc == "":
        print("Please enter a valid country.")
        continue
    elif loc == "skip":
        location = None
    break

# Part 2: set agency filters
print("Filter by agency: enter the name of a preferred agency, otherwise, type 'skip'")
while True:
    ag = input()
    if ag != "skip" and ag != "":
        agency = ag
        print("Agency: " + agency)
    elif ag == "":
        print("Please enter a valid agency.")
        continue
    elif ag == "skip":
        ag = None
    break

# Search with these parameters

# Ask if user wants to add a specific event to calendar (input number of result)


# if found: display results, if not found, prompt user to try again or quit
    # in this case, reexecute function







print(location)
print(agency)






print("See you space cowboy!")