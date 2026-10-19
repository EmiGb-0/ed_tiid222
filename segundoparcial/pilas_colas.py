
# Ejercicios 1 y 2: Colas y Pilas

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1. Colas")
    print("2. Pilas")
    print("3. Salir")

    seleccion = input("Selecciona una opcion: ")

    if seleccion == "1":
        cola = []

        while True:
            print("\n--- MENU DE COLAS ---")
            print("1. Insertar cola")
            print("2. Borrar en cola")
            print("3. Listar cola")
            print("4. Salir")

            opcion = input("Selecciona una opcion: ")

            if opcion == "1":
                try:
                    numero = int(input("Ingresa un numero: "))
                    cola.append(numero)
                    print("Numero agregado correctamente")
                except ValueError:
                    print("Debes ingresar un numero entero")

            elif opcion == "2":
                if len(cola) > 0:
                    eliminado = cola.pop(0)
                    print("Numero eliminado:", eliminado)
                else:
                    print("La cola esta vacia")

            elif opcion == "3":
                if len(cola) > 0:
                    print("Elementos de la cola:")
                    for numero in cola:
                        print(numero)
                else:
                    print("La cola esta vacia")

            elif opcion == "4":
                print("Saliendo del menu de colas...")
                break

            else:
                print("Opcion no valida")

    elif seleccion == "2":
        pila = []

        while True:
            print("\n--- MENU DE PILAS ---")
            print("1. Insertar pila")
            print("2. Borrar en pila")
            print("3. Listar pila")
            print("4. Salir")

            opcion = input("Selecciona una opcion: ")

            if opcion == "1":
                try:
                    numero = int(input("Ingresa un numero: "))
                    pila.append(numero)
                    print("Numero agregado correctamente")
                except ValueError:
                    print("Debes ingresar un numero entero")

            elif opcion == "2":
                if len(pila) > 0:
                    eliminado = pila.pop()
                    print("Numero eliminado:", eliminado)
                else:
                    print("La pila esta vacia")

            elif opcion == "3":
                if len(pila) > 0:
                    print("Elementos de la pila:")
                    for numero in pila:
                        print(numero)
                else:
                    print("La pila esta vacia")

            elif opcion == "4":
                print("Saliendo del menu de pilas...")
                break

            else:
                print("Opcion no valida")

    elif seleccion == "3":
        print("\nPrograma finalizado")
        break

    else:
        print("Opcion no valida")
        continue

    repetir = input("\nDeseas ejecutar nuevamente? (s/n): ")

    if repetir.lower() != "s":
        print("Programa finalizado")
        break
