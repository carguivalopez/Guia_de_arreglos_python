'''
Crear un arreglo de 10 filas por 3 columnas, con un rango de números desde 20 a 30, mostrar solo las primeras 2 columnas
de la fila 2
'''


import numpy as np

# Crear un rango de números del 20 al 49 con un paso de 1
arreglo = np.arange(20, 50)

# Remodelar el arreglo a 10 filas y 3 columnas
arreglo = arreglo.reshape(10, 3)

# Mostrar los primeros 2 elementos de la fila 2
print(arreglo[1, :2])
