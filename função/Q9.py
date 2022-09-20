#Reverso do número. Faça uma função que retorne o reverso de um 
# número inteiro informado. 
# Por exemplo: 127 -> 721.

def inteiro(num):
    return str(num[::-1])

num = str(input('Digite um número >: ')).strip()
print(f'O reverso do {num} é {inteiro(num)}')

inteiro(num)