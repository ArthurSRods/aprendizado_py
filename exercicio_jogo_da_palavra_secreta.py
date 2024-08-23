"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra_secreta = 'abacate'
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativas +=1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    
    print(palavra_formada)
    print(f'Tentativas: {tentativas}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Voce conseguiu!')
        print(f'A palavra era {palavra_secreta}')
        print(f'Tentativas: {tentativas}')
        break