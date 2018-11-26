#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:16:27 2018

@author: miguelf
"""

class CAP:
    def __init__(self):
        self._cad = []

    def adicionar(self, evento):
        return [evento1 for evento1 in self._cad if evento.tempo()<evento.tempo()]+[evento]+\
           [evento1 for evento1 in self._cad if evento.tempo()>evento.tempo()]
    
    def remover(self):
        if len(self._cad)>0:
            return self._cad[1:]
        else:
            print("A função remover() encontrou um erro: A CAP está vazia.")
            
    def proximo(self):
        if len(self._cad)>0:
            return self._cad[0]
        else:
            print("A função proximo() encontrou um erro: A CAP está vazia.")
        
    def mostrar(self):
        for evento in self._cad:
            print(evento.tempo(), evento.tipo())   
    
