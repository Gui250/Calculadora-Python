print("*******************************")
print("Bem vindo a calculadora")
print("*******************************")


entrada = int(input("Digite (1) para soma, (2) para subtração, (3) para multiplicação, (4) para divisão, ou digite qualquer tecla para sair: "))

calculadora = True

while(calculadora):
    if(entrada == 1): 
        print("Utilizando soma")
        a = int(input("Digite um número: "))
        b = int(input("Digite outro número: "))
        c = a + b 
        print(f'A soma dos números é {c} ')
        break
    elif(entrada == 2): 
        print("Utilizando subtração")
        a = int(input("Digite um número: "))
        b = int(input("Digite outro número: "))
        c = a - b
        print(f'A subtração dos números é {c}')
        break
    elif(entrada == 3): 
        print("Utilizando multiplicação")
        a = int(input("Digite um número: "))
        b = int(input("Digite outro número: "))
        c = a * b
        print(f'A multiplicação dos números é {c}')
        break
    elif(entrada == 4): 
        print("Utilizando divisão")
        a = int(input("Digite um número: "))
        b = int(input("Digite outro número: "))
        c = a / b
        print(f'A divisão do número é {c}')
        break
    else:
        break
