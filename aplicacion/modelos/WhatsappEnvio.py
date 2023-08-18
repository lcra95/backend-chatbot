from sqlalchemy import Column, Integer, Text, DateTime, func
from flask_sqlalchemy import SQLAlchemy
from aplicacion.db import db

class WhatsappEnviado(db.Model):
    __tablename__ = 'whatsaap_enviado'
    __table_args__ = {'schema': 'chat_bot'}
    
    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Text, nullable=False)
    id_mensaje = db.Column(db.Text, nullable=False)
    mensaje = db.Column(db.Text)
    from_ = db.Column(db.String(100), nullable=False)  # Usando "from_" porque "from" es una palabra reservada en Python
    to = db.Column(db.String(100), nullable=False)
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
            to=dataJson['to'],
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
                query.to = dataJson['to']
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