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

mayor = matriz[0][0]

posicion_fila = 0
posicion_columna = 0

for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            posicion_fila = i
            posicion_columna = j

print("\nMatriz ingresada:")
for fila in matriz:
    print(fila)

print("\nValor máximo:", mayor)
print("Posición: fila", posicion_fila + 1,
      ", columna", posicion_columna + 1)
