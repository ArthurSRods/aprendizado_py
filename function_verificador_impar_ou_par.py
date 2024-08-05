def checaSeImparOuPar():
    numero = int(input('Digite um numero '))
    if numero % 2 == 0:
        return (f'O numero {numero} e par')
    elif numero % 2 != 0:
        return (f'O numero {numero} e impar')
    else:
        return ('Algo deu errado. ')

print(checaSeImparOuPar())