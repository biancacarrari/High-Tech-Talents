from terrestre.terrestre import Terrestre

class Caminhao(Terrestre):
    def __init__(self, capacidade_pessoas, numero_rodas,placa,eixos):
        super().__init__(capacidade_pessoas,numero_rodas)
        self.placa = placa
        self.eixos = eixos