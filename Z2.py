import time

cont = 0

def almacenar_numero():
    numero = input("Introduce un número de 4 dígitos: ")
    while len(numero) != 4 or not numero.isdigit():
        print("Error: debes introducir un número de 4 dígitos.")
        numero = input("Introduce un número de 4 dígitos: ")
    return numero

def buscar_numero(numero):
    global cont
    inicio = time.time()
    for i in range(10000):
        if cont <= 3:
            if f"{i:04}" == numero:
                fin = time.time()
                print(f"Número encontrado: {numero}")
                print(f"Tiempo tardado: {fin - inicio} segundos")
                cont = 0
                break
            else:
                cont += 1
        else:
            print("Has superado el número de intentos.")
            break

def main():
    global cont
    opcion = input("Elige una opción (CrearPin, Ataque, Salir): ")
    while opcion != "Salir":
        if opcion == "CrearPin":
            numero = almacenar_numero()
            print(f"Número almacenado: {numero}")
        elif opcion == "Ataque":
            if 'numero' in locals():
                buscar_numero(numero)
                if cont >= 3:
                    print("Has sido bloqueado por exceder el número de intentos durante 5 segundos.")
                    time.sleep(5)
            else:
                print("Primero debes almacenar un número usando la opcion1.")
        else:
            print("Opción no válida.")
        opcion = input("Elige una opción (CrearPin, Ataque, Salir): ")
        

if __name__ == "__main__":
    main()