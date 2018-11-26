#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 23:00:58 2018

@author: miguelf
"""

class Individuo:
    def __init__(self, identificador, estado):
        self._ide=identificador
        self._est=estado
    def estado(self):
        return self._est
    def identificador(self):
        return self._ide