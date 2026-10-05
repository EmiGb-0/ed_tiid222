import os
import random
import sys
import time
import msvcrt

sys.stdout.reconfigure(encoding='utf-8')

columnas = 15
serpiente = [(filas // 2, columnas // 2), (filas // 2, columnas // 2 - 1)]
direccion = (0, 1)
comida = None
puntaje = 0


def crear_comida():
	espacios = [
		(fila, columna)
		for fila in range(filas)
		for columna in range(columnas)
		if (fila, columna) not in serpiente
	]
	return random.choice(espacios)


def dibujar():
	os.system('cls')
	tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]

	for fila, columna in serpiente:
		tablero[fila][columna] = 'o'
	cabeza_fila, cabeza_columna = serpiente[0]
	tablero[cabeza_fila][cabeza_columna] = '@'
	fila_comida, columna_comida = comida
	tablero[fila_comida][columna_comida] = '*'

	print('SNAKE | Puntaje:', puntaje)
	print('+' + '-' * (columnas * 2 + 1) + '+')
	for fila in tablero:
		print('| ' + ' '.join(fila) + ' |')
	print('+' + '-' * (columnas * 2 + 1) + '+')
	print('Usa WASD o las flechas. Pulsa Q para salir.')


def leer_direccion():
	global direccion

	if not msvcrt.kbhit():
		return True

	tecla = msvcrt.getch()
	if tecla in (b'q', b'Q'):
		return False
	if tecla in (b'w', b'W') and direccion != (1, 0):
		direccion = (-1, 0)
	elif tecla in (b's', b'S') and direccion != (-1, 0):
		direccion = (1, 0)
	elif tecla in (b'a', b'A') and direccion != (0, 1):
		direccion = (0, -1)
	elif tecla in (b'd', b'D') and direccion != (0, -1):
		direccion = (0, 1)
	elif tecla == b'\xe0':
		flecha = msvcrt.getch()
		direcciones = {
			b'H': (-1, 0),
			b'P': (1, 0),
			b'K': (0, -1),
			b'M': (0, 1),
		}
		nueva_direccion = direcciones.get(flecha)
		if nueva_direccion and nueva_direccion != (-direccion[0], -direccion[1]):
			direccion = nueva_direccion
	return True


def jugar():
	global comida, puntaje

	comida = crear_comida()
	while True:
		if not leer_direccion():
			break
		cabeza_fila, cabeza_columna = serpiente[0]
		nueva_cabeza = (
			cabeza_fila + direccion[0],
			cabeza_columna + direccion[1],
		)

		choca_pared = not (
			0 <= nueva_cabeza[0] < filas and 0 <= nueva_cabeza[1] < columnas
		)
		choca_serpiente = nueva_cabeza in serpiente[:-1]
		if choca_pared or choca_serpiente:
			break

		serpiente.insert(0, nueva_cabeza)
		if nueva_cabeza == comida:
			puntaje += 1
			if len(serpiente) == filas * columnas:
				break
			comida = crear_comida()
		else:
			serpiente.pop()

		dibujar()
		time.sleep(0.2)

	dibujar()
	print('\nJuego terminado. Puntaje final:', puntaje)


if __name__ == '__main__':
	jugar()



