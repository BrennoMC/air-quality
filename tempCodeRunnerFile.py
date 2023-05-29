MP10_quality = {
    'Boa': list(range(0, 51)),
    'Moderada': list(range(51, 101)),
    'Ruim': list(range(101, 151)),
    'Muito Ruim': list(range(151, 251))
}

MP25_quality = {
    'Boa': list(range(0, 26)),
    'Moderada': list(range(26, 51)),
    'Ruim': list(range(51, 76)),
    'Muito Ruim': list(range(76, 126))
}

O3_quality = {
    'Boa': list(range(0, 101)),
    'Moderada': list(range(101, 131)),
    'Ruim': list(range(131, 161)),
    'Muito Ruim': list(range(161, 201))
}

CO_quality = {
    'Boa': list(range(0, 10)),
    'Moderada': list(range(10, 12)),
    'Ruim': list(range(12, 14)),
    'Muito Ruim': list(range(14, 16))
}

NO2_quality = {
    'Boa': list(range(0, 201)),
    'Moderada': list(range(201, 241)),
    'Ruim': list(range(241, 321)),
    'Muito Ruim': list(range(321, 1131))
}

SO2_quality = {
    'Boa': list(range(0, 21)),
    'Moderada': list(range(21, 41)),
    'Ruim': list(range(41, 366)),
    'Muito Ruim': list(range(366, 801))
}

quality = []

def verify(poluente, qualidade):
    pessimo = True

    for key, value in qualidade.items():
        for value in value:
            if value == poluente:
                quality.append(f'{key}')
                pessimo = False

    if pessimo == True:
        quality.append('Péssima')

def prioridade(qualidade):
    prioridade = 0
    indice = 0

    for qualidade in qualidade:
        if qualidade == 'Boa' and prioridade == 0:
            prioridade = 0
            indice = qualidade
            texto = 'Qualidade boa. Não oferece riscos à saúde.'
        elif qualidade == 'Moderada' and prioridade <= 1:
            prioridade = 1
            indice = qualidade
            texto = 'Pessoas de grupos sensíveis (crianças, idosos, e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada.'
        elif qualidade == 'Ruim' and prioridade <= 2:
            prioridade = 2
            indice = qualidade
            texto = 'Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta, Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.'
        elif qualidade == 'Muito Ruim' and prioridade <= 3:
            prioridade = 3
            indice = qualidade
            texto = 'Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante, Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).'
        elif qualidade == 'Péssima' and prioridade <= 4:
            prioridade = 4
            indice = qualidade
            texto = 'Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes premeaturas em pessoas de grupos sensíveis'

    return [indice, texto]

while True:
    try:
        print("\nInsira os parametros abaixo\n")
        MP10 = float(input(" Partículas inaláveis (MP10): "))
        MP25 = float(input(" Partículas inaláveis finas (MP2,5): "))
        O3 = float(input(" Ozônio (O3): "))
        CO = float(input(" Monóxido de carbono (CO2): "))
        NO2 = float(input(" Dióxido de nitrogênio (NO2): "))
        SO2 = float(input(" Dióxido de enxofre (SO2): "))

        if MP10 < 0 or MP25 < 0 or O3 < 0 or CO < 0 or NO2 < 0 or SO2 < 0:
            print("\n\nPor favor, digite um valor igual ou maior que zero.\n\n")
            print("\n\n")
        else:
            verify(MP10, MP10_quality)
            verify(MP25, MP25_quality)
            verify(O3, O3_quality)
            verify(CO, CO_quality)
            verify(NO2, NO2_quality)
            verify(SO2, SO2_quality)

            teste = prioridade(quality)[0]
            print('\nQualidade do ar: {} \n\nRiscos a saúde: {}\n'.format(prioridade(quality)[0], prioridade(quality)[1]))
    except:
        print("\nPor favor, digite um valor correto.\n")
