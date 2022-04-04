from aereo.aereo import Aereo
        
class Helicoptero(Aereo):
    def __init__(self, capacidade_pessoas, altitude_max):
        super().__init__(capacidade_pessoas, altitude_max)