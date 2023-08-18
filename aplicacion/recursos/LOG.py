#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse
from aplicacion.modelos.LOG import LOG

class LogResource(Resource):
    def get(self, _id):
        try:
            var_LOG = LOG.get_data(_id)
            if var_LOG:
                return var_LOG, 200
            return {'mensaje': 'No se encontró el recurso solicitado'}, 404
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            # exc_type, fname, exc_tb.tb_lineno
            msj = 'Error: '+ str(exc_obj) + ' File: ' + fname +' linea: '+ str(exc_tb.tb_lineno)
            return {'mensaje': str(msj) }, 500
