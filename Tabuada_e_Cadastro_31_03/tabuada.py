# Fazer um programa que imprima a tabuada do 0 até o 10
# no (Console)
# 1-) Entender o problema
# Gerar as tabuadas do 0 até o 10 no console
# 2-) Planejar a solução (Console)
# Criar um sistema que tenha os seguinte:
# -Um login/boas vindas
# -Menu
#   -Multiplicar
#   -Sair
# 3-) Dividir/Planejar Tarefas
# -Criação tela login
# -Criação Menu principal
# -Criação funcionalidade Sair
# -Criação Tela "Multiplicar"
#   -Preparar loops
# 4-) Estimar tempo de desenvolvimento (Até a metade da aula)

def tabuada(número):
    i = int(número)
    "imprime tabuada do número informado"
    for j in range(11):
        print(f"{i} x {j} = {i*j}")
    print("\n")
   

usuario = input("Entre com o seu nome: ")
print(f"Seja Bem-vindo {usuario} !\n")
lista = []
while True:
    print("Selecione uma opção:")
    print("1 - Multiplicar")
    print("2 - Sair")
    opcao = int(input(""))
    if opcao in [1,2]:
        if opcao == 1: #Multiplicar
            print("Iniciando a multiplicação")
            for i in range(11):
                tabuada(i)
            print("Sucesso!")
        elif opcao == 2:#Sair
            print("Saindo do sistema...")
            break
    else:
        print("Opção Inválida!")