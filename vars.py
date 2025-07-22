#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29907731"))
API_HASH = environ.get("API_HASH", "8f59d632cb374705cfdee46ac17cc3cd")
BOT_TOKEN = environ.get("BOT_TOKEN", "8069612418:AAFUfBaVEO3Wy9lVdJochO65rLMfNjbRLuw")

OWNER = int(environ.get("OWNER", "6697397532"))
CREDIT = environ.get("CREDIT", "MJ TEAM❤️")

TOTAL_USER = os.environ.get('TOTAL_USERS', '6697397532').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '6697397532').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
