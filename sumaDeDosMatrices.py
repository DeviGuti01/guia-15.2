filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

A = []
B = []

print("\nIngrese los elementos de la matriz A:")

for i in range(filas):
    fila = []
    for j in range(columnas):
        numero = float(input(f"Ingrese el elemento [{i}][{j}]: "))
        fila.append(numero)
    A.append(fila)

print("\nIngrese los elementos de la matriz B:")

for i in range(filas):
    fila = []
    for j in range(columnas):
        numero = float(input(f"Ingrese el elemento [{i}][{j}]: "))
        fila.append(numero)
    B.append(fila)

resultado = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        suma = A[i][j] + B[i][j]
        fila.append(suma)
    resultado.append(fila)

print("\nMatriz A:")
for fila in A:
    print(fila)

print("\nMatriz B:")
for fila in B:
    print(fila)

print("\nMatriz resultante:")
for fila in resultado:
    print(fila)