#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganho = int(input("Qual seu salario por h: "))
hora = int(input("Quanta horas trabalhadas no mês: "))
total = ganho * hora
print(f'O total de ganho foi de {total}')