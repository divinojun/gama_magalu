#Faça um programa para imprimir:
# 1
#    1   2
#   1   2   3
#    .....
#    1   2   3   ...  n

def exercicio2(lista):
    numero = int(input('Digite um número: '))
    linha = ''
    for i in range(1, numero + 1):
        linha = linha + str(i) + ''
        print(linha)

exercicio2(range)
