# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


from aplicacion.db import db



class PERSONA(db.Model):
    __tablename__ = 'PERSONA'

    idPersona = db.Column(db.Integer, primary_key=True)
    Identificacion = db.Column(db.Integer)
    Nombre1 = db.Column(db.String(45))
    Nombre2 = db.Column(db.String(20))
    Apellido1 = db.Column(db.String(20))
    Apellido2 = db.Column(db.String(20))
    Nacionalidad = db.Column(db.String(20))
    CRM = db.Column(db.Integer)
    Activo = db.Column(db.Integer)
    IdPais = db.Column(db.ForeignKey('PAIS.idPAIS'), index=True)

    #CRUD

    @classmethod
    def get_data(cls, _id):
        output = {}
        sql =" SELECT * FROM PERSONA WHERE idPersona = " + str(_id)
        query = db.session.execute(sql)
        print(query)
        if query:
            for data in query:
                
                output["Identificacion"] = data["Identificacion"]
                output["Nombre1"] = data["Nombre1"]

        print(output)
        return  output

    @classmethod
    def insert_data(cls, dataJson):
        query = PERSONA( 
            idPersona = dataJson['idPersona'],
            Identificacion = dataJson['Identificacion'],
            Nombre1 = dataJson['Nombre1'],
            Nombre2 = dataJson['Nombre2'],
            Apellido1 = dataJson['Apellido1'],
            Apellido2 = dataJson['Apellido2'],
            Nacionalidad = dataJson['Nacionalidad'],
            CRM = dataJson['CRM'],
            Activo = dataJson['Activo'],
            IdPais = dataJson['IdPais'],
            PAI = dataJson['PAI'],
            )
        PERSONA.guardar(query)
        if query.id:                            
            return  {'response': {'data': {'last_id': query.id} }} 
        return  None

    @classmethod
    def update_data(cls, _id, dataJson):
        query = cls.query.filter_by(id=_id).first()
        if query:
            if 'idPersona' in dataJson:
                query.idPersona = dataJson['idPersona']
            if 'Identificacion' in dataJson:
                query.Identificacion = dataJson['Identificacion']
            if 'Nombre1' in dataJson:
                query.Nombre1 = dataJson['Nombre1']
            if 'Nombre2' in dataJson:
                query.Nombre2 = dataJson['Nombre2']
            if 'Apellido1' in dataJson:
                query.Apellido1 = dataJson['Apellido1']
            if 'Apellido2' in dataJson:
                query.Apellido2 = dataJson['Apellido2']
            if 'Nacionalidad' in dataJson:
                query.Nacionalidad = dataJson['Nacionalidad']
            if 'CRM' in dataJson:
                query.CRM = dataJson['CRM']
            if 'Activo' in dataJson:
                query.Activo = dataJson['Activo']
            if 'IdPais' in dataJson:
                query.IdPais = dataJson['IdPais']
            if 'PAI' in dataJson:
                query.PAI = dataJson['PAI']
            db.session.commit()
            if query.id:                            
                return query.id
        return  None

    @classmethod
    def delete_data(cls, _id):
        query = cls.query.filter_by(id=_id).first()
        if query:
            PERSONA.eliminar(query)
            if query.id:                            
                return query.id
        return  None

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

