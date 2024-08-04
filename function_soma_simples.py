def boas_vindas():
    nome = input('Digite seu nome ')
    return (f'Olá {nome}, bem vindo ao Python!')
print(boas_vindas())

def soma():
    valor1 = int(input('Digite um valor int '))
    valor2 = int(input('Digite um valor int '))
    resultado = valor1+valor2
    return resultado
print(soma())