'''
Crear dos arreglo de 3 filas por 3 columnas, con un rango de números desde 1 a 10, realizar la multiplicación de los dos
arreglos
'''

import numpy as np  # Importamos la librería numpy para trabajar con matrices

# Creamos dos matrices de 3x3 con números aleatorios en el rango de 1 a 10
matriz1 = np.random.randint(1, 11, (3, 3))
matriz2 = np.random.randint(1, 11, (3, 3))

print("Matriz 1:")
print(matriz1)
print("\nMatriz 2:")
print(matriz2)

# Realizamos la multiplicación de las dos matrices elemento por elemento
resultado = np.multiply(matriz1, matriz2)

print("\nResultado de la multiplicación:")
print(resultado)
