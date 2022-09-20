#Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, 
# se seu argumento for zero ou negativo.

def exercicio_4(argumento):
    if argumento >= 0:
        print('O número digitado foi positivo!')
    else:
        print('O número digitado foi negativo!')

argumento = int(input('Digite um número: '))

exercicio_4 (argumento)

