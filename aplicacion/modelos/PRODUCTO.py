# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


from aplicacion.db import db



class PRODUCTO(db.Model):
    __tablename__ = 'PRODUCTO'

    idPRODUCTO = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(20))
    IdCliente = db.Column(db.Integer)
    Descripcion = db.Column(db.String(45))
    Activo = db.Column(db.Integer)
    #CRUD

    @classmethod
    def get_data(cls, _id):
        query =  cls.query.filter_by(idPRODUCTO=_id).first()
        return  query

    @classmethod
    def insert_data(cls, dataJson):
        query = PRODUCTO( 
            idPRODUCTO = dataJson['idPRODUCTO'],
            Nombre = dataJson['Nombre'],
            IdCliente = dataJson['IdCliente'],
            Descripcion = dataJson['Descripcion'],
            Activo = dataJson['Activo'],
            )
        PRODUCTO.guardar(query)
        if query.id:                            
            return  {'response': {'data': {'last_id': query.id} }} 
        return  None

    @classmethod
    def update_data(cls, _id, dataJson):
        query = cls.query.filter_by(id=_id).first()
        if query:
            if 'idPRODUCTO' in dataJson:
                query.idPRODUCTO = dataJson['idPRODUCTO']
            if 'Nombre' in dataJson:
                query.Nombre = dataJson['Nombre']
            if 'IdCliente' in dataJson:
                query.IdCliente = dataJson['IdCliente']
            if 'Descripcion' in dataJson:
                query.Descripcion = dataJson['Descripcion']
            if 'Activo' in dataJson:
                query.Activo = dataJson['Activo']
            db.session.commit()
            if query.id:                            
                return query.id
        return  None

    @classmethod
    def delete_data(cls, _id):
        query = cls.query.filter_by(id=_id).first()
        if query:
            PRODUCTO.eliminar(query)
            if query.id:                            
                return query.id
        return  None

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

