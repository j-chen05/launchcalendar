"""
Author: Jacob Chen 2020
gcalendar_api
- Class that requests and manages/parses data from the Google Calendar API.
- If user wishes to use this app, they must authorize their Google account when prompted.

Google Calendar API by Google:
https://developers.google.com/calendar/v3/reference
"""

from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from launch_obj import Launch_obj

# Scope of the program (in this case, read/write access to the main calendar
SCOPES = ['https://www.googleapis.com/auth/calendar']

class Gcal:
    def __init__(self):
        self.creds = None
        self.service = None

    """ALWAYS INVOKE THIS FUNCTION FIRST
    authorize(): Authorize the app for read/write access to your Google Calendar
    Usage:
        - After executing, the function will open up a default browser tab to prompt the user to log 
        into their Google account.
        - Failure to log in will not allow app to function.
    """
    def authorize(self, client_id, project_id, client_secret):
        """
        Code taken from the Python quickstart code on Google Calendar API's documentation website
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('API Data/token.pickle'):
            with open('API Data/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                clientcfg = {"installed":
                                    {"client_id":client_id,
                                     "project_id":project_id,
                                     "auth_uri":"https://accounts.google.com/o/oauth2/auth",
                                     "token_uri":"https://oauth2.googleapis.com/token",
                                     "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
                                     "client_secret":client_secret,
                                     "redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}
                flow = InstalledAppFlow.from_client_config(client_config=clientcfg, scopes=SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('API Data/token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        # Log creds with self variable
        self.creds = creds
        self.service = build('calendar', 'v3', credentials=self.creds)

    """
    event_exists(launch_event): Check if the provided launch event already exists, and if so, return that event
        - User passes in a launch_obj, which is then compared to all the events on the day of this launch_obj, to see
        if this event has been added already
    Return value: returns a Google Calendar event if the launch_obj event is indeed on your calendar already
                  returns None if the launch_obj event was not on your calendar 
                  (it is new or something changed about the launch's identity)
    """
    def event_exists(self, launch_event):
        # Get date and summary of launch event
        date = launch_event.date
        summary = launch_event.name

        # Get start and end times for the date of this launch event
        start = date + 'T' + '00:00:00' + 'Z'
        end = date + 'T' + '23:59:59' + 'Z'

        # Create list of events on the launch event's day, and see if any events match with the summary
        # if so, return that event
        events = self.service.events().list(calendarId='primary', timeMin=start, timeMax=end).execute()
        for event in events['items']:
            this_event_summary = event['summary']
            if this_event_summary == summary:
                return event

        # if no events matched, that means this is a new event. Return None.
        return None

    """
    update(launch_event, event_to_update): update a selected event to the most recent information gathered by the 
    Launch Library API
        - User provides a launch_obj and an event they would like to update
        - Function will fetch the current data, namely time and description
    """
    def update(self, launch_event, event_to_update):
        new_event = self.service.events().get(calendarId='primary', eventId=event_to_update['id']).execute()

        # Update time/description components of the event
        new_event['start']['dateTime'] = launch_event.window_start[0:19] + '-07:00'
        new_event['end']['dateTime'] = launch_event.window_end[0:19] + '-07:00'
        new_event['description'] = launch_event.description

        # Update the event
        self.service.events().update(calendarId='primary', eventId=new_event['id'], body=new_event).execute()

    """
    add(launch_event)
    - add the provided launch_obj to your calendar
    """
    def add(self, launch_event):
        # Get the user's timezone settings
        tz = self.service.settings().get(setting='timezone').execute()
        timezone = tz['value']

        # Customize a new event in Calendar API's format
        event = {
            'summary': launch_event.name,
            'location': launch_event.location,
            'description': launch_event.description,
            'start': {
                'dateTime': launch_event.window_start[0:19] + '-07:00',
                'timeZone': timezone,
            },
            'end': {
                'dateTime': launch_event.window_end[0:19] + '-07:00',
                'timeZone': timezone,
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }

        # Add event to calendar
        event = self.service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))
