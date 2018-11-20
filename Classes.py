#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:46:02 2018

@author: miguelf
"""
        
import random

class individuo:
    def __init__(self, identificador, estado):
        self._ide=identificador
        self._est=estado
    def estado(self):
        return self._est
    def identificador(self):
        return self._ide
        
class grelha:
    def __init__(self, tamanho, obstaculos):
        self._obs=obstaculos
        self._n=tamanho
        
        self._cen=tamanho//2+1 #centro da grelha para trabalhar com coordenadas
        
        r=[]
        for i in range(2*n+1):
            a=[]
            for j in range(2*n+1):
                a+=[0]
            r+=[a]
        for i in obstaculos:
            self._gre[self._cen+i[0]][self._cen+i[1]]
        self._gre=r
            
        
    def identificador(self):
        return self._ide