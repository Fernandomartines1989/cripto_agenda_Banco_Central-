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

mensagens = []


for compromisso in dados["conteudo"]:
    autoridade = compromisso.get("autoridade") 
    descricao = compromisso.get("descricao")
    if not descricao:
      continue
    html = BeautifulSoup(compromisso.get("descricao"))
    descricao = html.text 
    printado = False
    for word in ['btc', 'cripto', "bitcoin", "criptomoeda", "real digital", "CBDC", "ethereum", "mercado bitcoin", "binance", "bitso", "blockchain", "real tokenizado", "cripto"]:
        if not printado and word.lower() in compromisso['descricao'].lower():
          mensagens.append(f"A autoridade {autoridade} tem um compromisso de autoridade do BC no setor cripto hoje: {descricao}")
          mensagem_adicionada = True
          printado = True

nova_mensagem_2 = '\n'.join(mensagens)

TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY_2"]
TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID_2"]

app = Flask(__name__)


@app.route("/")
def hello_world():
   return "Olá, mundo!"

@app.route("/telegram-bot", methods=["POST"])
def telegram_bot():
  hoje = datetime.now().strftime("%d-%m-%Y")
  update = request.json
  chat_id = update["message"]["chat"]["id"]
  message = update["message"]["text"]
  nova_mensagem = {"chat_id": chat_id, "text": nova_mensagem_2}
  mensagem_if = {"chat_id": chat_id, "text": f"Olá! Seja bem-vindo (a). Quer saber se alguma autoridade do Banco Central tem algum evento de criptomoedas em sua agenda em {hoje}? Digite Sim" }
  mensagem_else = {"chat_id": chat_id, "text": "Não entendi Digite /start e eu te digo o que sei fazer" }
  if message == "/start":
    texto_resposta = requests.post(f"https://api.telegram.org./bot{TELEGRAM_API_KEY}/sendMessage", data=mensagem_if)
  elif message.lower() == "sim":
    texto_resposta = requests.post(f"https://api.telegram.org./bot{TELEGRAM_API_KEY}/sendMessage", data=nova_mensagem)
  else:
    texto_resposta = requests.post(f"https://api.telegram.org./bot{TELEGRAM_API_KEY}/sendMessage", data=mensagem_else)
  return "ok"
