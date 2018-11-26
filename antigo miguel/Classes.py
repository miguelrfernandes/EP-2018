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
    def __init__(self, N, obstaculos):
        self._obs=obstaculos
        self._n=N
        self._lad=N*2+1 #lado da rede
        
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
            
    def numeroindividuos():
        i=0
        yield i
        i+=1
    
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
    
    def individuo(self, pos):
        return self._gre[self._cen-pos[1]][self._cen+pos[0]]
    
    def livre(self, posicao):
        return self._gre[self._cen-posicao[1]][self._cen+posicao[0]]==None
    
    def dentrogrelha(self, posi):
        while posi[0]>self._n:
            posi[0]=posi[0]-self._lad
        while posi[0]<-self._n:
            posi[0]=posi[0]+self._lad
        while posi[1]>self._n:
            posi[1]=posi[1]-self._lad
        while posi[1]<-self._n:
            posi[1]=posi[1]+self._lad
        return posi
    
    def vizinhanca1(self, posicao):
        vizinhos=[]
        translacoes=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        for i in translacoes:
            vizinhos+=[self.dentrogrelha([posicao[0]+i[0],posicao[1]+i[1]])]
        return vizinhos
    
    def vizinhanca2(self, posicao):
        vizinhos=[]
        translacoes=[[-2,-2],[-2,-1],[-2,0],[-2,1],[-2,2],
                     [-1,-2],[-1,2],[0,-2],[0,2],[1,-2],[1,2],
                     [2,-2],[2,-1],[2,0],[2,1],[2,2],
                     ]
        for i in translacoes:
            vizinhos+=[self.dentrogrelha([posicao[0]+i[0],posicao[1]+i[1]])]
        return vizinhos
    
    def popular(self, infectados, suscetiveis):  #verificar se é aleatório
        for i in range(infectados):
            pos=[random.randrange(self._n),random.randrange(self._n)]
            while not self.livre(pos):
                pos=[random.randrange(self._n),random.randrange(self._n)]
            self.inserir(Individuo(self.numeroindividuos, "I"), pos)
        for i in range(suscetiveis):
            pos=[random.randrange(self._n),random.randrange(self._n)]
            while not self.livre(pos):
                pos=[random.randrange(self._n),random.randrange(self._n)]
            self.inserir(Individuo(self.numeroindividuos, "S"), pos)
    def numinfetados(self):
        num=0
        i=0
        while i<len(self._gre):
            j=0
            while j<len(self._gre):
                if self._gre[i][j]!="obstaculo" and self._gre[i][j]!=None:
                    if self._gre[i][j].estado()=="I":
                        num+=1
                j+=1
            i+=1
        return num
    
    def coordenadasindividuos(self):
        coordenadas=[]
        i=0
        while i<len(self._gre):
            j=0
            while j<len(self._gre):
                if self._gre[i][j]!="obstaculo" and self._gre[i][j]!=None:
                    coordenadas+=[[j-self._cen,self._cen-i]]
                j+=1
            i+=1
        return coordenadas
    
    def coordenadassuscetiveis(self):
        coordenadas=[]
        i=0
        while i<len(self._gre):
            j=0
            while j<len(self._gre):
                if self._gre[i][j]!="obstaculo" and self._gre[i][j]!=None:
                    if self._gre[i][j].estado()=="S":
                        coordenadas+=[[j-self._cen,self._cen-i]]
                j+=1
            i+=1
        return coordenadas
    
    def coordenadasexpostos(self):
        coordenadas=[]
        i=0
        while i<len(self._gre):
            j=0
            while j<len(self._gre):
                if self._gre[i][j]!="obstaculo" and self._gre[i][j]!=None:
                    if self._gre[i][j].estado()=="I":
                        coordenadas+=[[j-self._cen,self._cen-i]]
                j+=1
            i+=1
        return coordenadas
    
    def coordenadasinfetados(self):
        coordenadas=[]
        i=0
        while i<len(self._gre):
            j=0
            while j<len(self._gre):
                if self._gre[i][j]!="obstaculo" and self._gre[i][j]!=None:
                    if self._gre[i][j].estado()=="I":
                        coordenadas+=[[j-self._cen,self._cen-i]]
                j+=1
            i+=1
        return coordenadas
    
    def coordenadasrecuperados(self):
        coordenadas=[]
        i=0
        while i<len(self._gre):
            j=0
            while j<len(self._gre):
                if self._gre[i][j]!="obstaculo" and self._gre[i][j]!=None:
                    if self._gre[i][j].estado()=="R":
                        coordenadas+=[[j-self._cen,self._cen-i]]
                j+=1
            i+=1
        return coordenadas
    
    
    
    
    def verestados(self):
        for i in range(len(self._gre)+2):
            print("*", end=" ")
        print("")
        for i in self._gre:
            print("*", end=" ")
            for j in i:
                if j=="obstaculo":
                    print("*", end=" ")
                elif j==None:
                    print("-", end=" ")
                else:
                    print(j.estado(), end=" ")
            print("*")
        for i in range(len(self._gre)+2):
            print("*", end=" ")
    
    def veridentificadores(self): #não está a funcionar corretamente
        for i in range(len(self._gre)+2):
            print("*", end=" ")
        print("")
        for i in self._gre:
            print("*", end=" ")
            for j in i:
                if j=="obstaculo":
                    print("*", end=" ")
                elif j==None:
                    print("-", end=" ")
                else:
                    print(j.identificador(), end=" ")
            print("*")
        for i in range(len(self._gre)+2):
            print("*", end=" ")
            
            
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
    
class CAP:
    def __init__(self):
        self._cad = []

    def adicionar(self, evento):
        m1=0
        m2=len(self._cad)-1
        while m1<=m2:
            a=(m1+m2)//2
            if evento.tempo()>self._cad[a].tempo():
                m1=a-1
            else:
                m2=a+1
        self._cad.insert(m2,evento)
    
    def remover(self):
        if len(self._cad)>0:
            return self._cad[1:]
        else:
            print("A função remover() encontrou um erro: A CAP está vazia.")
            
    def removeridentificador(self, identificador):
        for evento in self._cad:
            if evento.identificador()==identificador:
                self._cad.pop(evento)
    
    def proximo(self):
        if len(self._cad)>0:
            return self._cad[0]
        else:
            print("A função proximo() encontrou um erro: A CAP está vazia.")
        
    def mostrar(self):
        for evento in self._cad:
            print(evento.tempo(), evento.tipo())   
            
def Sim(N, obstaculos, Ps, Pi, Th, pd, pm):
    gre=Grelha(N, obstaculos)
    gre.popular(Pi, Ps)
    cad=CAP()
    cad.adicionar(Evento(1,"M",4))
    tsim=0
    while tsim<Th:
        tsim+=cad.proximo()._tem
        for posind in gre.coordenadasindividuos():
            
            #deslocamento
            viz1=gre.vizinhanca1(posind)
            viz1livre=[]
            for i in viz1:
                if gre.livre(i):
                    viz1livre+=i
            #pelo menos 3 individuos infectados e posicoes livres
            vizinf=0
            for i in viz1:
                if not gre.livre(i) and not isinstance(gre.individuo(i),str):
                    if gre.individuo(i).estado()=="I":
                        vizinf+=1
                    
            if vizinf>=3 or random.randrange(3)>pd:
                posdes=[random.randrange(gre._n),random.randrange(gre._n)]
                while not gre.livre(posdes):
                    posdes=[random.randrange(gre._n),random.randrange(gre._n)]
                gre.inserir(gre.individuo(posind), posdes)
                gre.remover(posind)
        cad.adicionar(Evento(1,"M",4))
            
            
    
