from aplicacion.modelos.Integraciones import Integracion
from aplicacion.enviroment import env
enviroment = env
import openai, time
class Openai():
    def chatGpt(prompt):
        from aplicacion.helpers.Twilio import TwilioClass
        integracion_data = Integracion.get_data('Openai_chatgpt', enviroment)
        openai.api_key = integracion_data[0]["api_key"]
        preguntas = list()
        respuestas_gpt = list()
        mensajes = list()

        contexto = "Eres Lucy la asistente virtual de RyP Cambios, la mejor casa de cambio de pesos chilenos a bs y la tasa actual es de 0.0360 bs por peso chileno, al recibir un mensaje debes presentarte e indicar cual es la tasa de cambio"
        mensajes.append({'role': 'system', 'content': contexto})
        # while True:
        pregunta_actual = prompt
        if pregunta_actual.lower() in ["chao", "listo", 'bye', 'salir', 'exit']:
            print("Chao")
            time.sleep(3)
            
        if pregunta_actual != '':
            mensajes.append({'role': 'user', 'content': pregunta_actual})
            respuestas = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=mensajes,
                    temperature = 0.7,
                    max_tokens = 200
                )
            respuesta_actual = respuestas['choices'][0]['message']['content']
            TwilioClass.enviar_whatsapp(None, respuesta_actual)
            return respuesta_actual
            # respuestas_gpt.append(respuesta_actual)
            # mensajes.append({'role': 'assistant', 'content': respuesta_actual})