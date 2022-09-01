#Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
hom = float(input("Digite sua altura: "))
mul = float(input("Digite sua altura: "))
ph = (72.2 * hom) - 58
pm = (62.1 * mul) - 44.7
print(f'Homem = {ph}')
print(f'Mulher = {pm}')