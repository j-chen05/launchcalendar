"""
Author: Jacob Chen 2020
main.py
- Main driver for Launch Calendar.
- Launch Calendar is a command-line interface that lets you search for the most recent rocket launches by location and agency
and potentially add them to your Google Calendar.
"""

import os
from gcal import Gcal
from launchlib import Launchlib
from dotenv import load_dotenv
load_dotenv()

def run_interface(cal_handler):
    location = None
    agency = None

    # Part 1: ask user for location filters
    while True:
        print("Filter by location: enter a country name, otherwise, type 'skip'")
        loc = input()
        if loc != "skip" and loc != "":
            location = loc
            print("Searching for launches in " + location)
        elif loc == "":
            print("Please enter a valid country.")
            continue
        elif loc == "skip":
            location = None

        # Part 2: ask user for agency filters
        print("Filter by agency: enter the name of a preferred agency, otherwise, type 'skip'")
        while True:
            ag = input()
            if ag != "skip" and ag != "":
                agency = ag
                print("Searching for launches by " + agency)
            elif ag == "":
                print("Please enter a valid agency.")
                continue
            elif ag == "skip":
                agency = None

            # Initialize a new instance of the Launch Library API
            launch_library = Launchlib()
            # Search it with these parameters
            results = launch_library.search(location, agency)

            # Part 3: display results
            # if no launches found, prompt user to start over or quit
            if not len(results):
                print("No launches found for the specified filters.")
                print("Enter 'y' to search again. Enter 'q' to quit.")
                while True:
                    user = input()
                    if user == "y":
                        break
                    elif user == "q":
                        return
                    else:
                        print("Enter 'y' to search again. Enter 'q' to quit.")
                        continue
                # break out of this loop (return to the first one)
                break
            # if launches found, display results
            else:
                print("[" + str(len(results)) + "]" + " launches found:")
                count = 1
                for launch in results:
                    print(str(count))
                    print(launch)
                    print("---------------------------")
                    count += 1

                # Part 4: Ask if user wants to put anything in their calendar
                event = cal_handler.event_exists(results[0])
                if event:
                    print("This launch was already detected in your calendar. Updating to most up-to-date information.")
                    cal_handler.update(results[0], event)
                else:
                    cal_handler.add(results[0])
                    print("Added this event to your calendar.")




# Get env variables for authorization
client_id = os.environ.get('CLIENT_ID')
project_id = os.environ.get('PROJECT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

# Construct a new instance of the Gcal class
cal_handler = Gcal()

# Try to authorize the user's GOogle Account
cal_handler.authorize(client_id, project_id, client_secret)

# Program start
print("Welcome to Launch Calendar!")
# Main interface function
run_interface(cal_handler)

# End
print("See you space cowboy!")