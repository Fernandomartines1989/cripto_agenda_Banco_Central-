import os
import requests
import getpass
import json

from bs4 import BeautifulSoup
from datetime import datetime

from flask import Flask

TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY_2"]
TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID_2"]

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "Olá, mundo!"
