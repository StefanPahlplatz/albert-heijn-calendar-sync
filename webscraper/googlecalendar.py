from __future__ import print_function
import httplib2
import os
import datetime
from calendar import monthrange

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at "C:\Users\user\.credentials\albert-heijn-calendar-sync.json"
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Albert Heijn Calendar Sync'


class Calendar:
    @staticmethod
    def get_credentials():
        """Gets valid user credentials from storage.
    
        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.
    
        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'albert-heijn-calendar-sync.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    def __init__(self):
        """ Initializes the calendar by authenticating.

            Creates a Google Calendar API service object.
        """
        # Initialize a calendar connection.
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        self.service = discovery.build('calendar', 'v3', http=http)

        # Get the event bounds.
        firstofmonth = datetime.datetime.today().replace(day=1).isoformat() + 'Z'  # 'Z' indicates UTC time
        lastofmonth = datetime.datetime.today().replace(month=datetime.datetime.now().month + 1, day=1).isoformat() + \
                      'Z'  # 'Z' indicates UTC time

        # Get this months events.
        events_result = self.service.events().list(
            calendarId='primary', timeMin=firstofmonth, timeMax=lastofmonth, maxResults=20, singleEvents=True,
            orderBy='startTime').execute()

        # Save the events to check for duplicates later.
        self.events = events_result.get('items', [])
        
        # Filter events to only have work events.
        self.events = [ev for ev in self.events if ev['description'] == 'Event created by Stefan Pahlplatz\'s ' +
                       'webscraper.']

    def insert_event(self, event):
        """ Inserts an event into the calendar.
        
            :param event: JSON representation of the to be inserted event. For reference look at
            https://developers.google.com/google-apps/calendar/create-events
        """
        # Check if the event already exists.
        if any(event['start']['dateTime'] == x['start']['dateTime'] for x in self.events):
            return

        # Insert event.
        self.service.events().insert(calendarId='primary', body=event).execute()
