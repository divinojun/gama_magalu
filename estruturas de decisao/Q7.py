from calendar import c


n1 = int(input('Digite 1º número: '))
n2 = int(input('Digite 2º número: '))
n3 = int(input('Digite 3º número: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
  maior = n3
menor = n1  
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print('O MENOR é {}'.format(menor))
print('O MAIOR é {}'.format(maior))
