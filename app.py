print("Air quality.")
# print("MENU")
# while True:
#     print("1 - Inserção")
#     print("2 - Consulta")
#     print("3 - Exclusão")
#     print("4 - Sair")

#     option = int(input("Digite a opção desejada: "))


qualidadeBoa = False


def qualidadeN1():
    if MP10 in range(0, 50) or MP25 in range(0, 25) or O3 in range(0, 100) or CO in range(0, 9) or NO2 in range(0, 200) or SO2 in range(0, 20):
        qualidadeBoa = True
    return qualidadeBoa
    # print("\nA qualidade do ar é N1 - Boa\n")


def qualidadeN2():
    print("\nA qualidade do ar é N2 - Moderada\n")


def qualidadeN3():
    print("\nA qualidade do ar é N3 - Ruim\n")


def qualidadeN4():
    print("\nA qualidade do ar é N4 - Muito Ruim\n")


def qualidadeN5():
    print("\nA qualidade do ar é N5 - Péssima\n")


qualityN1 = []
qualityN2 = []
qualityN3 = []
qualityN4 = []
qualityN5 = []


def verifyMP10(MP10):
    if MP10 in range(0, 50):
        # só entra se for valor valido
        qualityN1.append(MP10)
    elif MP10 in range(51, 100):
        qualityN2.append(MP10)
    elif MP10 in range(101, 150):
        qualityN3.append(MP10)
    elif MP10 in range(151, 250):
        qualityN4.append(MP10)
    elif MP10 > 250:
        qualityN5.append(MP10)


def verifyMP25(MP25):
    if MP25 in range(0, 25):
        qualityN1.append(MP25)
    elif MP25 in range(26, 50):
        qualityN2.append(MP25)
    elif MP25 in range(51, 75):
        qualityN3.append(MP25)
    elif MP25 in range(76, 125):
        qualityN4.append(MP25)
    elif MP25 > 125:
        qualityN5.append(MP25)


def verifyO3(O3):
    if O3 in range(0, 100):
        qualityN1.append(O3)
    elif O3 in range(101, 130):
        qualityN2.append(O3)
    elif O3 in range(131, 160):
        qualityN3.append(O3)
    elif O3 in range(161, 200):
        qualityN4.append(O3)
    elif O3 > 200:
        qualityN5.append(O3)


def verifyCO(CO):
    if CO in range(0, 9):
        qualityN1.append(CO)
    elif CO in range(10, 11):
        qualityN2.append(CO)
    elif CO in range(12, 13):
        qualityN3.append(CO)
    elif CO in range(14, 15):
        qualityN4.append(CO)
    elif CO > 15:
        qualityN4.append(CO)


def verifyNO2(NO2):
    if NO2 in range(0, 200):
        qualityN1.append(NO2)
    elif NO2 in range(201, 240):
        qualityN2.append(NO2)
    elif NO2 in range(241, 320):
        qualityN3.append(NO2)
    elif NO2 in range(321, 1130):
        qualityN4.append(NO2)
    elif NO2 > 1130:
        qualityN5.append(NO2)


def verifySO2(SO2):
    if SO2 in range(0, 20):
        qualityN1.append(SO2)
    elif SO2 in range(21, 40):
        qualityN2.append(SO2)
    elif SO2 in range(41, 365):
        qualityN3.append(SO2)
    elif SO2 in range(366, 800):
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

if (len(qualityN1)) == 6:
    print("\nA qualidade do ar é N1 - Boa\n")

# chacon@puccampinas.edu.br
