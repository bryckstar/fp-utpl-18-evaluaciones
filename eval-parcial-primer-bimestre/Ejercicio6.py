n = int

n = int(input("Ingresse el numero del mes de un a\u00f1o: \n"))


if n == 2:
    print("El mes", n, "tiene 29 dias\n")
else:
    if n == 4 or n == 6 or n == 9 or n == 11:
        print("El mes", n, "tiene 30 dias\n")
    else:
        if n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
            print("El mes", n, "tiene 31 dias\n")
        else:
            print("Se ha ingresado un numero de mes no valido\n")
