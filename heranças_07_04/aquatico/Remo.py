from aquatico.aquatico import Aquatico

class Remo(Aquatico):
    def __init__(self, capacidade_pessoas):
        super().__init__(capacidade_pessoas)
    
    def remando(self):
        print("Remando")