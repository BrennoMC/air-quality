print("Air quality.")
print("MENU")
while True:
    print("1 - Inserção")
    print("2 - Consulta")
    print("3 - Exclusão")
    print("4 - Sair")

    option = int(input("Digite a opção desejada: "))

    if option == 1:
        print("Insira os parametros abaixo")
        MP10 = float(input(" Partículas inaláveis (MP10): "))
        MP25 = float(input(" Partículas inaláveis finas (MP2,5):  "))
        #FMC = float(input(" Ozônio (O3): "))
        #O3 = float(input(" monóxido de carbono (CO):  "))
        #CO = float(input(" Dióxido de nitrogênio (NO2): "))
        #NO2 = float(input(" Dióxido de enxofre (SO2):  "))
        #SO2 = float(input("Dióxido de enxofre (SO2): "))

        if MP10 <= 50 or MP25 <= 25: #or O3 <= 100 or CO <= 9 or NO2 <= 200 or SO2 <= 20:
            print("\nA qualidade do ar é N1 - Boa\n")
        elif MP10 in range(51, 101) or MP25 in range(26, 51): #or O3 > 100 or CO > 9 or NO2 > 200 or SO2 > 20:
            print("\nA qualidade do ar é N2 - Moderada\n")
        elif MP10 in range(101, 151): #or MP25 <= 75 or O3 <= 160 or CO <= 13 or NO2 <= 320 or SO2 <= 365:
            print("\nA qualidade do ar é N3 - Ruim\n")
        elif MP10 in range(151, 251): #or MP25 <= 125 or O3 <= 200 or CO <= 15 or NO2 <= 1130 or SO2 <= 800:
            print("\nA qualidade do ar é N4 - Muito Ruim\n")
        elif MP10 > 250: #or MP25 > 125 or O3 > 200 or CO > 15 or NO2 > 1130 or SO2 > 800:
            print("\nA qualidade do ar é N5 - Péssima\n")
    
    elif option == 4:
        break
      