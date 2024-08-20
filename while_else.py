###WHILE/ELSE###
string = input('Digite algo ')

i = 0
while i < len(string):
    letra = string[i]
    print(letra)
    i += 1

    if letra == ' ':
        break

else:
    print('O else foi execultado depois que a condição do while foi cumprida. ')
    # Caso haja um break no laço while, o else não será executado.

print('Fora do laço. ')