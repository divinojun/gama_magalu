#Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input("1º número: "))
n2 = int(input("2º número: "))
if n1 > n2:
    print('O {} é maior'.format(n1))
else:
    print('O {} é maior'.format(n2))