# cripto_agenda_Banco_Central-
Robô que checa se diariamente se alguma autoridade do Banco Central do Brasil tem agenda relacionada a criptomoedas
- Esse é um programa criado com linguagem Python
- Ele checa os eventos da "Agenda de Autoridades" do Banco Central daquele dia
- O código passa uma lista de termos que estão relacionados com o setor de criptomoedas
- A lista é: 'btc', 'cripto', "bitcoin", "criptomoeda", "real digital", "CBDC", "ethereum", "mercado bitcoin", "binance", "bitso", "blockchain", "real tokenizado", "cripto"]:
- Essa lista pode ser atualizada e novo itens podem ser adicionados
- O robô então checa se algum desses termos está na agenda de alguma das autoridades
- Se estiver, uma interação com o bot de Telegram @Cripto_Agenda_BC_bot irá entregar ao usuário o nome da autoridade e o evento
- Se não estiver presente nenhum dos termos na agenda do dia, a interação devolve para o usuário uma mensagem "Hoje nenhuma autoridade do Banco Central tem na agenda um evento envolvendo criptomoedas"
- O programa fica rodando em um servidor da empresa Render 
- 
