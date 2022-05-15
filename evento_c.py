class evento:
    def __init__(self,ID,tipo,tempo):
        self._tempo=tempo
        self._tipo=tipo
        self._ID=ID

    def tempo(self):
        return self._tempo

    def tipo(self):
        return self._tipo
            
    def ID(self):
        return self._ID