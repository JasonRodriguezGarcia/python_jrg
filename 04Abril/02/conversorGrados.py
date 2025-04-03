# Conversion de temperaturas Convertir la temperatura en Celsius a Fahrenheit y vice versa.
# Preguntar el usuario tanto por la temperatura como la conversion:

print("--------------------------")
print("Conversión de temperaturas")
print("1 - Farearenheith a Celsius")
print("2 - Celsius a Farenheihtgrados")
print("--------------------------")
tipoTemperatura = input("Introduce opción (1/2): ")
dato = int(input("Introduce número:"))

if tipoTemperatura == "1":
    conversion = (dato - 32) * (5/9)
elif tipoTemperatura == "2":
    conversion = dato * (9/5) + 32
else:
    conversion = "opción no válida"

print (f"Resultado final es: {conversion:,.2f}")

# Pruebas unitarias (Unit Tests) Llevar a cabo una prueba unitaria (unit test)

# Prueba	Input	        Output      esperado	Output actual	PASS/FAIL
# 1	        Celsius 31	    Fahrenheit  87.8		87.80               P
# 2     	Celsius 12	    Fahrenheit  53.6		53.60               P
# 3	        Fahrenheit 99	Celsius     37.22		37.22               P
