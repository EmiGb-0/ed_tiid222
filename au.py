
# Se crea una lista de números
numeros = [10, 20, 30, 40, 50]

# consultamos el tercer elemento de la lista (índice 2)
print(numeros[2])

# Se modifica el tercer elemento de la lista (índice 2)
numeros[2] = 100

# Mostramos la lista completa después de la modificación
print(numeros)

# Agregamos un nuevo elemento al final de la lista
numeros.append(60)

# Mostramos la lista completa después de agregar un nuevo elemento
print(numeros)

# Agregamos una lista de dos elementos al final de la lista
numeros.append([60, 70])

# Mostramos la lista completa después de agregar una lista
print(numeros)

numeros.append(60)
numeros.append(70)

numeros = [10, 20, 30, 40]

numeros.insert(2, 25)

print(numeros)


numeros = [10, 20, 30, 40]

numeros = numeros + [50]

print(numeros)


numeros = [10, 20, 30]

numeros.extend([40, 50, 60])

print(numeros)

numeros = [10, 20, 30]
otros_numeros = [40, 50, 60]

numeros.extend(otros_numeros)

print(numeros)

numeros = [10, 20, 30]

print(len(numeros))

# ========================================
# EJERCICIO 1 - LISTA DE CALIFICACIONES
# ========================================

print("Ejercicio 1:")
calificaciones = [70, 85, 90, 65]

calificaciones.append(95)
print(calificaciones)

calificaciones.insert(2, 80)
print(calificaciones)

print(calificaciones)

# ========================================
# EJERCICIO 2 - COLORES
# ========================================

print("\nEjercicio 2:")
colores = ["Azul", "Amarillo", "Rosa"]

colores.extend(["Verde", "Morado", "Rojo"])

print(colores)


# ========================================
# EJERCICIO 3 - RETO DE POSICIONES
# ========================================

numeros = [10, 20, 30, 40]

numeros.insert(2, 95)
numeros.extend([50, 67])

print("\nEjercicio 3:")
print(numeros)

print("95:", numeros[2])
print("67:", numeros[6])

print("El número 95 ocupa el índice 2")
print("El número 67 ocupa el índice 6")