from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_699251265289-opjl7q7oj2hpe4vfdlleoepilsj07ls8.apps.googleusercontent.com.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']
API_KEY = 'AIzaSyA2kzvUJ7QvT_2NLSEw2ReNrLziQ3rZHgg'

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES, API_KEY)