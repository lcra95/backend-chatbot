#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse
from aplicacion.modelos.PERSONA import PERSONA

class PersonaResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('idPersona',
            type=int,
            required=True,
            help="Debe indicar id persona"
        )
        data = parser.parse_args()
        try:

            _id = data["idPersona"]
            var_PERSONA = PERSONA.get_data(_id)
            if var_PERSONA:
                return var_PERSONA, 200
            return {'mensaje': 'No se encontró el recurso solicitado'}, 404
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            # exc_type, fname, exc_tb.tb_lineno
            msj = 'Error: '+ str(exc_obj) + ' File: ' + fname +' linea: '+ str(exc_tb.tb_lineno)
            return {'mensaje': str(msj) }, 500
