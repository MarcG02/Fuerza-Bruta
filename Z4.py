import time
import os

cont = 0
timeout = 5

"""
Este ejercicio tiene tambien el siguiente. (Control de contraseña correcta para letras y encontrar la contraseña por letras en mayusculas)
"""

def almacenar_numero():
    numero = input("Introduce una contraseña de 4 letras: ").upper()
    while len(numero) != 4 or not numero.isalpha():
        print("Error: debes introducir una contraseña de 4 letras.")
        numero = input("Introduce una contraseña de 4 letras: ").upper()
    return numero

def buscar_diccionario(codigo):
    inicio = time.time()
    with open('combinaciones.txt', 'r') as f:
        data = [line.rstrip() for line in f]
        for password in data:
            if codigo == password:
                fin = time.time()
                print(f"Contraseña encontrada en el diccionario {password}")
                print(f"Tiempo tardado: {fin - inicio} segundos")
                break

def main():
    global cont
    global timeout
    opcion = input("Elige una opción (CrearPin, Ataque, Salir): ")
    while opcion != "Salir":
        if opcion == "CrearPin":
            numero = almacenar_numero()
            print(f"Número almacenado: {numero}")
        elif opcion == "Ataque":
            if 'numero' in locals():
                buscar_diccionario(numero)
            else:
                print("Primero debes almacenar un número usando la opcion1.")
        else:
            print("Opción no válida.")
        opcion = input("Elige una opción (CrearPin, Ataque, Salir): ")

if __name__ == "__main__":
    main()