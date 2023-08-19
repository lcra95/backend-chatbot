import sys,os
from sqlalchemy import Column, Integer, Text, DateTime, func
from flask_sqlalchemy import SQLAlchemy
from aplicacion.db import db

class WhatsappEnviado(db.Model):
    __tablename__ = 'mensajeria'
    __table_args__ = {'schema': 'chat_bot'}
    
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Text, nullable=False)
    id_mensaje = db.Column(db.Text, nullable=False)
    mensaje = db.Column(db.Text)
    from_ = db.Column(db.String(100), nullable=False)  # Usando "from_" porque "from" es una palabra reservada en Python
    to_ = db.Column(db.String(100), nullable=False)
    estado_envio = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())

    @classmethod
    def get_data(cls, _id):
        query = cls.query.filter_by(id=_id).first()
        return query

    @classmethod
    def insert_data(cls, dataJson):
        query = WhatsappEnviado(
            id_cliente=dataJson['id_cliente'],
            id_mensaje=dataJson['id_mensaje'],
            mensaje=dataJson['mensaje'],
            from_=dataJson['from'],
            to_=dataJson['to'],
            estado_envio=dataJson['estado_envio']
        )
        db.session.add(query)
        db.session.commit()
        if query.id:
            return {'response': {'data': {'last_id': query.id}}}
        return None

    @classmethod
    def update_data(cls, _id, dataJson):
        query = cls.query.filter_by(id=_id).first()
        if query:
            if 'id_cliente' in dataJson:
                query.id_cliente = dataJson['id_cliente']
            if 'id_mensaje' in dataJson:
                query.id_mensaje = dataJson['id_mensaje']
            if 'mensaje' in dataJson:
                query.mensaje = dataJson['mensaje']
            if 'from' in dataJson:
                query.from_ = dataJson['from']
            if 'to' in dataJson:
                query.to_ = dataJson['to']
            if 'estado_envio' in dataJson:
                query.estado_envio = dataJson['estado_envio']
            db.session.commit()
            return query.id
        return None

    @classmethod
    def delete_data(cls, _id):
        query = cls.query.filter_by(id=_id).first()
        if query:
            db.session.delete(query)
            db.session.commit()
            if query.id:
                return query.id
        return None
    @classmethod
    def buscar_historial(cls, to_):
        try:    
            sql_historial =  f"""
            SELECT 
                id, mensaje, estado_envio 
            FROM mensajeria 
            WHERE 
                from_ = '{to_}' or to_='{to_}'
                AND estado_envio in (1, 3)
            ORDER BY created_at ASC;
            """
            data = []
            contexto = """
                    Eres Lucy la asistente virtual de RyP Cambios, 
                    debes dar respuestas cortas y consisas, 
                    RyP Cambios realiza envios de dinero a Venezuela, Colombia y Peru,
                    La tasa actual para venezuela es 0,0360 bs por 1 peso  chileno,
                    La tasa actual para Colombia es 4 pesos colombianos por 1 peso chileno,
                    La tasa actual para Peru es 0.0040 soles por 1 peso chileno,
                    Cuando recibas el primer mensaje de la conversacion debes:
                    Presentarte, Indicar la tasa actual de cada pais, y preguntar al cliente a que pais desea enviar su dinero, debes preguntar la cantidad en pesos chilenos que desea enviar o la cantidad de dinero en la moneda del pais elegido.
                    cuando recibas el monto a enviar en cualquiera de las monedas, debes indicarle al cliente que debe realizar un deposito bancario a la cuenta 123 a nombre de luis requena, si el cliente dice que pagara en efectivo debes indicarle que se comunique con luis requena por el +56049980822
            """
            data.append({'role': 'system', 'content': contexto})
            query = db.session.execute(sql_historial)
            
            if query:
                transformed_data = []
                for x in query:
                    temp2 = {
                        "role" : "user" if x["estado_envio"] == 3 else "assistant",
                        "content" : x["mensaje"]
                    }

                    print(temp2)
                    data.append(temp2)
                return data
            return data
        except Exception as e:
           exc_type, exc_obj, exc_tb = sys.exc_info()
           fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
           msj = 'Error: '+ str(exc_obj) + ' File: ' + fname +' linea: '+ str(exc_tb.tb_lineno)
           print(f"----------------{msj}--------------------------")