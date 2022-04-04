from MeioTransporte import MeioTransporte


class Terrestre(MeioTransporte):
    def __init__(self, capacidade_pessoas, numero_rodas):
        super().__init__(capacidade_pessoas)
        self.numero_rodas = numero_rodas
    def andar(self):
        print("Andando")
