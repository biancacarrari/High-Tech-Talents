from MeioTransporte import MeioTransporte

class Aquatico(MeioTransporte):
    def __init__(self, capacidade_pessoas):
        super().__init__(capacidade_pessoas)

    def navegar(self):
        print("Navegando")
        
