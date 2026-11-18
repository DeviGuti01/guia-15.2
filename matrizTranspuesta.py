filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

matriz = []

print("\nIngrese los elementos de la matriz:")

for i in range(filas):
    fila = []
    for j in range(columnas):
        numero = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        fila.append(numero)
    matriz.append(fila)

transpuesta = []

for j in range(columnas):
    fila = []
    for i in range(filas):
        fila.append(matriz[i][j])
    transpuesta.append(fila)

print("\nMatriz original:")
for fila in matriz:
    print(fila)

print("\nMatriz transpuesta:")
for fila in transpuesta:
    print(fila)