#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:58:07 2018

@author: miguelf
"""
        
import random


def new(n):
    a=[]
    for i in range(n):
        b=[]
        for j in range(n):
            b=b+["0"]
        a=a+[b]
    return a

#SEIR

class individuo:
    def __init__(self, identificador, estado):
        self._identificador=identificador
        self._estado=estado
        def estado(self):
            return self.estado
            

class grid:
    def __init__(self, n):
        r=[]
        for i in range(2*n+1):
            a=[]
            for j in range(2*n+1):
                a+=[0]
            r+=[a]
        self.grelha=r
        self.n=n
        self.nindividuos=0
        
    def verestados(self):
        for i in range(self.n*2+3):
            print("*", end="")
        print("")
        for i in self.grelha:
            print("*", end="")
            for j in i:
                if j==None:
                    print("-", end="")
                else:
                    print(j.estado, end="")
            print("*")
        for i in range(len(self.grelha)+2):
            print("*", end="")
    
    def veridentificadores(self):
        for i in range(self.n*2+3):
            print("*", end="")
        print("")
        for i in self.grelha:
            print("*", end="")
            for j in i:
                if j==None:
                    print("0", end="")
                else:
                    print(j.identificador, end="")
            print("*")
        for i in range(len(self.grelha)+2):
            print("*", end="")
    
    def inserir(self, ind, pos):
        self.grelha[pos.x][pos.y]=ind
    
    def retirar(self, pos):
        self.grelha[pos.x][pos.y]=None
        
    def posicaoindividuo(self, identificador):
        r=[]
        i=0
        while i<len(self.grelha):
            j=0
            while j<len(i):
                if j[i][j].identificador==identificador:
                    r=pos(i,j)
                j+=1
            i+=1
        return r
    def popula(self, ps,pi):
        sus=[]
        for i in range(ps):
            sus+=[pos(random.randrange(2*self.n+1),random.randrange(2*self.n+1))]
        infec=[]
        for i in range(pi):
            infec+=[pos(random.randrange(2*self.n+1),random.randrange(2*self.n+1))]
        
        
        for i in sus:
            self.inserir(individuo(self.nindividuos,"S"),i)
            self.nindividuos+=1
        for i in infec:
            self.inserir(individuo(self.nindividuos,"I"),i)
            self.nindividuos+=1
    
    def vazioQ(self, p):
        return self.grelha(p.x,p.y)==None
    
    
#class pos():
#    def __init__(self, x, y):
#        self.x=x
#        self.y=y
        

        




    

