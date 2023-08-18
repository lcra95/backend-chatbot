#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Se establece enviroment como argumento importado
from aplicacion.enviroment import env
enviroment = env



import sys,os,click,json
import requests
import time
from time import ctime
import datetime
import threading
import base64
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from flask_mail import Mail
from ftplib import FTP
# from flask_analytics import Analytics

from aplicacion.config import app_config
from aplicacion.db import db
from aplicacion.redis import redis
from aplicacion.helpers.Twilio import Twilio

# IMPORTACIÓN DE RECURSOS
from aplicacion.recursos.Mensajeria import MensajeriaResource,MensajeriaRecibirResource

#Inicializacion de flask
app = Flask(__name__)

#habilitacion de CORS
CORS(app)

#Inicializacion de datos de BD
db.init_app(app)

#Se setean variables de configuracion segun ambiente(env)
print("### AMBIENTE: " + enviroment + "###")
app.config.from_object(app_config[enviroment])
redis.init_app(app)

#Inicializacion de servicios api
api = Api(app)

# SE DEFINEN LOS ENDPOINTS Y LA CLASE QUE SE ENCARGARÁ DE PROCESAR CADA SOLICITUD
api.add_resource(MensajeriaResource, '/whatsapp/enviar')
api.add_resource(MensajeriaRecibirResource, '/whatsapp/recibir')

#ROUTES
@app.route('/')
def index():
    return "Hola =)", 200

#INICIAMOS LA APLICACIÓN
app.run(host='0.0.0.0', port=9090, debug=True )
    
        
