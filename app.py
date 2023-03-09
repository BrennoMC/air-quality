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
        particulaInalavel = float(input(" partículas inaláveis (MP10): "))
        particulaInalavelFina = float(input(" Partículas inaláveis finas (MP2,5):  "))
        ozonio = float(input(" Ozônio (O3): "))
        monoxidoDeCarbono = float(input(" monóxido de carbono (CO):  "))
        dioxidoDeNitrogenio = float(input(" Dióxido de nitrogênio (NO2): "))
        dioxidoDeEnxofre = float(input(" Dióxido de enxofre (SO2):  "))
    
    elif option == 4:
        break
      