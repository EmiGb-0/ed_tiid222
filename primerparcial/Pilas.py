

pila = []

pila.append("Plato 1")
pila.append("Plato 2")
pila.append("Plato 3")

print("Pila actual:", pila)

cima = pila[-1]  # Obtenemos el último elemento de la pila
print("Cima de la pila:", cima)

ultimo = pila.pop()  # Retiramos el último elemento de la pila
print("Elemento retirado:", ultimo)
print("Pila después de retirar el último elemento:", pila)

