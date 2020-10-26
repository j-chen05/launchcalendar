"""
Author: Jacob Chen 2020
main.py
- Main driver for Launch Calendar.
- Launch Calendar is a command-line app that lets you search for the most recent rocket launches by location and agency
and potentially add them to your Google Calendar.
"""

import os
from gcal import Gcal
from launchlib import Launchlib
from dotenv import load_dotenv
load_dotenv()

"""
run_interface(cal_handler): Runs the main interface a user will see on their command line.
    - Grabs recent launch data within, by instantiating a new launchlib object.
    - Must provide a Gcal class as parameter.
"""
def run_interface(cal_handler):
    location = None
    agency = None

    # Part 1: ask user for location filters
    while True:
        print("Filter by location: enter name of a country, or location keyword; otherwise, type 'skip'")
        loc = input()
        if loc != "skip" and loc != "":
            location = loc
            print("Searching for launches in " + location)
        elif loc == "":
            print("Please enter a valid name or keyword.")
            continue
        elif loc == "skip":
            location = None

        # Part 2: ask user for agency filters
        print("Filter by agency: enter name of a preferred agency, or agency keyword; otherwise, type 'skip'")
        while True:
            ag = input()
            if ag != "skip" and ag != "":
                agency = ag
                print("Searching for launches by " + agency)
            elif ag == "":
                print("Please enter a valid name or keyword.")
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
                print()
                print("Enter 's' to search again. Enter 'q' to quit.")
                while True:
                    user = input()
                    if user == "s":
                        break
                    elif user == "q":
                        return
                    else:
                        print("Enter 's' to search again. Enter 'q' to quit.")
                        continue
                # break out of this loop (return to the first one)
                break
            # if launches found, display results
            else:
                print()
                print("[" + str(len(results)) + "]" + " launches found:")
                count = 1
                for launch in results:
                    print(str(count))
                    print(launch)
                    print("---------------------------")
                    count += 1

                # Part 4: Ask if user wants to put anything in their calendar
                while True:
                    print("Input the integer of the event you would like to add to your calendar.")
                    print("Or, enter 's' to search again, or 'q' to quit.")
                    ID = input()

                    # If an integer was input
                    # Try to convert to an integer
                    integerID = 0
                    try:
                        integerID = int(ID)
                    # If can't convert, then it was either a key or something else
                    except ValueError:
                        if ID == 's':
                            print()
                            break
                        if ID == 'q':
                            return
                        print("Please enter a valid character or integer.")
                        print()
                        continue
                    # Check if the integer was in range
                    if 1 <= integerID <= len(results):
                        integerID -= 1
                        # Check if this event exists in the calendar, first.
                        event = cal_handler.event_exists(results[integerID])

                        if event:
                            print("The launch of " + results[integerID].name + " on " + results[integerID].date + " was already detected in your calendar. "
                                  "Updating to most recent launch information.")
                            cal_handler.update(results[integerID], event)
                        else:
                            cal_handler.add(results[integerID])
                            print("Created a new event for the " + results[integerID].name + " launch in your calendar on " + results[integerID].date + ".")
                        print()
                        continue

                    # Go back to original prompt if int was out of range
                    else:
                        print("There is no rocket launch by this number.")
                        print()
                        continue

                # For the path where s is input: go back to search
                break



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
print("Launch Calendar will search for upcoming rocket launches that you can add to your Google Calendar.")
print("First, provide search filters, if desired. Note searches are NOT case sensitive.")
# Main interface function
run_interface(cal_handler)

# End
print()
print("Go see those launches! (if you can!!)")
print("Thanks for using Launch Calendar. Safe flying!")

