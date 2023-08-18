# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


from aplicacion.db import db



class TIPOCASO(db.Model):
    __tablename__ = 'TIPO_CASO'

    IdTIPO_CASO = db.Column(db.Integer, primary_key=True)
    Descripcion = db.Column(db.String(20))
    #CRUD

    @classmethod
    def get_data(cls, _id):
        query =  cls.query.filter_by(IdTIPO_CASO=_id).first()
        return  query

    @classmethod
    def insert_data(cls, dataJson):
        query = TIPOCASO( 
            IdTIPO_CASO = dataJson['IdTIPO_CASO'],
            Descripcion = dataJson['Descripcion'],
            )
        TIPOCASO.guardar(query)
        if query.id:                            
            return  {'response': {'data': {'last_id': query.id} }} 
        return  None

    @classmethod
    def update_data(cls, _id, dataJson):
        query = cls.query.filter_by(id=_id).first()
        if query:
            if 'IdTIPO_CASO' in dataJson:
                query.IdTIPO_CASO = dataJson['IdTIPO_CASO']
            if 'Descripcion' in dataJson:
                query.Descripcion = dataJson['Descripcion']
            db.session.commit()
            if query.id:                            
                return query.id
        return  None

    @classmethod
    def delete_data(cls, _id):
        query = cls.query.filter_by(id=_id).first()
        if query:
            TIPOCASO.eliminar(query)
            if query.id:                            
                return query.id
        return  None

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

