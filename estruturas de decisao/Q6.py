'''Faça um Programa que leia três números e mostre o maior deles.'''

n1 = int(input('Digite 1º número: '))
n2 = int(input('Digite 2º número: '))
n3 = int(input('Digite 3º número: '))
if n1 > n3 and n1 > n2:
    print('N1 é maior')
elif n2 > n3 and n2 > n1:
    print('N2 é o maior')
elif n3 > n2 and n3 > n1:
    print('N3 é o maior')