"""
Author: Jacob Chen 2020
launch_obj.py
- Class/struct that represents a launch event (referred to as launch_event in many locations in the code)
- Stores relevant information about a given launch event provided by the Launch Library API.
"""

class Launch_obj:
    """
    Init
        - init with relevant input values
    """
    def __init__(self, name="none provided", location="none provided", description="none provided",
                 date="none provided", window_start="none provided", window_end="none provided"):
        self.name = name
        self.location = location
        self.description = description
        self.date = date
        self.window_start = window_start
        self.window_end = window_end

    """
    Str
        - print out all information in readable format
    """
    def __str__(self):
        return "Launch Vehicle: " + self.name + "\n" + "Location: " + self.location + "\n" + "Purpose of launch: " \
               + self.description + "\n" + "Launch date: " + self.date + "\n" + "Launch window (UTC): " \
               + self.window_start + " -- " + self.window_end

