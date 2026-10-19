
# # Declaración de un arreglo (lista) en Python
# numeros = [10, 20, 30, 40, 50]

# # Imprimo el tercer elemento del arreglo (índice 2)
# print(numeros[2])

# # Quiero que el 40 sea 35
# numeros[3] = 35

# print(numeros)

# # Agregar un nuevo elemento al final del arreglo
# numeros.append(60)

# print(numeros)

# # Eliminar el elemento 35 del arreglo
# numeros.remove(35)
# numeros.pop(3)  # También se puede eliminar por índice

# print(numeros)

# frutas = ["manzana", "banana", "cereza", "mango", "melon", "pera"]

# # Eliminar el primer elemento del arreglo
# del frutas[0]
# frutas.remove("banana") # También se puede eliminar por valor

# print(frutas)

# Hicimos un arreglo vacío y le pedimos al usuario que ingrese la cantidad de elementos que desea agregar. Luego, usamos un bucle para solicitar cada elemento y lo agregamos al arreglo. Finalmente, imprimimos el arreglo resultante.

"""arreglo = []

n = int(input("Ingrese la cantidad de elementos que desea agregar al arreglo: "))

for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    arreglo.append(elemento)

print("Arreglo resultante:", arreglo)"""

# Llenar un array sin usar apend solo con un for
# f sirve a para definir el formato de la cadena, y {i + 1} se reemplaza con el valor de i + 1 en cada iteración del bucle.

# n = int(input("Ingrese la cantidad de elementos que desea agregar al arreglo: "))

# se multiplica porque en Python, al multiplicar una lista por un número, se crea una nueva lista con ese número de elementos, todos inicializados con el valor que se encuentra en la lista original. En este caso, estamos creando un arreglo de n elementos inicializados a 0.
# arreglo = [0] * n  # Crear un arreglo de n elementos inicializados a 0

# for i in range(n):
#     dato = int(input(f"Ingrese el elemento {i + 1}: "))
#     arreglo[i] = dato
    
 
# Escribir un programa que retiene un array de 15 elementos con numeros enteros comprendidos entre 0 y 500 (pedir numeros). A continuacion, se mostrara un array "Cincuerizando", segun el siguiente criterio: si el numero que hay en una posicion del arrray es multiplo de 5, se deja igual y si no, se cambia por el siguiente multiplo de 5 que exista a partir de el. Y mostrar el array original y el array "Cincuerizado".
# Arreglo original: [12, 25, 33, 40, 47, 50, 62, 75, 88, 90, 100, 123, 150, 200, 250]
# Arreglo "Cincuerizado": [15, 25, 35, 40, 50, 50, 65, 75, 90, 90, 100, 125, 150, 200, 250]

arreglo = []
for i in range(15):
    while True:
        numero = int(input(f"Ingrese el número {i + 1} (entre 0 y 500): "))
        if 0 <= numero <= 500:
            arreglo.append(numero)
            break
        else:
            print("Número fuera de rango. Intente nuevamente.")

print ("Arreglo original:", arreglo)
print ("Arreglo Cincuerizado:", [num if num % 5 == 0 else num + (5 - num % 5) for num in arreglo])


