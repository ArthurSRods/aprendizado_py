frase = 'O Python e uma linguagem de programacao' \
    'multiparadigma'\
    'O Python foi criado por Guido van Rossum'.lower()

print(frase.count('python'))

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i+=1
        continue

    contagem_letra = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes<contagem_letra:
        qtd_apareceu_mais_vezes = contagem_letra
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes.upper()}", que apareceu {qtd_apareceu_mais_vezes}x. ')
