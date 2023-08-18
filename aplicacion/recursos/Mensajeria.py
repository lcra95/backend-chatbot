import json
import sys,os
from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse
from aplicacion.helpers.Twilio import Twilio

class MensajeriaResource(Resource):
    def post(self):
        try:
            dataJson = request.get_json()
            Mensaje = Twilio.enviar_whatsapp()
            return Mensaje
        except Exception as e:
           exc_type, exc_obj, exc_tb = sys.exc_info()
           fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
           msj = 'Error: '+ str(exc_obj) + ' File: ' + fname +' linea: '+ str(exc_tb.tb_lineno)
           return {'estado':0,'mensaje': str(msj) }, 500
class MensajeriaRecibirResource(Resource):
    def post(self):
        try:
            dataJson = request.get_json()
            print("_----------------------------------_")
            print(dataJson)
            print("_----------------------------------_")
            return dataJson
        except Exception as e:
           exc_type, exc_obj, exc_tb = sys.exc_info()
           fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
           msj = 'Error: '+ str(exc_obj) + ' File: ' + fname +' linea: '+ str(exc_tb.tb_lineno)
           return {'estado':0,'mensaje': str(msj) }, 500