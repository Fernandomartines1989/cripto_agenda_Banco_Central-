import os
import requests
import getpass
import json

from bs4 import BeautifulSoup
from datetime import datetime

from flask import Flask

import re

import httpx

hoje = datetime.now().strftime("%Y-%m-%d")
data = httpx.get(f"https://www.bcb.gov.br/api/servico/sitebcb/agendadiretoria?lista=Agenda%20da%20Diretoria&inicioAgenda=%27{hoje}%27&fimAgenda=%27{hoje}%27")

dados = data.json()

desc = dados["conteudo"][0]["descricao"]

parsed = BeautifulSoup(desc, "html.parser")

TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY_2"]
TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID_2"]

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "Olá, mundo!"
