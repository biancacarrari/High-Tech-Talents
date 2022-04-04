from terrestre.terrestre import Terrestre

class Carro(Terrestre):
    def __init__(self, capacidade_pessoas, numero_rodas,placa):
        super().__init__(capacidade_pessoas,numero_rodas)
        self.placa = placa