#Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
#  e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#  Informe ao usuário a quantidades de latas de tinta a serem compradas 
# e o preço total.

metro = int(input('Digite o tamanho em metro a ser pintado: '))
litros = metro / 3
prec = 80.0
capac = 18
latas = litros / capac
total = latas * prec
print('Você usara', round(latas), 'latas de tinta')
print('O preco total é de: R$ ', round(total))
