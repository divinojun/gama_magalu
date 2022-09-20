#Faça uma função que informe a quantidade de dígitos de um determinado 
# número inteiro informado

from tkinter import N


def inteiros(num):
    return len(str(num))

n = str(input('Digite um número inteiro >: ')).strip()
print(f'Esse número tem {inteiros(n)} digitos')