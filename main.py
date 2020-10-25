"""
main driver for program
"""

from dotenv import load_dotenv
load_dotenv()

import os
from gcal import Gcal
from launchlib import Launchlib


def run_interface():
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

            # Search with these parameters
            test = Launchlib()
            results = test.search(location, agency)

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






client_id = os.environ.get('CLIENT_ID')
project_id = os.environ.get('PROJECT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

# constructor
cal_handler = Gcal()

# try authorize
cal_handler.authorize(client_id, project_id, client_secret)

print("Welcome to Launch Calendar!")

run_interface()

print("See you space cowboy!")