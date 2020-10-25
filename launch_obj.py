"""
launch_obj.py
- Class/struct that stores relevant data about a particular launch

"""

class Launch_obj:
    """
    Init
        - init with relevant input values
    """
    def __init__(self, name="none provided", location="none provided", description="none provided",
                 window_start="none provided", window_end="none provided"):
        self.name = name
        self.location = location
        self.description = description
        self.window_start = window_start
        self.window_end = window_end

    def __str__(self):
        return "Launch Vehicle: " + self.name + "\n" + "Location: " + self.location + "\n" + "Purpose of launch: " \
               + self.description + "\n" + "Launch time frame: " + self.window_start + " -- " + self.window_end

