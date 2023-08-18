# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


from aplicacion.db import db



class CONTACTO(db.Model):
    __tablename__ = 'CONTACTOS'

    IdCONTACTOS = db.Column(db.Integer, primary_key=True)
    IdPersona = db.Column(db.ForeignKey('PERSONA.idPersona'), index=True)
    Telefono1 = db.Column(db.String(25))
    Telefono2 = db.Column(db.String(25))

    #CRUD

    @classmethod
    def get_data(cls, _id):
        query =  cls.query.filter_by(IdCONTACTOS=_id).first()
        return  query

    @classmethod
    def insert_data(cls, dataJson):
        query = CONTACTO( 
            IdCONTACTOS = dataJson['IdCONTACTOS'],
            IdPersona = dataJson['IdPersona'],
            Telefono1 = dataJson['Telefono1'],
            Telefono2 = dataJson['Telefono2'],
            PERSONA = dataJson['PERSONA'],
            )
        CONTACTO.guardar(query)
        if query.id:                            
            return  {'response': {'data': {'last_id': query.id} }} 
        return  None

    @classmethod
    def update_data(cls, _id, dataJson):
        query = cls.query.filter_by(id=_id).first()
        if query:
            if 'IdCONTACTOS' in dataJson:
                query.IdCONTACTOS = dataJson['IdCONTACTOS']
            if 'IdPersona' in dataJson:
                query.IdPersona = dataJson['IdPersona']
            if 'Telefono1' in dataJson:
                query.Telefono1 = dataJson['Telefono1']
            if 'Telefono2' in dataJson:
                query.Telefono2 = dataJson['Telefono2']
            if 'PERSONA' in dataJson:
                query.PERSONA = dataJson['PERSONA']
            db.session.commit()
            if query.id:                            
                return query.id
        return  None

    @classmethod
    def delete_data(cls, _id):
        query = cls.query.filter_by(id=_id).first()
        if query:
            CONTACTO.eliminar(query)
            if query.id:                            
                return query.id
        return  None

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

