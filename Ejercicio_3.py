'''
Crear un arreglo multidimensional de 3 x 3 con los números pares desde 1 a 100
'''

import numpy as np

# Creamos un arreglo multidimensional de 3x3 lleno de ceros
arreglo = np.zeros((3, 3), dtype=int)

# Contador para rastrear el número par que estamos insertando
numero_par = 2

# Llenamos el arreglo con números pares del 2 al 100
for i in range(3):
    for j in range(3):
        arreglo[i][j] = numero_par
        numero_par += 2

# Imprimimos el arreglo resultante
print(arreglo)
