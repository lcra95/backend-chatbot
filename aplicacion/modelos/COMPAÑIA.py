# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


from aplicacion.db import db



class COMPAÑIA(db.Model):
    __tablename__ = 'COMPA\xd1IA'

    IdCOMPAÑIA = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(30))
    Direccion = db.Column(db.String(45))
    Telefono = db.Column(db.String(25))
    #CRUD

    @classmethod
    def get_data(cls, _id):
        query =  cls.query.filter_by(IdCOMPAÑIA=_id).first()
        return  query

    @classmethod
    def insert_data(cls, dataJson):
        query = COMPAÑIA( 
            IdCOMPAÑIA = dataJson['IdCOMPAÑIA'],
            Nombre = dataJson['Nombre'],
            Direccion = dataJson['Direccion'],
            Telefono = dataJson['Telefono'],
            )
        COMPAÑIA.guardar(query)
        if query.id:                            
            return  {'response': {'data': {'last_id': query.id} }} 
        return  None

    @classmethod
    def update_data(cls, _id, dataJson):
        query = cls.query.filter_by(id=_id).first()
        if query:
            if 'IdCOMPAÑIA' in dataJson:
                query.IdCOMPAÑIA = dataJson['IdCOMPAÑIA']
            if 'Nombre' in dataJson:
                query.Nombre = dataJson['Nombre']
            if 'Direccion' in dataJson:
                query.Direccion = dataJson['Direccion']
            if 'Telefono' in dataJson:
                query.Telefono = dataJson['Telefono']
            db.session.commit()
            if query.id:                            
                return query.id
        return  None

    @classmethod
    def delete_data(cls, _id):
        query = cls.query.filter_by(id=_id).first()
        if query:
            COMPAÑIA.eliminar(query)
            if query.id:                            
                return query.id
        return  None

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

