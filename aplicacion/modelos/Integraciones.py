from sqlalchemy import Column, Integer, String, Text, DateTime, func
from flask_sqlalchemy import SQLAlchemy
from aplicacion.db import db
from aplicacion.helpers.utilidades import Utilidades
class Integracion(db.Model):
    __tablename__ = 'integraciones'
    __table_args__ = {'schema': 'chat_bot'}

    id = db.Column(db.Integer, primary_key=True)
    api_key = db.Column(db.Text)
    id_cliente = db.Column(db.Text)
    authorization = db.Column(db.Text)
    enviroment = db.Column(db.String(10), nullable=False, comment="testing produccion")
    url_base = db.Column(db.Text)
    nombre_integracion = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())

    @classmethod
    def get_data(cls, integracion_name, env):
        query = cls.query.filter_by(nombre_integracion = integracion_name, enviroment = env).first()
        return Utilidades.obtener_datos(query)

    @classmethod
    def insert_data(cls, dataJson):
        query = Integracion(
            api_key=dataJson['api_key'],
            id_cliente=dataJson['id_cliente'],
            authorization=dataJson['authorization'],
            enviroment=dataJson['enviroment'],
            url_base=dataJson['url_base'],
            nombre_integracion=dataJson['nombre_integracion']
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
            if 'api_key' in dataJson:
                query.api_key = dataJson['api_key']
            if 'id_cliente' in dataJson:
                query.id_cliente = dataJson['id_cliente']
            if 'authorization' in dataJson:
                query.authorization = dataJson['authorization']
            if 'enviroment' in dataJson:
                query.enviroment = dataJson['enviroment']
            if 'url_base' in dataJson:
                query.url_base = dataJson['url_base']
            if 'nombre_integracion' in dataJson:
                query.nombre_integracion = dataJson['nombre_integracion']
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
