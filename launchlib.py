"""
Author: Jacob Chen 2020
launchlib.py
- Class that requests and manages/parses data from the Launch Library API.

Launch Library API created by The Space Devs
https://ll.thespacedevs.com/2.0.0/swagger
- Note that with the free version, the user is limited to a max of 300 requests per day.
"""

import requests
from launch_obj import Launch_obj

# Request the launch data
orig_data = requests.get("https://ll.thespacedevs.com/2.0.0/launch/upcoming")

class Launchlib:
    """
    Init
        - create a json library from the requested data
    """
    def __init__(self):
        self.launch_data = orig_data.json()

    """
    search(self, location, agency): Search through the most recently fetched launch data with specified parameters, and return a list
        of matches, if any
        - Takes in a location and agency string (which will be handled by the interface)
        - Will only filter with parameters != None
    Return value: a list of results
    """
    def search(self, location, agency):
        # List containing all the items
        results_list = []

        if location != None:
            location = location.lower()
        if agency != None:
            agency = agency.lower()

        for result in self.launch_data['results']:
            result_loc = (result['pad']['location']['name']).lower()
            result_ag = (result['launch_service_provider']['name']).lower()

            # print("user inputs")
            # print(location)
            # print(agency)
            # print("comparing to items in data")
            # print(result_loc)
            # print(result_ag)

            if location != None and agency != None:
                if location in result_loc and agency in result_ag:
                    obj = Launch_obj(result['name'], result['pad']['location']['name'],
                                     result['mission']['description'], result['window_start'][0:10], result['window_start'], result['window_end'])
                    results_list.append(obj)
            elif location != None and agency == None:
                if location in result_loc:
                    obj = Launch_obj(result['name'], result['pad']['location']['name'],
                                     result['mission']['description'], result['window_start'][0:10], result['window_start'], result['window_end'])
                    results_list.append(obj)
            elif location == None and agency != None:
                if agency in result_ag:
                    obj = Launch_obj(result['name'], result['pad']['location']['name'],
                                     result['mission']['description'], result['window_start'][0:10], result['window_start'], result['window_end'])
                    results_list.append(obj)
            elif location == None and agency == None:
                obj = Launch_obj(result['name'], result['pad']['location']['name'],
                                 result['mission']['description'], result['window_start'][0:10], result['window_start'], result['window_end'])
                results_list.append(obj)

        return results_list

