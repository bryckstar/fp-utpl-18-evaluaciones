ancho = float
alto = float
superficie = float

ancho = float(input("Ingrese el valor del ancho de la habitacion en metros: \n"))

alto = float(input("Ingrese el valor de la longitud de la habitacion en metros: \n"))


superficie = alto * ancho

print("El valor de la superficie es de: ", "{0:.3f}".format(superficie), "m\u00B2 \n")
