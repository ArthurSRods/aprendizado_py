###CALCULADORA COM WHILE###
while True:
    #NUMEROS
    primeiro_numero = input('Digite um número ')
    segundo_numero = input('Digite outro número ')
    
    try:
        primeiro_numero_float = float(primeiro_numero)
        segundo_numero_float = float(segundo_numero)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Algum dos numeros digitados é inválido. ')
        continue # Se os numeros digitados forem invalidos, a calculadora voltará pro começo do laço.
    
    #OPERADOR
    operador = input('Qual operação vc quer realizar? (+-/*) ')
    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido ')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador. ')
        continue

    #OPERAÇÕES
    print('Realizando sua conta. Confira o resultado abaixo ')
    if operador == '+':
        print(f'{primeiro_numero_float} + {segundo_numero_float} = {primeiro_numero_float+segundo_numero_float}')
    elif operador == '-':
        print(f'{primeiro_numero_float} - {segundo_numero_float} = {primeiro_numero_float-segundo_numero_float}')
    elif operador == '/':
        print(f'{primeiro_numero_float} / {segundo_numero_float} = {primeiro_numero_float/segundo_numero_float}')
    elif operador == '*':
        print(f'{primeiro_numero_float} * {segundo_numero_float} = {primeiro_numero_float*segundo_numero_float}')

    #SAIR
    sair = input('Quer sair? digite [S] para sim ').upper().startswith('S')
    if sair is True:
        break

print('Voce saiu. ')