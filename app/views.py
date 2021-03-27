"""
Definiciòn de las vistas
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest


import json
import os

import requests
from django.http import JsonResponse
from django.views import View
from app.models import *

from dotenv import load_dotenv
load_dotenv()

TELEGRAM_URL = "https://api.telegram.org/bot"
BOT_TOKEN = os.getenv("TOKEN", "error_token")

def home(request):
    """Renderea a home."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renderea a about"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            
            'year':datetime.now().year,
        }
    )


class chatBotView(View):
    """Se definen las preguntas para encuestas de tipo mercado y encuestas de tipo social de manera estatica, se recolecta la
    informaciòn del boot por medio de json.loads() para posteriormente extraer los valores con object notation, se invoca al
    mètodo enviar_mensaje() para dar respuesta al usuario y guardar_info() para guardar en la base de datos"""

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        text = data["message"]["text"]
        chat = data["message"]["chat"]["id"]
        nombre = data["message"]["chat"]["first_name"]
        usuario = data["message"]["chat"]["username"]
        chat = str(chat)
        text = text.upper()
        
        general="✉︎ ¿Que encuesta quieres realizar?\n"
        mercado1="¿Cuántas veces fue a ver una película al cine en los últimos 6 meses?\n"
        mercado2="¿De estos generos de pélicula, cuál te gusta más? Terror - Aventura"
        mercado3="Compraste Coca-Cola Light o Coca-Cola 100?"
        mercado4="¿Te tocó algun cupon de descuento para tu pélicula? "
        mercado5="¿Compraste refresco Coca-Cola Zero?"
        mercado6="¿Que tan familiar se te hace la marca Doritos Sabritas?\n"
        mercado7="¿Que cupón de tiempo AIRE encontraste?"
        mercado8="¿De que compañia de telefonia era el cupón?"
        mercado9="¿Que tanto te gusto la pélicula de IT el PAYASO 🤡? "

        social1="¿En que categoría de edad, te encuentras?"
        social2="¿Cuál es tu clasificación en la universidad?"
        social3="Si tuviera que seguir otros estudios, ¿volverías a la universidad?"

        if text == "/START":
            msg1 = "☀ Teclea 'Mercado' para encuesta de Mercado \n Teclea 'Social' para encuesta Social"
            
            self.enviar_mensaje(general, chat)
            self.enviar_mensaje(msg1, chat)

        elif text == "/HELP":
            msg2 = "Para iniciar una encuesta teclea el comando /start"
            self.enviar_mensaje(msg2,chat)

        elif text == "MERCADO":
            msg2 = "Teclea 2 para 2 veces\n Teclea 4 para 4 veces"
            
            self.enviar_mensaje(mercado1, chat)
            self.enviar_mensaje(msg2, chat)
            self.guardar_info(chat,nombre,usuario,general,text)

        elif text == "2":
            msg2 = "Teclea Aventura para Aventura\n Teclea Terror para Terror\n"

            self.enviar_mensaje(mercado2, chat)
            self.enviar_mensaje(msg2, chat)
            self.guardar_info(chat,nombre,usuario,mercado1,text)
        
        elif text == "4":
            msg2 = "Teclea Si para Si\n Teclea No para No\n"

            self.enviar_mensaje(mercado5, chat)
            self.enviar_mensaje(msg2, chat)
            self.guardar_info(chat,nombre,usuario,mercado1,text)
        
        elif text == "AVENTURA":
            msg2 = "Si\n No\n"

            self.enviar_mensaje(mercado4, chat)
            self.enviar_mensaje(msg2, chat)
            self.guardar_info(chat,nombre,usuario,mercado2,text)
        
        elif text == "TERROR":
            msg2 = "Poco\n Mucho\n"
            self.enviar_mensaje(mercado9, chat)
            self.enviar_mensaje(msg2, chat)
            self.guardar_info(chat,nombre,usuario,mercado2,text)
        
        elif text == "POCO":
            msg2 = "De momento no aplicas para nuestra encuesta de mercado \n Fin de la encusta\n"

            self.enviar_mensaje(msg2, chat)
            self.guardar_info(chat,nombre,usuario,mercado9,text)
        
        elif text == "NO":
            msg2 = "De momento no aplicas para nuestra encuesta de mercado \n Fin de la encusta\n"

            self.enviar_mensaje(msg2, chat)
            self.guardar_info(chat,nombre,usuario,mercado6,text)
        
        elif text == "SI":
           msg2 = "Teclea Coca para Coca-Cola 100\n Teclea L para Light\n"

           self.enviar_mensaje(mercado3, chat)
           self.enviar_mensaje(msg2, chat)
           self.guardar_info(chat,nombre,usuario,mercado4,text)

        elif text == "MUCHO":
           msg2 = "Teclea Coca para Coca-Cola 100\n Teclea L para Light\n"

           self.enviar_mensaje(mercado3, chat)
           self.enviar_mensaje(msg2, chat)
           self.guardar_info(chat,nombre,usuario,mercado9,text)
        
        elif text == "COCA" or text == "L":
           msg2 = " Si la conoces desde hace tiempo teclea OK\n Si no la conces teclea No\n"

           self.enviar_mensaje(mercado6, chat)
           self.enviar_mensaje(msg2, chat)
           self.guardar_info(chat,nombre,usuario,mercado3,text)

        elif text == "OK":
           msg2 = "Teclea 20 para 20$\n Teclea 50 para 50$\n Teclea Ninguno para no encontre cupón\n"
           self.enviar_mensaje(mercado7, chat)
           self.enviar_mensaje(msg2, chat)
           self.guardar_info(chat,nombre,usuario,mercado6,text)
        
        elif text == "20" or text == "50":
           msg2 = "Teclea Telcel para Telcel\n Teclea Movistar para Movistar\n"
           
           self.enviar_mensaje(mercado8, chat)
           self.enviar_mensaje(msg2, chat)
           self.guardar_info(chat,nombre,usuario,mercado7,text)
        
        
        elif text == "NINGUNO":
           msg2 = "De momento no aplicas para la encuesta que estamos realizando\n"
           
           self.enviar_mensaje(msg2, chat)
           self.guardar_info(chat,nombre,usuario,mercado6,text)
        
        elif text == "TELCEL":
           msg1 = "Has finalizado la encuesta correctamente\n"
           msg2 = "COMPLETADO"
           
           self.enviar_mensaje(msg1, chat)
           self.guardar_info(chat,nombre,usuario,msg2,text)

        elif text == "MOVISTAR":
           msg1 = "Has finalizado la encuesta correctamente\n"
           msg2 = "COMPLETADO"

           self.enviar_mensaje(msg1, chat)
           self.guardar_info(chat,nombre,usuario,msg2,text)

        
        elif text == "SOCIAL":
            msg2 = "Teclea A para 18 años\n Teclea B para 18-26 años\n Teclea C para 26-34 años \n"
            
            self.enviar_mensaje(social1, chat)
            self.enviar_mensaje(msg2, chat)
            self.guardar_info(chat,nombre,usuario,general,text)
        
        elif text == "A" or text == "B":
            msg2 = "Teclea primero para Estudiante de primer año\n Teclea segundo para Estudiante de segundo año\n  Teclea Ultimo para Último año\n"
            self.enviar_mensaje(social2, chat)
            self.enviar_mensaje(msg2, chat)
            self.guardar_info(chat,nombre,usuario,social1,text)
        
        elif text == "PRIMERO" or text == "SEGUNDO":
            msg2 = "Teclea X Probablemente si\n Tecle Z para Probablemente no\n Teclea B para Definitivamente no\n"
            self.enviar_mensaje(social3, chat)
            self.enviar_mensaje(msg2, chat)
            self.guardar_info(chat,nombre,usuario,social2,text)
        
        elif text == "ULTIMO" or text == "C":
            msg2 = "De momento no aplicas para la encuesta que estamos realizando"
            self.enviar_mensaje(msg2,chat)
            self.guardar_info(chat,nombre,usuario,social2,text)
        
        elif text == "Z" or text == "X":
            msg2 = "Encuesta finalizada correctamente"
            self.enviar_mensaje(msg2,chat)
            self.guardar_info(chat,nombre,usuario,social3,text)

        else:

            msg2 = "No conozco ese comando, escibre el comando /help para ayuda"
            self.enviar_mensaje(msg2,chat)

        return JsonResponse({"ok": "request processed"})

    @staticmethod
    def enviar_mensaje(message, chat_id):
        """Recibe como parametros el mensaje como pregunta y el chat_id del chat, para hacer una peticiòn post al endpoint
        sendMessage especificando la url+tokeBot+data"""
        data = {
            "text": message,
            "chat_id": chat_id,
        }
        response = requests.post(
            TELEGRAM_URL + BOT_TOKEN + "/sendMessage?", data=data
        )
    
    @staticmethod
    def guardar_info(chat,nombre,usuario,pregunta,respuesta):
        """Recibe como parametros chat,nombre,usuario,pregunta,respuesta y se encarga de guardar esta informaciòn en la tabla encuestas"""
        encuesta = Encuestas()
        encuesta.id_chat    =chat
        encuesta.nombre     = nombre
        encuesta.usuario    = usuario
        encuesta.pregunta   = pregunta
        encuesta.respuesta  = respuesta
        encuesta.save()

def informacion_encuesta(request):
    """Se encarga de listar la informaciòn disponible en la tabla Encuestas y retornar la informaciòn a la plantilla encuestas.html"""
    lista=Encuestas.objects.all().order_by('id_chat')

    ctx={'lista':lista}
    return render(request,'app/encuestas.html',ctx)
