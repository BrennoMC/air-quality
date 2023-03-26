print("Air quality.")
# print("MENU")
# while True:
#     print("1 - Inserção")
#     print("2 - Consulta")
#     print("3 - Exclusão")
#     print("4 - Sair")

#     option = int(input("Digite a opção desejada: "))

qualityN1 = []
qualityN2 = []
qualityN3 = []
qualityN4 = []
qualityN5 = []


def verifyMP10(MP10):
    if MP10 in range(0, 51):
        # só entra se for valor valido
        qualityN1.append(MP10)
    elif MP10 in range(51, 101):
        qualityN2.append(MP10)
    elif MP10 in range(100, 151):
        qualityN3.append(MP10)
    elif MP10 in range(151, 251):
        qualityN4.append(MP10)
    elif MP10 > 250:
        qualityN5.append(MP10)


def verifyMP25(MP25):
    if MP25 in range(0, 26):
        qualityN1.append(MP25)
    elif MP25 in range(26, 51):
        qualityN2.append(MP25)
    elif MP25 in range(51, 76):
        qualityN3.append(MP25)
    elif MP25 in range(76, 126):
        qualityN4.append(MP25)
    elif MP25 > 125:
        qualityN5.append(MP25)


def verifyO3(O3):
    if O3 in range(0, 101):
        qualityN1.append(O3)
    elif O3 in range(101, 131):
        qualityN2.append(O3)
    elif O3 in range(131, 161):
        qualityN3.append(O3)
    elif O3 in range(161, 201):
        qualityN4.append(O3)
    elif O3 > 200:
        qualityN5.append(O3)


def verifyCO(CO):
    if CO in range(0, 10):
        qualityN1.append(CO)
    elif CO in range(10, 12):
        qualityN2.append(CO)
    elif CO in range(12, 14):
        qualityN3.append(CO)
    elif CO in range(14, 16):
        qualityN4.append(CO)
    elif CO > 15:
        qualityN5.append(CO)


def verifyNO2(NO2):
    if NO2 in range(0, 201):
        qualityN1.append(NO2)
    elif NO2 in range(201, 241):
        qualityN2.append(NO2)
    elif NO2 in range(241, 321):
        qualityN3.append(NO2)
    elif NO2 in range(321, 1131):
        qualityN4.append(NO2)
    elif NO2 > 1130:
        qualityN5.append(NO2)


def verifySO2(SO2):
    if SO2 in range(0, 21):
        qualityN1.append(SO2)
    elif SO2 in range(21, 41):
        qualityN2.append(SO2)
    elif SO2 in range(41, 366):
        qualityN3.append(SO2)
    elif SO2 in range(366, 801):
        qualityN4.append(SO2)
    elif SO2 > 800:
        qualityN5.append(SO2)


valoresDigitados = []
print("Insira os parametros abaixo")
MP10 = float(input(" Partículas inaláveis (MP10): "))
MP25 = float(input(" Partículas inaláveis finas (MP2,5): "))
O3 = float(input(" Ozônio (O3): "))
CO = float(input(" Monóxido de carbono (CO2): "))
NO2 = float(input(" Dióxido de nitrogênio (NO2): "))
SO2 = float(input(" Dióxido de enxofre (SO2): "))

'''
if indice >= 0 and indice <= 40:
    print("\nA qualidade do ar é N1 - Boa\n")
elif indice >= 41 and indice <= 80:
    print("\nA qualidade do ar é N2 - Moderada\n")
elif indice >= 81 and indice <= 120:
    print("\nA qualidade do ar é N3 - Ruim\n")
elif indice >= 121 and indice <= 200:
    print("\nA qualidade do ar é N4 - Muito Ruim\n")
else:
    print("\nA qualidade do ar é N5 - Péssima\n")
'''

verifyMP10(MP10)
verifyMP25(MP25)
verifyO3(O3)
verifyCO(CO)
verifyNO2(NO2)
verifySO2(SO2)
print(qualityN1)
print(qualityN2)
print(qualityN3)
print(qualityN4)
print(qualityN5)

if (len(qualityN5)) >= 1:
    print("\nA qualidade do ar é N5 - Péssima\n")
elif (len(qualityN4) >= 1):
    print("\nA qualidade do ar é N4 - Muito Ruim")
elif (len(qualityN3) >= 1):
    print("\nA qualidade do ar é N3 - Ruim")
elif (len(qualityN2) >= 1):
    print("\nA qualidade do ar é N2 - Moderado")
else:
    print("\nA qualidade do ar é N1 - Boa\n")
    


# chacon@puccampinas.edu.br
