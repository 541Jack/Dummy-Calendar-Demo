from pprint import pprint
from sys import api_version
from Google import Create_Service

# Defining constants
CLIENT_SECRET_FILE = 'client_secret_dummy.json'  # secret file name
API_NAME = 'calendar'
API_VERSION = 'V3'
# Located in google api website
SCOPES = ['https://www.googleapis.com/auth/calendar']

# creating new object
# Creates the service object that can use google api methods
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

print(dir(service))
