import os
from datetime import timedelta

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))
load_dotenv(os.path.join(basedir, 'blog/.env'))

SECRET_KEY = os.urandom(36)
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

REMEMBER_COOKIE_DURATION = timedelta(seconds=60)


MAIL_USERNAME = os.environ.get('EMAIL_USER')
MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True





"""
Ненадежные приложения, у которых есть доступ к аккаунту
https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NuwcNk1xMXMXCVGJkgq1HvicbUIgbtJ3m3lknLqC_mJL5XyeqXyhPmIXUvIxQGfoQgddeSG9zcPCPRocy-9JSzzSlAGg

login = testforytlesson@gmail.com
password Qweqaz8485psyX
"""
