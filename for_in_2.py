for i in range(10):
    if i == 2:
        print('i é 2, pulando')
        continue
    for j in range(1,5):
        print(i,j)

for i in range(0, 10):
    if i % 2 == 0:
        print(f'{i} é par.')
        continue
    elif i == 9:
        print('i é 9. Seu else não será executado.')
        break
    else:
        print('For completo.')

