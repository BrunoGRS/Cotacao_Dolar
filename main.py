import requests
import json
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Material1')

layout = ([sg.Text('Cotação do Dólar para Real', font='Bahnschrift')],
          [sg.Column(layout=[[sg.Button('Mostrar Cotação', font='Bahnschrift')]], justification='center')],
          [sg.Column(layout=[[sg.Text('', key='cotacao', font='Bahnschrift')]], justification='center')])

#Janela
janela = sg.Window('Conversor', layout)

#eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == "Mostrar Cotação":
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"

        site = requests.get(url)

        dicCot = json.loads(site.content)

        cotacao = 'R$ '+ dicCot['USDBRL']['bid']

        janela['cotacao'].update(cotacao)