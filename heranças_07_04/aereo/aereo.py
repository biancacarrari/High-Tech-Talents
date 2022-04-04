from MeioTransporte import MeioTransporte

class Aereo(MeioTransporte):
    def __init__(self, capacidade_pessoas, altitude_max):
        super().__init__(capacidade_pessoas)
        self.altitude_max = altitude_max
    
    def voar(self):
        print("Voando")

class Aviao(Aereo):
    def __init__(self, capacidade_pessoas, altitude_max, companhia_aerea):
        super().__init__(capacidade_pessoas, altitude_max)
        self.companhia_aerea = companhia_aerea
        
class Helicoptero(Aereo):
    def __init__(self, capacidade_pessoas, altitude_max):
        super().__init__(capacidade_pessoas, altitude_max)
