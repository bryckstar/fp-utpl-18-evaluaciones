valor = int
minutos = int
segundos = int
horas = int

valor = int(input("Ingrese el valor en segundos: \n"))

horas = int(valor/3600)

minutos = int((valor-(horas*3600))/60)

segundos = valor-((horas*3600)+(minutos*60))

print(valor, " segundos es igual a", minutos, "minutos y ", segundos, "segundos\n")
