import json
import sys,os
from twilio.rest import Client
from aplicacion.modelos.Integraciones import Integracion
from aplicacion.modelos.WhatsappEnvio import WhatsappEnviado
from aplicacion.helpers.Openai import Openai
from aplicacion.enviroment import env
enviroment = env
# Puedes especificar el ambiente al instanciar o dejar que tome el valor por defecto del entorno


class TwilioClass():
    def enviar_whatsapp(data=None, body= None):
        integracion_data = Integracion.get_data('Twilio_whatsapp', enviroment)
        account_sid = integracion_data[0]["id_cliente"]
        auth_token = integracion_data[0]["authorization"]
        client = Client(account_sid, auth_token)
        if body is None:
            body = "Hola Soy tu probando"
        # DEFAULT MENSAJE
        from_ = 'whatsapp:+17622244982',
        body = body,
        to = 'whatsapp:+56949980822'
        # DEFAULT MENSAJE

        if data is not None:
            from_ = f'whatsapp:{data["from"]}'
            body = data["body"]
            to = f'whatsapp:{data["to"]}'

        try:
        
            message = client.messages.create(
                from_=from_,
                body=body,
                to=to
            )
            whatsapp_enviado = {
                "id_cliente" : account_sid,
                "id_mensaje" : message.sid,
                "from" : from_,
                "to": to,
                "mensaje" : body,
                "estado_envio" : 1
            }
            WhatsappEnviado.insert_data(whatsapp_enviado)
            return {"estado": 1, "id_mensaje": message.sid}
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            msj = str(exc_obj)
            whatsapp_enviado = {
                "id_cliente" : account_sid,
                "id_mensaje" : msj,
                "from" : from_,
                "to": to,
                "mensaje" : body,
                "estado_envio" : 0
            }
            WhatsappEnviado.insert_data(whatsapp_enviado)
            return {'estado':0,'mensaje': str(msj) }, 500

    def recibir_whatsapp(data):
        try:
            whatsapp_enviado = {
                    "id_cliente" : data["AccountSid"],
                    "id_mensaje" : data["SmsSid"],
                    "from" : data["From"],
                    "to": data["To"],
                    "mensaje" : data["Body"],
                    "estado_envio" : 3,
                }
            WhatsappEnviado.insert_data(whatsapp_enviado)
            historial = WhatsappEnviado.buscar_historial(data["To"])
            print(historial)
            respuesta_actual = Openai.chatGpt(historial)
            return respuesta_actual    
        except Exception as e:
           exc_type, exc_obj, exc_tb = sys.exc_info()
           fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
           msj = 'Error: '+ str(exc_obj) + ' File: ' + fname +' linea: '+ str(exc_tb.tb_lineno)
           return  str(msj)