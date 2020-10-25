"""
main driver for program
"""

from dotenv import load_dotenv
load_dotenv()
import os
from gcal import Gcal

client_id = os.environ.get('CLIENT_ID')
project_id = os.environ.get('PROJECT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

# constructor
cal_handler = Gcal()

# try authorize
cal_handler.authorize(client_id, project_id, client_secret)
cal_handler.ten_events()
