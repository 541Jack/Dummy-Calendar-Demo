from pprint import pprint
from sys import api_version
from urllib import response
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_dummy.json'
API_NAME = 'calendar'
API_VERSION = 'V3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
