'''
Crear un arreglo de 5 filas y 2 columnas rellenados con ceros y otro de las mismas dimensiones rellenados con unos,
realizar la suma y mostrar en pantalla el valor de la suma de arreglos, mostrar también de cada arreglo solo la fila 2 de
forma completa
'''

import numpy as np

# Crear un arreglo de 5 filas y 2 columnas rellenado con ceros
arreglo_zeros = np.zeros((5, 2))

# Crear otro arreglo de 5 filas y 2 columnas rellenado con unos
arreglo_unos = np.ones((5, 2))

# Realizar la suma de los dos arreglos
suma_arreglos = arreglo_zeros + arreglo_unos

# Mostrar en pantalla el valor de la suma de los arreglos
print("Valor de la suma de los arreglos:")
print(suma_arreglos)

# Mostrar en pantalla la fila 2 completa de cada arreglo
print("\nFila 2 del arreglo de ceros:")
print(arreglo_zeros[1])  # Recordemos que en Python se comienza a contar desde 0, por lo que la segunda fila tiene índice 1
print("\nFila 2 del arreglo de unos:")
print(arreglo_unos[1])
