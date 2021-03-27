"""
Definition of views.
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

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )



TELEGRAM_URL = "https://api.telegram.org/bot"
TUTORIAL_BOT_TOKEN = os.getenv("TUTORIAL_BOT_TOKEN", "error_token")




class chatBotView(View):
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
        mercado9="¿Que tanto te gusto la pélicula de IT el PAYASO? "

        social1="¿En categoría de edad, te encuentras?"
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
        
        elif text == "NO" or text == "POCO":
            msg2 = "De momento no aplicas para nuestra encuesta de mercado \n Fin de la encusta\n"

            self.enviar_mensaje(msg2, chat)
            self.guardar_info(chat,nombre,usuario,mercado4,text)

        elif text == "SI" or text == "MUCHO":
           msg2 = "Teclea Coca para Coca-Cola 100\n Teclea L para Light\n"

           self.enviar_mensaje(mercado3, chat)
           self.enviar_mensaje(msg2, chat)
           self.guardar_info(chat,nombre,usuario,mercado4,text)
        
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
            msg2 = "Teclea x Probablemente si\n Tecle Z para Probablemente no\n Tecle B para Definitivamente no\n"
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
        data = {
            "text": message,
            "chat_id": chat_id,
        }
        response = requests.post(
            TELEGRAM_URL + "1626213109:AAEqqbqNaWbXXD2P4eaprwHP5xIPfowlifE/sendMessage?", data=data
        )
    
    @staticmethod
    def guardar_info(chat,nombre,usuario,pregunta,respuesta):
        
        encuesta = Encuestas()
        encuesta.id_chat    =chat
        encuesta.nombre     = nombre
        encuesta.usuario    = usuario
        encuesta.pregunta   = pregunta
        encuesta.respuesta  = respuesta
        encuesta.save()

def informacion_encuesta(request):
    lista=Encuestas.objects.all()

    ctx={'lista':lista}
    return render(request,'app/encuestas.html',ctx)
