#Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal,
#  usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input("Digite a sua altura: "))
p = (72.7 * altura) - 58
print('Seu peso é %.2f'.format(p))