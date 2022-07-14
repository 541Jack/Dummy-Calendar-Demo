import colorsys
from pprint import pprint
from sys import api_version
from tracemalloc import start
from urllib import response
from Google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE = 'client_secret_dummy.json'
API_NAME = 'calendar'
API_VERSION = 'V3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# ID of the event
calendar_id_dining = '3g56esarnq7pm727nq513dvqgc@group.calendar.google.com'

"""
Create Event
"""

colors = service.colors().get().execute()  # get color
# pprint(colors)

event_request_body = {
    'start': {  # start time
        # year, month, day, hour, minute
        'dateTime': convert_to_RFC_datetime(2022, 7, 12, 18, 30),
        'timeZone': 'America/New_York'
    },
    'end': {  # end time
        'dateTime': convert_to_RFC_datetime(2022, 7, 12, 19, 00),
        'timeZone': 'America/New_York'
    },
    'summary': 'BBQ party',  # event title
    'description': 'BBQ party baby!',
    'colorId': 5,  # 5th color on palette
    'status': 'confirmed',
    'transparency': 'opaque',  # if the event blocks the time, default is opaque
    'location': 'West_Lafayette, IN',
    # 'attachments' {
    # fileurl here:
    # }
    'attendees': [
        {  # attendee number 1
            'displayname': 'Jack',
            'comment': 'hi',
            'email': 'zlgod1972dummy@gmail.com',  # must require e-mail
            'optional': False,
            'organizer': True,
            'responseStatus': 'accepted'
        }
    ]
}

maxAttendee = 5
sendNotification = True
sendUpdate = 'none'
# supportAttachments

response = service.events().insert(
    calendarId=calendar_id_dining,
    maxAttendees=maxAttendee,
    sendNotifications=sendNotification,
    sendUpdates=sendUpdate,
    body=event_request_body
).execute()

pprint(response)
