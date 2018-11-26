#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:29:02 2018

@author: miguelf
"""

class Evento:
    def __init__(self,identificador, tipo, tempo):
        self._ide=identificador
        self._tip=tipo
        self._tem=tempo
        def tempo(self):
            return self._tem
        def tipo(self):
            return self._tip
        def identificador(self):
            return self._ide
        def mostra(self):
            print ('Identificador:', self._ide,'  ','Tipo:', self._tip,'  ','Tempo:', self._tem)