#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
n1 = int(input("Digite 1ª valor: "))
n2 = int(input("Digite 2º valor: "))
r = float(input("Digite valor real: "))
pr = (n1 * 2) / 2
sm = (n1 * 3) + r
cub = r * 3
print(f'Dobro do produto = {pr}')
print(f'A soma do triplo = {sm}')
print(f'Elevado ao cubo {cub}')