sueldo = 360.40
ventas = float
porc = float
sueldoT = float

ventas = float(input("Ingrese el valor del las ventas del mes: \n"))

if ventas <= 500:
    porc = (ventas * 5) / 100
else:
    if 500 < ventas <= 1000:
        porc = (ventas * 8) / 100
    else:
        if 1000 < ventas <= 5000:
            porc = (ventas * 10) / 100
        else:
            if ventas > 5000:
                porc = (ventas * 15) / 100

sueldoT = sueldo + porc

print("El sueldo del empelado con ventas de", ventas, "dolares es de: ", sueldoT, "dolares\n")
