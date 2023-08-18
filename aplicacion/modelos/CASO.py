# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from aplicacion.db import db



class CASO(db.Model):
    __tablename__ = 'CASO'

    idCASO = db.Column(db.Integer, primary_key=True)
    Descripcion = db.Column(db.String(200))
    Fecha = db.Column(db.DateTime)
    IdEstado = db.Column(db.ForeignKey('ESTADO.IdESTADO'), index=True)
    Opcion = db.Column(db.String(20))
    IdUsuario = db.Column(db.Integer)
    IdPersona = db.Column(db.Integer)
    IdModulo = db.Column(db.ForeignKey('MODULO.idMODULO'), index=True)
    Activo = db.Column(db.Integer)
    IdTipo = db.Column(db.ForeignKey('TIPO_CASO.IdTIPO_CASO'), index=True)
    IdLog = db.Column(db.ForeignKey('LOG.IdLOG'), index=True)
    URL_JIRA = db.Column(db.Integer)

    #CRUD

    @classmethod
    def get_data(cls, _id):
        query =  cls.query.filter_by(idCASO=_id).first()
        return  query

    @classmethod
    def insert_data(cls, dataJson):
        query = CASO( 
            idCASO = dataJson['idCASO'],
            Descripcion = dataJson['Descripcion'],
            Fecha = dataJson['Fecha'],
            IdEstado = dataJson['IdEstado'],
            Opcion = dataJson['Opcion'],
            IdUsuario = dataJson['IdUsuario'],
            IdPersona = dataJson['IdPersona'],
            IdModulo = dataJson['IdModulo'],
            Activo = dataJson['Activo'],
            IdTipo = dataJson['IdTipo'],
            IdLog = dataJson['IdLog'],
            URL_JIRA = dataJson['URL_JIRA'],
            ESTADO = dataJson['ESTADO'],
            LOG = dataJson['LOG'],
            MODULO = dataJson['MODULO'],
            TIPO_CASO = dataJson['TIPO_CASO'],
            )
        CASO.guardar(query)
        if query.id:                            
            return  {'response': {'data': {'last_id': query.id} }} 
        return  None

    @classmethod
    def update_data(cls, _id, dataJson):
        query = cls.query.filter_by(id=_id).first()
        if query:
            if 'idCASO' in dataJson:
                query.idCASO = dataJson['idCASO']
            if 'Descripcion' in dataJson:
                query.Descripcion = dataJson['Descripcion']
            if 'Fecha' in dataJson:
                query.Fecha = dataJson['Fecha']
            if 'IdEstado' in dataJson:
                query.IdEstado = dataJson['IdEstado']
            if 'Opcion' in dataJson:
                query.Opcion = dataJson['Opcion']
            if 'IdUsuario' in dataJson:
                query.IdUsuario = dataJson['IdUsuario']
            if 'IdPersona' in dataJson:
                query.IdPersona = dataJson['IdPersona']
            if 'IdModulo' in dataJson:
                query.IdModulo = dataJson['IdModulo']
            if 'Activo' in dataJson:
                query.Activo = dataJson['Activo']
            if 'IdTipo' in dataJson:
                query.IdTipo = dataJson['IdTipo']
            if 'IdLog' in dataJson:
                query.IdLog = dataJson['IdLog']
            if 'URL_JIRA' in dataJson:
                query.URL_JIRA = dataJson['URL_JIRA']
            if 'ESTADO' in dataJson:
                query.ESTADO = dataJson['ESTADO']
            if 'LOG' in dataJson:
                query.LOG = dataJson['LOG']
            if 'MODULO' in dataJson:
                query.MODULO = dataJson['MODULO']
            if 'TIPO_CASO' in dataJson:
                query.TIPO_CASO = dataJson['TIPO_CASO']
            db.session.commit()
            if query.id:                            
                return query.id
        return  None

    @classmethod
    def delete_data(cls, _id):
        query = cls.query.filter_by(id=_id).first()
        if query:
            CASO.eliminar(query)
            if query.id:                            
                return query.id
        return  None

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

