
# Declaración de un arreglo (lista) en Python
numeros = [10, 20, 30, 40, 50]

# Imprimo el tercer elemento del arreglo (índice 2)
print(numeros[2])

# Quiero que el 40 sea 35
numeros[3] = 35

print(numeros)

# Agregar un nuevo elemento al final del arreglo
numeros.append(60)

print(numeros)

# Eliminar el elemento 35 del arreglo
numeros.remove(35)
numeros.pop(3)  # También se puede eliminar por índice

print(numeros)

frutas = ["manzana", "banana", "cereza", "mango", "melon", "pera"]

# Eliminar el primer elemento del arreglo
del frutas[0]
frutas.remove("banana") # También se puede eliminar por valor

print(frutas)
