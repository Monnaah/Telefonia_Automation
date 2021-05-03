#Automatizar tarefa de preenchimento de fatura, dos clientes de telefonia.

# importar bibliotecas
import pyautogui
import time
import pyperclip

# Esperar um segundo e emitir alerta que o programa vai começar a rodar
pyautogui.PAUSE = 1
pyautogui.alert("Vai começar, aperte OK e não mexa em nada")
# Passo 1 - abrir chrome
time.sleep(2)
pyautogui.click(1017,1056)
time.sleep(2)
# Passo 2 - clicar no drive
pyautogui.click(81,19)
time.sleep(5)
# Passo 4- Entrar na pasta da Tecnogate
pyautogui.click(574,678,clicks=2)
# entrar na pasta financeiro 
time.sleep(2)
pyautogui.click(424,657,clicks=2)
# entrar na pasta faturas locação
time.sleep(2)
pyautogui.click(448,536,clicks=2)
#entrar na pasta 2021
time.sleep(2)
pyautogui.click(415,488,clicks=2)
# entrar na pasta maio (mudar posição todo mês, para o mês atual)
time.sleep(2)
pyautogui.click(407,546,clicks=2)
#entrar em faturas
time.sleep(2)
pyautogui.click(411,361,clicks=2)
# entrar no cliente JORNADA
time.sleep(5)
pyautogui.click(474,357,clicks=2)
time.sleep(8)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1410")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(1)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)

# entrar cliente ECAR
pyautogui.click(535,422, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1411")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)

# entrar cliente HARMONIA
pyautogui.click(525,477, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1413")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente FOURPLANES
pyautogui.click(545,540, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1413")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente 4MINDS
pyautogui.click(518,601, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1414")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente INTEEGRA
pyautogui.click(539,660, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1415")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente JALORETO
pyautogui.click(521,719, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1416")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente NUCLEO
pyautogui.click(542,778, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1417")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente MHC
pyautogui.click(525,837, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1418")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente TETRA
pyautogui.click(534,898, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1419")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente TRIOLET
pyautogui.click(528,956, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1420")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)

#descer a tela
pyautogui.scroll(-5,474,357)

# entrar cliente QUALES
pyautogui.click(526,399, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1421")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente THOR
pyautogui.click(522,459, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1422")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente PERELLO
pyautogui.click(545,523, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1423")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente VALDEREZ
pyautogui.click(542,580, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1424")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente CSL
pyautogui.click(531,642, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1425")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente JEREMIAS
pyautogui.click(529,696, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1426")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente WAY REGULADORA
pyautogui.click(536,763, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1427")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente BIO
pyautogui.click(523,820, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1428")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente LDS
pyautogui.click(519,881, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1429")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente AV SEGUROS
pyautogui.click(547,943, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1430")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)
# entrar cliente VERMARI
pyautogui.click(546,1001, clicks=2)
time.sleep(5)
# mudar número da fatura
pyautogui.click(816,690)
pyautogui.press("delete")
pyautogui.write("1431")
time.sleep(5)
# mudar data de emissão
pyautogui.click(184,691)
pyautogui.press("delete")
pyautogui.write("22/05/2021")
time.sleep(5)
# mudar data de vencimento
pyautogui.click(605,693)
pyautogui.press("delete")
pyautogui.write("30/05/2021")
pyautogui.click(946,625)
time.sleep(7)
# Fazer download
pyautogui.hotkey("ctrl", "p")
time.sleep(3)
pyautogui.click(1834,162)
time.sleep(5)
pyautogui.click(1423,897)
time.sleep(3)
pyautogui.click(791,667)

# fechar
time.sleep(2)
pyautogui.click(500,18)
time.sleep(2)

# Clicar no drive novamente
pyautogui.click(81,19)
time.sleep(2)






"""
# fazer o download DO PDF
pyautogui.click(204,520)
time.sleep(3)
# arquivo pdf
pyautogui.click(521,462)
time.sleep(8)
# exportar
pyautogui.click(1834,160)
"""
