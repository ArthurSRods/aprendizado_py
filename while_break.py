####REPETIÇÕES###
# while: Executa uma ação enquanto uma condição dada for verdadeira.

condicao = True

while condicao:
    nome = input('Digite o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break # break: encerra o laço while

print('Acabou')

nome = True

while nome is True:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome} ')

print('Acabou')

###

contador = 0
while contador < 10:
    contador += 1 
    print(contador)
print('Acabou ')

###OPERADORES ARITMETICOS###
valor = 10
valor += 1 # equivale a valor = valor + 1
print (valor) 
valor -= 1 # equivale a valor = valor - 1
print (valor)
valor *= 2 # equivale a valor = valor * 2
print (valor)
valor /= 2 # equivale a valor = valor / 2
print (valor)
valor //= 1 # equivale a valor = valor // 1
print (valor)
valor %= 2 # equivale a valor = valor % 2
print (valor)
