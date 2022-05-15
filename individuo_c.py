class individuo:
    
    def __init__(self,ID,estado):
        self._ID=ID
        self._estado=estado
        
    def ID(self):
        return self._ID
    
    def estado(self):
        return self._estado
    
    def mudae(self,e):
        self._estado=e