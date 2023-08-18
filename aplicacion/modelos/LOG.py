# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


from aplicacion.db import db



class LOG(db.Model):
    __tablename__ = 'LOG'

    IdLOG = db.Column(db.Integer, primary_key=True)
    Descripcion = db.Column(db.String(45))
    IdCreador = db.Column(db.Integer)
    FechaCreacion = db.Column(db.DateTime)
    UsuarioModifica = db.Column(db.String(25))
    FechaModificacion = db.Column(db.DateTime)
    NombreTabla = db.Column(db.String(45))
    IdRegistroTabla = db.Column(db.Integer)
    #CRUD

    @classmethod
    def get_data(cls, _id):
        query =  cls.query.filter_by(IdLOG=_id).first()
        return  query

    @classmethod
    def insert_data(cls, dataJson):
        query = LOG( 
            IdLOG = dataJson['IdLOG'],
            Descripcion = dataJson['Descripcion'],
            IdCreador = dataJson['IdCreador'],
            FechaCreacion = dataJson['FechaCreacion'],
            UsuarioModifica = dataJson['UsuarioModifica'],
            FechaModificacion = dataJson['FechaModificacion'],
            NombreTabla = dataJson['NombreTabla'],
            IdRegistroTabla = dataJson['IdRegistroTabla'],
            )
        LOG.guardar(query)
        if query.id:                            
            return  {'response': {'data': {'last_id': query.id} }} 
        return  None

    @classmethod
    def update_data(cls, _id, dataJson):
        query = cls.query.filter_by(id=_id).first()
        if query:
            if 'IdLOG' in dataJson:
                query.IdLOG = dataJson['IdLOG']
            if 'Descripcion' in dataJson:
                query.Descripcion = dataJson['Descripcion']
            if 'IdCreador' in dataJson:
                query.IdCreador = dataJson['IdCreador']
            if 'FechaCreacion' in dataJson:
                query.FechaCreacion = dataJson['FechaCreacion']
            if 'UsuarioModifica' in dataJson:
                query.UsuarioModifica = dataJson['UsuarioModifica']
            if 'FechaModificacion' in dataJson:
                query.FechaModificacion = dataJson['FechaModificacion']
            if 'NombreTabla' in dataJson:
                query.NombreTabla = dataJson['NombreTabla']
            if 'IdRegistroTabla' in dataJson:
                query.IdRegistroTabla = dataJson['IdRegistroTabla']
            db.session.commit()
            if query.id:                            
                return query.id
        return  None

    @classmethod
    def delete_data(cls, _id):
        query = cls.query.filter_by(id=_id).first()
        if query:
            LOG.eliminar(query)
            if query.id:                            
                return query.id
        return  None

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

