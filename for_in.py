texto = 'Python'

i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i], i)
    i += 1

# While é muito utilizado para ciclos nos quais não se sabe ao certo quantas repetições serão executadas.
###FUNÇÃO FOR###
texto = 'Python'

for letra in texto:
    print(letra)

texto_com_asteriscos = ''
for letra in texto:
    texto_com_asteriscos += f'*{letra}'
print(texto_com_asteriscos + '*')

###FOR + RANGE###
#range -> range(start, stop, step)
numeros = range(10) #Pega o range de 0 a 10
print(numeros)
for numero in numeros:
    print(numero)

numeros = range(5,10) # Pega o range começando de 5 até 10
print(numeros)
print(numeros[2])
for numero in numeros:
    print(numero)

numeros = range(5,10,2) # Pega o range começando de 5 até 10, pulando de dois em dois (step 2)
print(numeros)
print(numeros[2])
for numero in numeros:
    print(numero)

pares_de_0_a_100 = range(0, 100, 2)
for numero in pares_de_0_a_100:
    print(numero)

multiplos_de_8 = range(0, 100, 8)
for numero in multiplos_de_8:
    print(numero)

"""
Iterável -> Todo elemento que pode me entregar uma coisa por vez (str, range, etc)
Iterador -> quem sabe entregar um valor por vez
next -> me entrega o próximo valor
iter -> me entrega seu iterador
"""
exemplo = iter('Arthur')
print(next(exemplo))
print(next(exemplo))
print(next(exemplo))
print(next(exemplo))
print(next(exemplo))
print(next(exemplo))
# print(next(exemplo)) #Quando terminados os elementos iteráveis, o comando next trará um erro.

lingua_do_p = ''
texto = input('Digite o texto que vc quer na lingua do p: ')
for letra in texto:
    lingua_do_p += (f'p{letra}')
print(f'{lingua_do_p}p')
