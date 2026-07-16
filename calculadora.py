 

while True:
    try:
        numero_1 = int(input('digite um numero?'))

        numero_2 =  int(input('Qual segundo Numero?'))
    except ValueError:
        print('Numero inválido')
        continue
    operacao = input('Digite a operação(+,-,x,/): ')

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
        resultado = numero_1 / numero_2
        print(resultado)
    
    else:
        print("Digite apenas +, -, *, /")

