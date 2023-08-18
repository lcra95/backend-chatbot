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


# IMPORTACIÓN DE RECURSOS
from aplicacion.recursos.CASO import CasoResource
from aplicacion.recursos.COMPAÑIA import CompañiaResource
from aplicacion.recursos.CONTACTO import ContactoResource
from aplicacion.recursos.ESTADO import EstadoResource
from aplicacion.recursos.LOG import LogResource
from aplicacion.recursos.MODULO import ModuloResource
from aplicacion.recursos.PAI import PaiResource
from aplicacion.recursos.PERFIL import PerfilResource
from aplicacion.recursos.PERSONA import PersonaResource
from aplicacion.recursos.PRODUCTO import ProductoResource
from aplicacion.recursos.TIPOCASO import TipocasoResource

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
api.add_resource(CasoResource, '/caso/<int:_id>')
api.add_resource(CompañiaResource, '/compañia/<int:_id>')
api.add_resource(ContactoResource, '/contacto/<int:_id>')
api.add_resource(EstadoResource, '/estado/<int:_id>')
api.add_resource(LogResource, '/log/<int:_id>')
api.add_resource(ModuloResource, '/modulo/<int:_id>')
api.add_resource(PaiResource, '/pai/<int:_id>')
api.add_resource(PerfilResource, '/perfil/<int:_id>')
api.add_resource(PersonaResource, '/persona')
api.add_resource(ProductoResource, '/producto/<int:_id>')
api.add_resource(TipocasoResource, '/tipocaso/<int:_id>')

#ROUTES
@app.route('/')
def index():
    return "Hola =)", 200

#INICIAMOS LA APLICACIÓN
app.run(host='0.0.0.0', port=5000, debug=True )
    
        
