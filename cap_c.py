class CAP:
    def __init__(self):
        self.CAP=[]
              
    def adicionarE(self,e):
        i=0
        j=len(self.CAP)-1
        while (i<=j):
            m=(i+j)//2
            if e.tempo()<self.CAP[m].tempo():
                j=m-1
            else:
                i=m+1
        self.CAP.insert(j+1,e)
            
    def proxE(self):
        assert len(self.CAP)>0  
        return self.CAP[0]
    
    def retirarE(self):
        assert len(self.CAP)>0
        self.CAP=self.CAP[1:]        
    
    def eliminarID(self,ID):
        i=len(self.CAP)-1
        while i>=0:
            if self.CAP[i].ID()==ID:
                self.CAP.remove(self.CAP[i])
            i=i-1
    
    def tamC(self):
        return len(self.CAP)
              
    def mostraC(self):
        for e in self.CAP:
            print ('ID:', e.ID(),'  ','Tipo:', e.tipo(),'  ','Tempo:', e.tempo())