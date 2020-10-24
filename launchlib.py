"""
launchlib_api
- Class that requests and manages/parses data from the Launch Library API.

Launch Library API created by The Space Devs
https://ll.thespacedevs.com/2.0.0/swagger

Note that with the free version, up to 300 requests can be made per day.
"""

import requests

# Request the launch data
launch_data = requests.get("https://ll.thespacedevs.com/2.0.0/launch/upcoming")

class Launchlib:
    def __init__(self):
        self.launch_data = launch_data



