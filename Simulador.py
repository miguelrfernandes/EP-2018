import evento_c as Evento
import cap_c as CAP
import individuo_c as Individuo
import grelha_c as Grelha
import random as R
import math as M
import matplotlib.pyplot as plt

def Sim(N,Ps,Pi,Th,Td,Tr,Tm,pd,pr,pm,Tas,Tae,Tai,o,cen,peradj):
    
    E=Evento.evento
    I=Individuo.individuo
    G=Grelha.grelha
    
    global novoID
    novoID=0
    
    
    def texp(x):
        r=R.random()
        return -x*M.log(r)
    
    
    def novoI(e,p,t):
        global novoID
        ind=I(novoID,e)
        G.insI(ind,p)
        C.adicionarE(E(ind.ID(),'D',t+texp(Td)))
        C.adicionarE(E(ind.ID(),'R',t+texp(Tr)))
        C.adicionarE(E(ind.ID(),'M',t+texp(Tm)))
        if e=='I':
            C.adicionarE(E(ind.ID(),'A',t+texp(Tai)))
        else:
            C.adicionarE(E(ind.ID(),'A',t+texp(Tas)))
        novoID=novoID+1
                    
                    
    def popular(w,Ps,Pi,cen,padj):
        if cen=='b':
            PA=round((Ps+Pi)*padj)
            ini=False
            while not ini:
                pos=[R.randint(-N,N),R.randint(-N,N)]
                if G.obj(pos)==None:
                    if Ps>0 and Pi>0:
                        e="I" if R.randint(0,1)==0 else "S"
                    elif Pi==0:
                        e='S'
                        Ps=Ps-1
                    elif Ps==0:
                        e='I'
                        Pi=Pi-1
                    novoI(e,pos,0)
                    x=pos
                    ini=True
            PA=PA-1
            while PA>0:
                p=R.choice(G.lis_Q(G.livQ,G.viz1(G.obj(x).ID())))
                if Ps>0 and Pi>0:
                    e="I" if R.randint(0,1)==0 else "S"
                elif Pi==0:
                    e='S'
                    Ps=Ps-1
                elif Ps==0:
                    e='I'
                    Pi=Pi-1
                novoI(e,p,0)
                x=p
                PA=PA-1
            cen='a'
            
        if cen=='a':
            while Ps>0:
                pos=[R.randint(-N,N),R.randint(-N,N)]
                if G.obj(pos)==None:
                    novoI('S',pos,0)
                    Ps=Ps-1
            while Pi>0:
                pos=[R.randint(-N,N),R.randint(-N,N)]
                if G.obj(pos)==None:
                    novoI('I',pos,0)
                    Pi=Pi-1
    
    
    def Pe(x):
        n1=len(G.lis_Q(G.infQ,G.viz1(x)))
        n2=0
        for i in G.lis_Q(G.infQ,G.viz2(x)):
            if G.contactoQ(x,i):
                n2=n2+1
        y=2*n1+n2
        return (1/(2*M.log(1.8)))-(1/(2*M.log(((y*(y-1))/5)+1.8)))
    
    
    G=Grelha.grelha(N,o)
    C=CAP.CAP()
    popular(G,Ps,Pi,cen,peradj)
    tempo=0
    
    nInf=Pi
    grafx=[tempo]
    grafy=[nInf]
    
    file=open("resultados.txt","w")
    file.write(str(N)+"\n")
    file.write(str(o)+"\n")
        
    prox=C.proxE()
    tempo=prox.tempo()
    x=prox.ID()
        
    while tempo<Th and C.tamC()>0:
        
        c=False
        C.retirarE()
         
        
        if prox.tipo()=='D':
            
            p=G.encontrar(x)
            b=G.obj(p)
            i=G.lis_Q(G.infQ,G.viz1(x))
            l=G.lis_Q(G.livQ,G.viz1(x))
            
            if len(l)>0:
                r=R.randint(0,len(l)-1)
                
                if len(i)>2:
                    G.insI(b,l[r])
                    G.delI(p)
                    c=True
                    
                elif len(i)<3 and R.random()<=pd:
                    G.insI(b,l[r])
                    G.delI(p)
                    c=True
                    
            C.adicionarE(E(x,'D',tempo+texp(Td)))
            
            
        elif prox.tipo()=='R':
            
            l=G.lis_Q(G.livQ,G.viz1(x))
            o=G.lis_Q(G.ocuQ,G.viz1(x))
            
            if len(l)>1 and len(o)>0 and R.random()<=pr: 
                s=R.randint(0,len(l)-1)      
                novoI('S',l[s],tempo)   
                c=True                
                
            C.adicionarE(E(x,'R',tempo+texp(Tr)))
            
            
        elif prox.tipo()=='M':
            
            p=G.encontrar(x)
            b=G.obj(p)
            r=R.random()
            
            if I.estado(b)=='I' and r<=min(1,pm+0.1):
                G.delI(G.encontrar(x))
                C.eliminarID(x)
                c=True                
                
                grafx=grafx+[tempo]
                nInf=nInf-1
                grafy=grafy+[nInf]
                
            elif I.estado(b)!='I' and r<=pm:
                G.delI(G.encontrar(x))
                C.eliminarID(x)
                c=True                
            
            else:
                C.adicionarE(E(x,'M',tempo+texp(Tm)))
                
        elif prox.tipo()=='A':
            
            v=G.viz1(x)+G.viz2(x)
            i=G.obj(G.encontrar(x))
            r=R.random()
            
            if I.estado(i)=='I':
                I.mudae(i,'R')
                c=True
                
                grafx=grafx+[tempo]
                nInf=nInf-1
                grafy=grafy+[nInf]
                
            elif I.estado(i)=='E':
                I.mudae(i,'I')
                C.adicionarE(E(x,'A',tempo+texp(Tai)))
                c=True
                
                grafx=grafx+[tempo]
                nInf=nInf+1
                grafy=grafy+[nInf]
                
            elif len(G.lis_Q(G.infQ,v))==0 or r>Pe(x):
                C.adicionarE(E(x,'A',tempo+texp(Tas)))
                c=True
                
            elif len(G.lis_Q(G.infQ,v))>0 and r<=Pe(x):
                I.mudae(i,'E')
                C.adicionarE(E(x,'A',tempo+texp(Tae)))
                c=True
                
                
        if c:
            file.write(str(G.c_estados())+"\n")                   
        
        
        prox=C.proxE()
        tempo=prox.tempo()
        x=prox.ID()
        
    file.close()
    plt.plot(grafx,grafy, '-r')
    plt.axis([0, Th, 0, max(grafy)+1])
    plt.title("Número de Infetados ao longo do tempo")
    plt.xlabel("Tempo")
    plt.ylabel("Número de Infetados")    
    plt.show()