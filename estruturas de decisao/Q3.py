#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input("Qual é o seu sexo [F - Feminino] ou [M - Masculino]: "))
if sexo == 'M' or sexo == 'm':
    print('Seu sexo é Masculino!')
elif sexo == 'F' or sexo == 'f':
    print('Seu sexo é Feminino!')
else:
    print('Letra não consta o tipo de sexo!')