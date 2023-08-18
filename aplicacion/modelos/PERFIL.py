# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


from aplicacion.db import db



class PERFIL(db.Model):
    __tablename__ = 'PERFIL'

    IdPERFIL = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(20))
    #CRUD

    @classmethod
    def get_data(cls, _id):
        query =  cls.query.filter_by(IdPERFIL=_id).first()
        return  query

    @classmethod
    def insert_data(cls, dataJson):
        query = PERFIL( 
            IdPERFIL = dataJson['IdPERFIL'],
            Nombre = dataJson['Nombre'],
            )
        PERFIL.guardar(query)
        if query.id:                            
            return  {'response': {'data': {'last_id': query.id} }} 
        return  None

    @classmethod
    def update_data(cls, _id, dataJson):
        query = cls.query.filter_by(id=_id).first()
        if query:
            if 'IdPERFIL' in dataJson:
                query.IdPERFIL = dataJson['IdPERFIL']
            if 'Nombre' in dataJson:
                query.Nombre = dataJson['Nombre']
            db.session.commit()
            if query.id:                            
                return query.id
        return  None

    @classmethod
    def delete_data(cls, _id):
        query = cls.query.filter_by(id=_id).first()
        if query:
            PERFIL.eliminar(query)
            if query.id:                            
                return query.id
        return  None

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

