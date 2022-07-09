from calendar import calendar
from pprint import pprint
from sys import api_version
from urllib import response
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_dummy.json'
API_NAME = 'calendar'
API_VERSION = 'V3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

request_body = {  # request body object, which is an dictionary
    'summary': 'Dining Events'  # calendar title
}

"""
Create Calendar
"""
# response = service.calendars().insert(
#    body=request_body).execute()  # create calendar with insert
# print(response)

"""
Delete Calendar
"""
service.calendars().delete(
    calendarId='gp7bc5ha94odj50a3dk41osv5k@group.calendar.google.com').execute()
