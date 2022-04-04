usuario = input("Entre com o seu nome: ")
print(f"Seja Bem-vindo {usuario} !\n")

while True:
    print("Selecione uma opção:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opcao = int(input(""))
    if opcao in [1,2,3,4,5]:
        num1 = ""
        num2 = ""
        while num1 == "":
            num1 = int(input("Coloque o primeiro número: "))
        while num2 == "":
            num2 = int(input("Coloque o segundo número: "))
        if opcao == 1: #Adição
            print(num1+num2)
            
        elif opcao == 2: #Subtração
            print(num1-num2)
        
        elif opcao == 3: #Multiplicação
            print(num1*num2)
            
        elif opcao == 4: #Divisão
            print(num1/num2)
            
        elif opcao == 5:#Sair
            print("Saindo do sistema...")
            break
    else:
        print("Opção Inválida!")