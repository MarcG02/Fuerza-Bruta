import time

def almacenar_numero():
    numero = input("Introduce un número de 4 dígitos: ")
    while len(numero) != 4 or not numero.isdigit():
        print("Error: debes introducir un número de 4 dígitos.")
        numero = input("Introduce un número de 4 dígitos: ")
    return numero

def buscar_numero(numero):
    inicio = time.time()
    for i in range(10000):
        if f"{i:04}" == numero:
            fin = time.time()
            print(f"Número encontrado: {numero}")
            print(f"Tiempo tardado: {fin - inicio} segundos")
            break

def main():
    opcion = input("Elige una opción (CrearPin, Ataque, Salir): ")
    while opcion != "Salir":
        if opcion == "CrearPin":
            numero = almacenar_numero()
            print(f"Número almacenado: {numero}")
        elif opcion == "Ataque":
            if 'numero' in locals():
                buscar_numero(numero)
            else:
                print("Primero debes almacenar un número usando la opcion1.")
        else:
            print("Opción no válida.")

        opcion = input("Elige una opción (CrearPin, Ataque, Salir): ")
    

if __name__ == "__main__":
    main()