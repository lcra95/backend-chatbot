# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


from aplicacion.db import db



class ESTADO(db.Model):
    __tablename__ = 'ESTADO'

    IdESTADO = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(25))
    #CRUD

    @classmethod
    def get_data(cls, _id):
        query =  cls.query.filter_by(IdESTADO=_id).first()
        return  query

    @classmethod
    def insert_data(cls, dataJson):
        query = ESTADO( 
            IdESTADO = dataJson['IdESTADO'],
            Nombre = dataJson['Nombre'],
            )
        ESTADO.guardar(query)
        if query.id:                            
            return  {'response': {'data': {'last_id': query.id} }} 
        return  None

    @classmethod
    def update_data(cls, _id, dataJson):
        query = cls.query.filter_by(id=_id).first()
        if query:
            if 'IdESTADO' in dataJson:
                query.IdESTADO = dataJson['IdESTADO']
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
            ESTADO.eliminar(query)
            if query.id:                            
                return query.id
        return  None

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

