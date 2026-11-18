filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = []

print("\nIngrese los elementos de la matriz:")

for i in range(filas):
    fila = []
    for j in range(columnas):
        numero = float(input(f"Ingrese el elemento [{i}][{j}]: "))
        fila.append(numero)
    matriz.append(fila)

escalar = float(input("\nIngrese el valor escalar: "))

resultado = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        multiplicacion = matriz[i][j] * escalar
        fila.append(multiplicacion)
    resultado.append(fila)

print("\nMatriz original:")
for fila in matriz:
    print(fila)

print("\nMatriz resultante:")
for fila in resultado:
    print(fila)
