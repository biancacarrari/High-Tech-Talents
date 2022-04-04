from aereo.aereo import Aereo

class Aviao(Aereo):
    def __init__(self, capacidade_pessoas, altitude_max, companhia_aerea):
        super().__init__(capacidade_pessoas, altitude_max)
        self.companhia_aerea = companhia_aerea
        