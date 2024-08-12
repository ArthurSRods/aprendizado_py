###REPETIÇÕES###
contador = 0
while contador < 40:
    contador += 1

    if contador == 6:
        print('não vou mostrar o 6')
        continue 

    if contador >= 10 and contador <= 27:
        print('vou pular o intervalo entre 10 e 27')
        continue 

    if contador == 39:
        break
    print(contador)
print('Acabou ')

###LAÇOS INTERNOS###
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    print(linha)

    while coluna <= qtd_colunas:
        print(f'{linha=},{coluna=}')
        coluna+=1

    linha +=1

print('Acabou ')