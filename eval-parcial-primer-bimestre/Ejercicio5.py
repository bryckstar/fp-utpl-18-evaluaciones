n1 = int
n2 = int
n3 = int
n4 = int
promedio = float
puntuacion = str
mensaje = "Ingrese la nota: "

n1 = int(input(f"{mensaje}1\n"))

n2 = int(input(f"{mensaje}2\n"))

n3 = int(input(f"{mensaje}3\n"))

n4 = int(input(f"{mensaje}4\n"))


promedio = (n1 + n2 + n3 + n4) / 4

if 0 <= promedio <= 69:
    puntuacion = 'D'
else:
    if 70 <= promedio <= 79:
        puntuacion = 'C'
    else:
        if 80 <= promedio <= 89:
            puntuacion = 'B'
        else:
            puntuacion = 'A'


print("El estudiante con el promedio de calificaciones de", promedio, "tiene una puntuacion de", puntuacion)
