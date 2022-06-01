print ("Calculadora:")
cont = 1 #variavel de controle do while
while(cont == 1): # repeti enquanto a opção for igual a 1
    opcao = int(input("escolha uma operação: 1 para + , 2 para -, 3 para x, 4 para/:")) #escolha das perações 

    if(opcao < 1 or opcao > 4): # testa se a opção é valida 
        print("opção invalida: ") # a opção digitada for invalida mostra o erro 
    else: # se a opção digitada for verdadeira execulta essa bloco

        n1 = float(input("Digite o Primeiro numero: ")) # variaveis de entrada 
        n2 = float(input("Digite o segundo numero numero: "))

        if(opcao == 1): # faz a soma de n1 e n2
            soma  = n1 + n2 
            print(f"{n1} + {n2} = {soma}")
        elif(opcao == 2): # faz a subtração de n1 e n2
            sub = n1 - n2
            print(f"{n1} - {n2} = {sub}")
        elif(opcao == 3): # faz a multiplacação de n1 e n2
            mult = n1 * n2
            print(f"{n1} x {n2} = {mult}")
        elif(opcao == 4): # faz a Divisão de n1 e n2
            div = n1 / n2
            print(f"{n1} / {n2} = {div}")
        else:
            print("opção invalida!!")
    cont = int(input("Digite 1 para fazer outra operação, ou qualque tecla para sair!!\n"))