def comparaValores():
    padrao= float(input('Digite um valor '))
    print('Vc digitou o valor ',padrao,' para o valor padrao.')
    valor1= float(input('Digite um valor '))
    print('Vc digitou o valor ',valor1,' para o primeiro valor.')
    if valor1 > padrao:
        return (f'O primeiro valor e maior que {padrao}.')
    if valor1 < padrao:
        return (f'O primeiro valor e menor que {padrao}.')
    if valor1 == padrao:
        return (f'O primeiro valor e equivalente a {padrao}.')
   
print(comparaValores())