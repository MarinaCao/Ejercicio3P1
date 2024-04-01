# Inicializamos la variable suma para almacenar la suma total
suma = 0

# Utilizamos un bucle for para recorrer los primeros 100 números naturales
for i in range(1, 101):
    # Sumamos el número actual al valor acumulado de la suma
    suma += i

# Mostramos el resultado
print("La suma de los primeros 100 números naturales es:", suma)
# Utilizamos la función sum() con una comprensión de lista para calcular la suma de los primeros 100 números naturales
suma = sum(range(1, 101))

# Mostramos el resultado
print("La suma de los primeros 100 números naturales es:", suma)
