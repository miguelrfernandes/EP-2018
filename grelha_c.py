class grelha:
    def __init__(self,N,o):
        self._N=N
        self._l=2*N+1
        w=[]
        for j in range(2*N+1):
            s=[]
            for i in range(2*N+1):
                s=s+[None]
            w=w+[s]
        for p in o:
            w[N-p[1]][N+p[0]]='O'
        self.G=w 
    
    def encontrar(self,ID):
        for i in range(len(self.G)):
            for j in range(len(self.G)):
                if self.G[i][j]!="O" and self.G[i][j]!=None:
                    if self.G[i][j].ID()==ID:
                        return [j-self._N,self._N-i]
    
    def obj(self, p):
        return self.G[self._N-p[1]][self._N+p[0]]
    
    def insI(self,ind,p):
        self.G[self._N-p[1]][self._N+p[0]]=ind
    
    def delI(self,p):
        self.G[self._N-p[1]][self._N+p[0]]=None
        
    def usaQ(self,p):
        return self.obj(p)!='O'   
    
    def livQ(self,p):
        return self.obj(p)==None

    def ocuQ(self,p):
        return self.obj(p)!=None and self.obj(p)!='O'
    
    def susQ(self,p):
        return self.obj(p)!=None and self.obj(p)!='O' and self.obj(p).estado()=='S'   
    
    def expQ(self,p):
        return self.obj(p)!=None and self.obj(p)!='O' and self.obj(p).estado()=='E' 
    
    def infQ(self,p):
        return self.obj(p)!=None and self.obj(p)!='O' and self.obj(p).estado()=='I' 
    
    def recQ(self,p):
        return self.obj(p)!=None and self.obj(p)!='O' and self.obj(p).estado()=='R'   
          
    def lis_Q(self,c,w):
        return list(x for x in w if c(x))
    
    def dentrogrelha(self,p):
        while p[0] > self._N:
            p[0] = p[0] - self._l
        while p[0] < -self._N:
            p[0] = p[0] + self._l
        while p[1] > self._N:
            p[1] = p[1] - self._l
        while p[1] < -self._N:
            p[1] = p[1] + self._l
        return p

    def viz1(self,ID):
        p=self.encontrar(ID)
        v = []
        t = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        for i in t:                 
            v=v+[self.dentrogrelha([p[0]+i[0],p[1]+i[1]])]
        return v

    def viz2(self,ID):
        p=self.encontrar(ID)
        v = []
        t = [[-2,-2],[-2,-1],[-2,0],[-2,1],[-2,2],[-1,-2],[-1,2],[0,-2],[0,2],[1,-2],[1,2],[2,-2],[2,-1],[2,0],[2,1],[2,2]]
        for i in t:
            v=v+[self.dentrogrelha([p[0]+i[0],p[1]+i[1]])]                 
        return v
    
    def contactoQ(self,aID,bp):
        if bp in self.lis_Q(self.usaQ,self.viz1(aID)):
            return True
        for i in self.lis_Q(self.usaQ,self.viz1(self.obj(bp)._ID)):
            if i in self.lis_Q(self.usaQ,self.viz1(aID)):
                return True
        return False          
            
    def nInf(self):
        n=0
        for i in self.G:
            for j in i:
                if j is not None and not isinstance(j,str):
                    if j.estado()=='I':
                        n=n+1
        return n   
    
    def c_estados(self):
        w=[[],[],[],[]]
        i=0
        while i<len(self.G):
            j=0
            while j<len(self.G):
                if self.G[i][j] is not None and not isinstance(self.G[i][j],str):
                    if self.G[i][j].estado()=='S':
                        w[0]=w[0]+[(j-self._N,self._N-i)]
                    if self.G[i][j].estado()=='E':
                        w[1]=w[1]+[(j-self._N,self._N-i)]
                    if self.G[i][j].estado()=='I':
                        w[2]=w[2]+[(j-self._N,self._N-i)]
                    if self.G[i][j].estado()=='R':
                        w[3]=w[3]+[(j-self._N,self._N-i)]
                j+=1
            i+=1
        return w