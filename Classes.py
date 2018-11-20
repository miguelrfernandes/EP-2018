#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:46:02 2018

@author: miguelf
"""
        
import random

class Individuo:
    def __init__(self, identificador, estado):
        self._ide=identificador
        self._est=estado
    def estado(self):
        return self._est
    def identificador(self):
        return self._ide
        
class Grelha:   
    def __init__(self, n, obstaculos):
        self._obs=obstaculos
        self._lad=n*2+1 #lado da rede
        
        self._cen=self._lad//2 #centro da grelha (no python) para trabalhar com coordenadas
        
        r=[]
        for i in range(self._lad):
            a=[]
            for j in range(self._lad):
                a+=[None]
            r+=[a]
        for i in obstaculos:
            r[self._cen-i[1]][self._cen+i[0]]="obstaculo"
        self._gre=r
            
    def inserir(self, individuo, posicao):
        self._gre[self._cen-posicao[1]][self._cen+posicao[0]]=individuo
    
    def remover(self, posicao):
        self._gre[self._cen-posicao[1]][self._cen+posicao[0]]=None
        
    def encontrar(self, identificador):
        i=0
        while i<len(self._gre):
            j=0
            while j<len(self._gre):
                if self._gre[i][j]!="obstaculo" and self._gre[i][j]!=None:
                    if self._gre[i][j].identificador()==identificador:
                        pos=[j-self._cen,self._cen-i]
                j+=1
            i+=1
        return pos
    
    def livre(self, posicao):
        return self._gre[self._cen-posicao[1]][self._cen+posicao[0]]==None
    
    def dentrogrelha(self, posicao):
        while posicao[0]>self._lad:
            posicao[0]=posicao[0]-self._lad+1
        while posicao[0]<self._lad:
            posicao[0]=posicao[0]+self._lad-1
        while posicao[1]>self._lad:
            posicao[1]=posicao[1]-self._lad+1
        while posicao[1]<self._lad:
            posicao[1]=posicao[1]+self._lad-1
        return posicao
    
    def vizinhanca1(posicao):
        r=[]
        return r
    
class Evento:
    def __init__(self, tempo):
        return None