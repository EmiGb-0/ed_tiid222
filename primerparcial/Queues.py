# Deque es una libreria que nos permite crear colas y pilas de manera eficiente. Es parte de la librería estándar de Python y se encuentra en el módulo collections.
from collections import deque
import time

# 1. Creamos la cola vacía y es como si fuera una lista, pero con la diferencia de que podemos agregar y quitar elementos de manera más eficiente segun sea el caso,
cola = deque()

# 2. Encolar (enqueue): agregamos elementos al final
# Es append porque se comporta como una lista, agregando al final de la cola o lista
cola.append("Ana")
cola.append("Carlos")
cola.append("Elena")

print("Cola actual:", list(cola))
# Salida: ['Ana', 'Carlos', 'Elena']

time.sleep(2)  # Simulamos un tiempo de espera antes de atender a la siguiente persona

# 3. Desencolar (dequeue): retiramos el primero que llegó (FIFO)
# popleft retira el primer elemento de la cola
atendido = cola.popleft()
print("Se atendió a: ", atendido)
# Salida: Se atendió a: Ana

time.sleep(2)

# 4. Ver al primero de la cola sin sacarlo
print("Siguiente en la fila:", cola[0])

time.sleep(3)

# 5. Estado final de la cola
print("Cola restante:", list(cola))
# Salida: ['Carlos', 'Elena']