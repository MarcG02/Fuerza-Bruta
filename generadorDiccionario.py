from itertools import product
import string

# Define el número de caracteres que deseas en cada combinación
num_caracteres = 4  # Cambia este valor según lo necesites

# Crea las combinaciones posibles de caracteres de la A a la Z
caracteres = string.ascii_uppercase
combinaciones = [''.join(c) for c in product(caracteres, repeat=num_caracteres)]

# Especifica el nombre del fichero donde deseas guardar las combinaciones
nombre_fichero = "combinaciones.txt"

# Escribe las combinaciones en el fichero
with open(nombre_fichero, 'w') as fichero:
    for combinacion in combinaciones:
        fichero.write(combinacion + '\n')

print(f"Generadas {len(combinaciones)} combinaciones en el fichero {nombre_fichero}")
