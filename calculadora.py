 
import os

while True:
    
    sair = input('Digite "sair" ou aperte enter pra continuar:').lower()
    if sair == 'sair':
        print("Calculadora encerrada")
        break
    try:
        numero_1 = int(input('digite um numero?'))

        numero_2 =  int(input('Digite outro Numero?'))
    except ValueError:
        print('Numero inválido')
        continue
    operacao = input('Digite a operação(+,-,x,/): ').lower()

    if operacao == '+':
        
        resultado = numero_1 + numero_2

        print(resultado)
        

    elif operacao == '-':
        
        resultado = numero_1 - numero_2
        print(resultado)
        
    elif operacao == 'x':
      
        resultado = numero_1 * numero_2
        print(resultado)
    elif operacao == '/':
        
        if numero_2 ==  0:
            print('Não é possivel dividir por zero')
        else:
            resultado = numero_1 / numero_2
            print(resultado)
    
    else:
           print("Digite apenas +, -, x, /")


