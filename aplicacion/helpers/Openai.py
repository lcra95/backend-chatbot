from aplicacion.modelos.Integraciones import Integracion
from aplicacion.enviroment import env
enviroment = env
import openai, time
class Openai():
    def chatGpt(prompt):
        from aplicacion.helpers.Twilio import TwilioClass
        integracion_data = Integracion.get_data('Openai_chatgpt', enviroment)
        openai.api_key = integracion_data[0]["api_key"]
       
        respuestas = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=prompt,
                temperature = 0.7,
                max_tokens = 100
            )
        respuesta_actual = respuestas['choices'][0]['message']['content']
        TwilioClass.enviar_whatsapp(None, respuesta_actual)
        return respuesta_actual
        # respuestas_gpt.append(respuesta_actual)
        # mensajes.append({'role': 'assistant', 'content': respuesta_actual})