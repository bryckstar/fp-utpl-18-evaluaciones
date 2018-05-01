t1c1 = float
t1c2 = float
t1c3 = float
t2c1 = float
t2c2 = float
t2c3 = float
t1a1 = float
t1a2 = float
t1a3 = float
t2a1 = float
t2a2 = float
t2a3 = float

t1c1 = float(input("Ingrese el valor del cateto 1 del triangulo 1\n"))
t1c2 = float(input("Ingrese el valor del cateto 2 del triangulo 1\n"))
t1c3 = float(input("Ingrese el valor del cateto 3 del triangulo 1\n"))
t2c1 = float(input("Ingrese el valor del cateto 1 del triangulo 2\n"))
t2c2 = float(input("Ingrese el valor del cateto 2 del triangulo 2\n"))
t2c3 = float(input("Ingrese el valor del cateto 2 del triangulo 2\n"))
t1a1 = float(input("Ingrese el valor del angulo 1 del triangulo 1\n"))
t1a2 = float(input("Ingrese el valor del angulo 2 del triangulo 1\n"))
t1a3 = float(input("Ingrese el valor del angulo 3 del triangulo 1\n"))
t2a1 = float(input("Ingrese el valor del angulo 1 del triangulo 2\n"))
t2a2 = float(input("Ingrese el valor del angulo 2 del triangulo 2\n"))
t2a3 = float(input("Ingrese el valor del angulo 3 del triangulo 2\n"))

if (t1c1 or t2c1)and(t1c2 or t2c2)and(t1c3 or t2c3)and(t1a1 or t2a1)and(t1a2 or t2a2)and(t1a3 or t2a3):
    print("Los triangulos son congruentes\n")
else:
    print("Los triangulos no son congruentes\n")
