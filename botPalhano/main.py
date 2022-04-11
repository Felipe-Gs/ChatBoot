import telebot
from dotenv import load_dotenv
import os

#---------------------------------- CONFIG ----------------------------------
load_dotenv('./.env.local')
token = os.environ['TOKEN']

bot = telebot.TeleBot(token)
types = telebot.types

#---------------------------------- TEXTOS ----------------------------------
palhano = """
	Sobre a cidade: 
		Fundação: 08/05/1958
		Emancipação Política: 8 DE MAIO
		Gentílico: PALHANENSE
		Unidade Federatíva: BRASIL
		Mesoregião: VALE DO JAGUARIBE
		Distância para a capital: 127,00
		População estimada: 9348
		Clima: TROPICAL QUENTE SEMI-ÁRIDO BRANDO/TROPICAL QUENTE SEMI-ÁRIDO
		Fuso Horário: Hora de Brasília
	História do nome da cidade: 
			Há uma grande duvida sobre a origem do nome Palhano que vem do antigo nome Cruz do Palhano, pode ser uma homenagem ao riacho (Riacho da Cruz) e ao sobrenome do primeiro morador (Tenente-Coronel Estêvão de Souza Palhano) ou pelo mito popular de José Palhano e o Cruzeiro por ele encravado e bento pelo Frei Davi, numa de suas missões no ano 1901. Muitos atribuem o nome do município à palha oriunda da carnaubeira, vegetal de existência abundante na região. Outros que apontam a passagem da família Palhano pela região como a causa da nomenclatura.
"""

hospitais = [
	"""
		Hospital e Maternidade Maria Tereza de Jesus Mateus
 		🧭 Endereço: R. Possidônio Barreto, 615
		📞 Telefone: +55 88 34151040 
		🕥 Disponibilidade: Aberto 24h 
	""",
	"""
		Maria de Jesus Ribeiro Paz
 		🧭 Endereço: R. Oitero
		📞 Telefone: +55 88 34151040 
		🕥 Disponibilidade: Aberto 24h 
	"""
]

prefeitura="""
    PREFEITURA MUNICIPAL DE PALHANO.
    ✉️ E-mail: sec.cultura@palhano.ce.gov.br
    📞 Telefone Público: (88) 3415-1050 
    🧭 Endereço: Avenida Possidônio Barreto, 330 , Centro, 62910-000, Palhano, CE
    CEP: 62910-000
    Logradouro: Avenida Possidônio Barreto
    Número: 330
    Bairro: Centro
    Município: Palhano
    Estado: CE
"""

estabelecimentos = [
	[
		"""
			Lollipop pizzaria
			📍Palhano-CE
			⏱Funcionamos: Quarta á Segunda
							 17h ás 22hs
			📞 (88) 99461-0333
			Instagram @lollipoppizzaria
		""",
		types.InlineKeyboardMarkup(row_width=1).add(
			types.InlineKeyboardButton("Instagram", url="https://www.instagram.com/lollipoppizzaria/"), 
			types.InlineKeyboardButton("Agende agora aqui", url="https://lollipoppizzaria.com.br")
		)
	],
	[
		"""
			TRAPITO AÇAÍ
			🌵 Palhano-CE
			🛵 Delivery 
			📲 WhatsApp 88993201949 
			Instagram @trapito.acai
			🗓 De quinta a terça feira 
			🕥 Semana até as 22:00h 
			🕥 Fds até as 22:30h 
		""",
		types.InlineKeyboardMarkup(row_width=1).add(
			types.InlineKeyboardButton("Instagram", url="https://www.instagram.com/trapito.acai/"), 
			types.InlineKeyboardButton("Peça já o seu açaí aqui", url="www.goomer.app/trapito-acai")
		)
	],
	[
		"""
			𝐌𝐢𝐥𝐤 𝐒𝐡𝐚𝐤𝐞 & +
			Não contem delivery
			🍦|Sorvetes expressos, Milk shake e +, você encontra aqui.
			🌵|Palhano/CE.
			📍|A maior e melhor variedade de sorvetes, nós oferecemos.
			❣️|Fale conosco ⤵️
			Instagram @sorveteriapalhano
		""",
		types.InlineKeyboardMarkup(row_width=1).add(
			types.InlineKeyboardButton("Instagram", url="https://www.instagram.com/sorveteriapalhano/")
		)
	]
]

#---------------------------------- BOTÃO PARA VOLTAR ----------------------------------
backMarkup = types.ReplyKeyboardMarkup(row_width=1)
backbtn = types.KeyboardButton("Voltar")

backMarkup.add(backbtn)

types.InlineKeyboardButton

#---------------------------------- CIDADE ----------------------------------
@bot.message_handler(func=lambda message: message.text=="A cidade \U0001F334")
def city(message):
	bot.send_message(message.chat.id, palhano, reply_markup=types.InlineKeyboardMarkup(row_width=1).add(
																types.InlineKeyboardButton("\U0001F50E Clique para maiores informações", url="https://www.ibge.gov.br/cidades-e-estados/ce/palhano.html")
															))
	bot.send_location(message.chat.id, -4.746113, -37.960603)

#---------------------------------- PONTOS TURISTICOS ----------------------------------
@bot.message_handler(func=lambda message: message.text == "Pontos turisticos \U0001F335")
def tourism(message):
	bot.send_message(message.chat.id, "Pontos turisticos")
	bot.send_location(message.chat.id, -4.7507019, -37.9702095)
	bot.send_message(message.chat.id, "Pedra do santo")

#---------------------------------- PREFEITURA ----------------------------------
@bot.message_handler(func=lambda message: message.text == "Prefeitura \U0001F3E2")
def prefecture(message):
	bot.send_message(message.chat.id, prefeitura, reply_markup=types.InlineKeyboardMarkup(row_width=2).add(
																	types.InlineKeyboardButton("Facebook", url="https://www.facebook.com/prefeituradepalhano/"), 
																	types.InlineKeyboardButton("Instagram", url="https://www.instagram.com/gmppalhano/"), 
																	types.InlineKeyboardButton("Site", url="https://www.palhano.ce.gov.br/")
																))
	bot.send_location(message.chat.id, -4.747570, -37.961995)

#---------------------------------- POSTOS DE SAÚDE ----------------------------------
@bot.message_handler(func=lambda message: message.text == "Postos de saúde \U0001F3E5")
def hospitals(message):
	bot.send_message(message.chat.id, "Postos de saúde")
	bot.send_location(message.chat.id, -4.743949, -37.957761)
	bot.send_message(message.chat.id, hospitais[0])
	bot.send_location(message.chat.id, -4.747259, -37.960439)
	bot.send_message(message.chat.id, hospitais[1])

#---------------------------------- HOSPEDAGENS ----------------------------------
@bot.message_handler(func=lambda message: message.text == "Hospendagens \U0001F3E8")
def hotels(message):
	bot.send_message(message.chat.id, "Hospedagens")
	bot.send_location(message.chat.id, -4.7486183, -37.9636996)
	bot.send_message(message.chat.id, "Pousada mãe rainha")
	bot.send_location(message.chat.id, -4.7465724, -37.9619324)
	bot.send_message(message.chat.id, "Pousada JF")

#---------------------------------- BARBEARIAS----------------------------------
@bot.message_handler(func=lambda message: message.text == "barbers")
def barbers(message):
	bot.send_message(message.chat.id, "Joab")
	bot.send_message(message.chat.id, "Eduardo")
	bot.send_message(message.chat.id, "Joelma")

#------------------------------------ Deliverys --------------------------------------------
@bot.message_handler(func=lambda message: message.text == "deliverys")
def deliverys(message):
	bot.send_message(message.chat.id, estabelecimentos[0][0],reply_markup=estabelecimentos[0][1])
	bot.send_message(message.chat.id, estabelecimentos[1][0],reply_markup=estabelecimentos[1][1])
	bot.send_message(message.chat.id, estabelecimentos[2][0],reply_markup=estabelecimentos[2][1])

#---------------------------------- MENU ESTABELECIMENTOS ----------------------------------

@bot.message_handler(func=lambda message: message.text == "Estabelecimentos \U0001F355")
def establishments(message):
	bot.send_message(message.chat.id, "Estabelecimentos em palhano, escolha uma das opções abaixo: ", reply_markup=types.InlineKeyboardMarkup(row_width=2).add(
		types.InlineKeyboardButton("Barbearias \U0001F334", callback_data="barbers"),
		types.InlineKeyboardButton("Deliverys \U0001F335", callback_data="barbers"),
		types.InlineKeyboardButton("Farmacias \U0001F3E2", callback_data="barbers"),
		types.InlineKeyboardButton("Padarias \U0001F3E5", callback_data="barbers"),
		types.InlineKeyboardButton("Construção \U0001F3E8", callback_data="barbers"),
	))

#---------------------------------- MENU GERAL ----------------------------------
@bot.message_handler(func=lambda message: True)
def menu(message):
	bot.send_message(message.chat.id, "Bem-vindo ao menu, escolha uma das opções abaixo: ", reply_markup=types.ReplyKeyboardMarkup(row_width=2).add(
		types.KeyboardButton(text="A cidade \U0001F334"),
		types.KeyboardButton(text="Pontos turisticos \U0001F335"),
		types.KeyboardButton(text="Prefeitura \U0001F3E2"),
		types.KeyboardButton(text="Postos de saúde \U0001F3E5"),
		types.KeyboardButton(text="Hospendagens \U0001F3E8"),
		types.KeyboardButton(text="Estabelecimentos \U0001F355")
	))

#----------------------------------------------------------------------------------------------
bot.polling()