#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
#  no mês. Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% 
# para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:

salario = int(input("Quanto você ganha por hora: "))
horas = int(input("Quantas horas trabalhada por mês: "))
total = salario * horas
inss = total * 8 / 100
imprenda = total * 11 / 100
sind = total * 5 / 100
salaliquido = total - inss - imprenda - sind     
print('Salario bruto: ', total)     
print('INNS (8%) : ', inss)     
print('IR (11%) : ',imprenda)     
print('Sindicato (5%) : ', sind)
print('Salario liquido : RS', salaliquido)     