#Construa uma função que receba uma data no formato 
# DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
# Opcionalmente,valide a data e retorne NULL caso a data seja inválida.


def dataExtenso():
    mes = ['janeiro',
            'fevereiro', 
            'Março',
            'Abril',
            'Junho',
            'Julho',
            'Agosto',
            'Setembro',
            'Outumbro',
            'Novembro',
            'Dezembro']
    data = str(input('Digita a data: '))
    print(data.split('/')[0], 'de', mes[(int(data.split('/')[1])-1)], 'de', data.split('/')[2])
dataExtenso()