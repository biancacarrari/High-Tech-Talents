# exercício para quem não pode comparecer na terça passada (dia da chuva):                                                                         Faça um programa que monte uma lista de compras na feira. Nesse programa deverá conter:
# -Uma tela para mostrar a lista de compras
# -Outra tela para cadastrar um item dessa lista
# -Outra tela para excluir um item (Deverá primeiro mostrar a lista e depois excluir o item conforme posição)
# -Login ao começar
# -Opção Sair do programa
# 
# LOGIN PRÉ CADASTRADO
# Usuário: Bianca
# Senha: 123456

from operator import truediv


def cadastrar(item):
    "cadastra o item"    
    listaCompras.append(item)
    print("Sucesso! Cadastrado!")
    print("\n")

def listar():
    "lista itens cadastrados"
    print("\n")
    print("Sua lista de compras é: ")
    for item in listaCompras:
        print(item)
    print("\n")
    
def validarLogin(nome,senha):
    "valida o login"    
    logins = {"Nome": "Bianca", "Senha": "123456"}
    if nome==logins["Nome"] and senha==logins["Senha"]:
        return True
    else:
        return False

while True:
    usuario = input("Entre com o seu nome: ")
    senha = input("Entre com o sua senha: ")
    listaCompras = []

    if validarLogin(usuario,senha):
        print(f"Seja Bem-vindo(a) {usuario} !\n")
        while True:
            print("Selecione uma opção:")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("3 - Sair")
            opcao = int(input(""))
            if opcao in [1,2,3]:
                if opcao == 1: #Cadastrar
                    item_usu = ""
                    while item_usu == "":
                        item_usu = input("Coloque o item: ")
                    cadastrar(item_usu)
                    
                elif opcao == 2: #Listar           
                    listar()
                    
                elif opcao == 3:#Sair
                    print("\n")
                    print("Saindo do sistema...")
                    break
            else:
                print("Opção Inválida!")
    else:
        print("Tente novamente")
