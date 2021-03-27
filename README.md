## chatbotHAL
Prototipo de un ChatBOT de encuestas con Telegram y Django para HAL

Esta API se desarrolló, se probó, se documento y se publicó principalmente con los siguientes lenguajes y herramientas (algunas otras se especifican en el archivo requirements.txt):

- Python-3.9.2
- Heroku
- psycopg2
- django-heroku

## Demo
[Link a la versión en Heroku](https://bit.ly/3swDZuJ)

Interactua con el bot 🤖 en Telegram buscalo como @halpollbot



### Getting Started
Para implementar de manera local la aplicación, crear y configurar tu bot sigue los siguientes pasos:

### Setupy 

    # Clona el repositorio con la siguiente URL
    $ git clone https://github.com/lnetza/chatbotHAL.git
  
    # entra a la carpeta chatbotHAL/botHAL
    $ cd chatbotHAL/botHAL
            
### Instalación

Si ya te encuentras dentro de la carptea `chatbotHAL\botHAL` crea un entorno virtual,  
para ello es necesario instalar `virtualenv` con el siguiente comando: `pip install virtualenv` si ya tienes  
instalado virtualenv ya no es necesario instalarlo.

Dentro de la carpeta `chatbotHAL\botHAL` crea un nuevo entorno virtual ejecutando: `python -m venv env`  

Una vez creado el entorno; procede a activarlo ingresando a la carpeta `chatbotHAL\botHAL\env\Scripts`  
y ejecuta el comando: `$ activate`  

Ahora regresa a la carpeta `chatbotHAL/botHAL` para instalar las dependencias necesarias descriptas en  
`requirements.txt`, ejecutando: `$ pip install -r requirements.txt`

### Base de datos
Crea la base de datos en PosgreSQL y especifica tus datos de acceso (usuario, contraseña y puerto) en el archivo ` settings.py` 

#### Migraciones
Realiza la migraciòn (verifica que te encuentres en la carpeta: `chatbotHAL\botHAL`) con el comando :
`$ python manage.py makemigrations`
`$ python manage.py migrate`  
Con los comandos anteriores se craròn las tablas que provee Django, si no se creo la tabla `Encuestas` del archivo `models.py` 
ejecuta: `$ python manage.py migrate app`

### Configuraciones de Telegram
Crea un nuevo bot en Telegram invocando a @BotFather con el comando `/newbot` y especifica la informaciòn que te va solicitando  
@BotFather como el nombre del CHAT y el nombre del BOT, finalmente se genera un TOKEN que vamos a requerir para vincular nuestra aplicaciòn con telegram.  

#### Variables de entorno
Cuando instalamos requirements.txt se instalo python-dotenv, ahora es necesario crear un archivo `.env` en `chatbotHAL\app`;  
dentro de `.env` crea la variable `TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'` especificando el TOKEN que te proporciono @BotFather  
https://api.telegram.org/bot"tutoken xxxxxxxxx"/getUpdates con esta URL obtenemos todos los mensajes de nuestro bot  


### Información de Uso
#### Ngrock
Ejecuta ngrock, (verifica que te encuentres en la carpeta `\botHAL\botHAL`) con el siguiente comando: `ngrok.exe http 8000`  
ngrock te va dar 2 urls, una con http y otra con https, vamos a ocupar la 2ª para enlazar nuestro bot desde el navegador de la siguiente forma:  
  `https://api.telegram.org/bot+TOKEN+/setWebhook?url=+URLNGROCK+URLDJANGOVISTABOT`  
    Ejemplo: `https://api.telegram.org/bot123456789012345678/setWebhook?url=https://d588e7f0149a.ngrok.io/webhooks/bot/`  
Si se ejecuto bien la peticiòn en el navegador, se visualizara los siguiente: `{"ok":true,"result":true,"description":"Webhook was set"}`  
la vigencia de la url que nos proporciona ngrock es de aproximadamente 2 horas, por lo que si queremos seguir haciendo pruebas es necesario  
volver a ejecutar `ngrok.exe http 8000` para que nos proporcione una nueva URL, cuando se enlaza nuestra aplicaciòn local con la url de ngrock  
no es posible obtener la data con `/getUpdates` debido a que el webHook se encuenta activo por lo tanto se visualiza lo siguiente: `{"ok":false,"error_code":409,"description":"Conflict: can't use getUpdates method while webhook is active; use deleteWebhook to delete the webhook first"}`  
para eliminarlo y poder volver a realizar una peticiòn a `/getUpdates`: `https://api.telegram.org/bot"tutoken xxxxxxxxx"/getUpdates` o bien para  
 enlazar una nueva URL generada por ngrock, se elimina con: `https://api.telegram.org/bot"tutoken xxxxxxxxx"/setWebHook?url=`  

Si ya se esta ejecutando ngrock, levanta el servidor local con: `$ python manage.py runserver`
Interactua con tu bot 🤖 buscandolo con el nombre que le asignaste, e ingresa a la siguiente URL para visualizar  
la informaciòn que llega desde el bot: http://127.0.0.1:8000  



