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

print('Hi, this is event creater')

# User enter their desired time
# For demo purpose, this will be an 1 hour event

inputCalId = input('please enter your calendar id: ')
startYear = input('please enter the start year: ')
startMonth = input('please enter the start month: ')
startDay = input('please enter the start day: ')
startHour = input('please enter the start hour: ')
startMinute = input('please enter the start minute: ')

# convert string to int
startYear = int(startYear)
startMonth = int(startMonth)
startDay = int(startDay)
startHour = int(startHour)
startMinute = int(startMinute)

#title and name
eventTitle = input('please enter event title: ')
eventDescription = input('please enter event description: ')

# status
eventTransparancy = input('Is event confirmed (y/n): ')

if ((eventTransparancy == 'y') or (eventTransparency == 'Y')):
    eventTransparancy = 'confirmed'
else:
    eventTransparancy = 'tentative'

event_request_body = {
    'start': {  # start time
        # year, month, day, hour, minute
        'dateTime': convert_to_RFC_datetime(startYear, startMonth, startDay, startHour, startMinute),
        'timeZone': 'America/New_York'
    },
    'end': {  # end time
        'dateTime': convert_to_RFC_datetime(startYear, startMonth, startDay, (startHour + 1), startMinute),
        'timeZone': 'America/New_York'
    },
    'summary': eventTitle,  # event title
    'description': eventDescription,
    'colorId': 5,  # 5th color on palette
    'status': eventTransparancy,
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
    calendarId=inputCalId,
    maxAttendees=maxAttendee,
    sendNotifications=sendNotification,
    sendUpdates=sendUpdate,
    body=event_request_body
).execute()
