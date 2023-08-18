# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


from aplicacion.db import db



class MODULO(db.Model):
    __tablename__ = 'MODULO'

    idMODULO = db.Column(db.Integer, primary_key=True)
    Descripcion = db.Column(db.String(30))
    IdProducto = db.Column(db.ForeignKey('PRODUCTO.idPRODUCTO'), index=True)
    Activo = db.Column(db.Integer)

    #CRUD

    @classmethod
    def get_data(cls, _id):
        query =  cls.query.filter_by(idMODULO=_id).first()
        return  query

    @classmethod
    def insert_data(cls, dataJson):
        query = MODULO( 
            idMODULO = dataJson['idMODULO'],
            Descripcion = dataJson['Descripcion'],
            IdProducto = dataJson['IdProducto'],
            Activo = dataJson['Activo'],
            PRODUCTO = dataJson['PRODUCTO'],
            )
        MODULO.guardar(query)
        if query.id:                            
            return  {'response': {'data': {'last_id': query.id} }} 
        return  None

    @classmethod
    def update_data(cls, _id, dataJson):
        query = cls.query.filter_by(id=_id).first()
        if query:
            if 'idMODULO' in dataJson:
                query.idMODULO = dataJson['idMODULO']
            if 'Descripcion' in dataJson:
                query.Descripcion = dataJson['Descripcion']
            if 'IdProducto' in dataJson:
                query.IdProducto = dataJson['IdProducto']
            if 'Activo' in dataJson:
                query.Activo = dataJson['Activo']
            if 'PRODUCTO' in dataJson:
                query.PRODUCTO = dataJson['PRODUCTO']
            db.session.commit()
            if query.id:                            
                return query.id
        return  None

    @classmethod
    def delete_data(cls, _id):
        query = cls.query.filter_by(id=_id).first()
        if query:
            MODULO.eliminar(query)
            if query.id:                            
                return query.id
        return  None

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

