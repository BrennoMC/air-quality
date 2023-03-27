
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

    for k, v in qualidade.items():
        for v in v:
            if v == poluente:
                quality.append(f'{k}')
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
        elif qualidade == 'Moderada' and prioridade <= 1:
            prioridade = 1
            indice = qualidade
        elif qualidade == 'Ruim' and prioridade <= 2:
            prioridade = 2
            indice = qualidade
        elif qualidade == 'Muito Ruim' and prioridade <= 3:
            prioridade = 3
            indice = qualidade
        elif qualidade == 'Péssima' and prioridade <= 4:
            prioridade = 4
            indice = qualidade

    return indice

print("Insira os parametros abaixo")
MP10 = float(input(" Partículas inaláveis (MP10): "))
MP25 = float(input(" Partículas inaláveis finas (MP2,5): "))
O3 = float(input(" Ozônio (O3): "))
CO = float(input(" Monóxido de carbono (CO2): "))
NO2 = float(input(" Dióxido de nitrogênio (NO2): "))
SO2 = float(input(" Dióxido de enxofre (SO2): "))

verify(MP10, MP10_quality)
verify(MP25, MP25_quality)
verify(O3, O3_quality)
verify(CO, CO_quality)
verify(NO2, NO2_quality)
verify(SO2, SO2_quality)

print(quality)
print(prioridade(quality))

        
