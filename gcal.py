"""
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

# Scope of the program (in this case, read/write access to the main calendar
SCOPES = ['https://www.googleapis.com/auth/calendar']

class Gcal:
    def __init__(self):
        self.creds = None

    """ALWAYS INVOKE THIS FUNCTION FIRST
    authorize(): Authorize the app for read/write access to your Google Calendar
    Usage:
        - After executing, the function will open up a default browser tab to prompt the user to log 
        into their Google account.
        - Failure to log in will not open app functionality.
    """
    def authorize(self):
        """
        Code taken from the Python quickstart code on Google Calendar API's documentation website
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('./APIs/token.pickle'):
            with open('./APIs/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    './APIs/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('./APIs/token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.creds = creds


    # print out the first 10 events
    def ten_events(self):
        service = build('calendar', 'v3', credentials=self.creds)

        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

