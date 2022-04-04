#Fazer a herança das seguintes classes:
#MeioTransporte
# Terrestre  --> Carro, Caminhao
# Aquatico --> Remo, Barco
# Aereo --> Avião, Helicóptero      

from terrestre.Caminhao import Caminhao
from terrestre.Carro import Carro

from aquatico.Remo import Remo
from aquatico.Barco import Barco

from aereo.Aviao import Aviao
from aereo.Helicoptero import Helicoptero

# Terrestre  --> Carro, Caminhao
carro = Carro(5,4,"placa")
carro.andar()
caminhao = Caminhao(4,6,"placa","3")
print(caminhao.placa)
print("\n")

# Aquatico --> Remo, Barco
remo = Remo(2)
remo.remando
barco = Barco(5)
barco.navegar()
print("\n")

# Aereo --> Avião, Helicóptero   
aviao = Aviao(130,3500,"gol")
print(aviao.companhia_aerea)
helicoptero = Helicoptero(5,2000)
helicoptero.voar()