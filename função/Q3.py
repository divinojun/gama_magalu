#Faça um programa, com uma função que necessite de três argumentos, 
# e que forneça a soma desses três argumentos.

def exercicio_3(n1, n2, n3):
    soma = n1 + n2 + n3
    print(f'A soma dos três argumentos é {soma}')

n1 = int(input('Digite 1º número: '))
n2 = int(input('Digite 2º número: '))
n3 = int(input('Digite 3º número: '))

exercicio_3(n1, n2, n3)
