filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

if filas != columnas:
    print("Error: la matriz debe ser cuadrada.")

else:
    matriz = []

    print("\nIngrese los elementos de la matriz:")

    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero = int(input(f"Ingrese el elemento [{i}][{j}]: "))
            fila.append(numero)
        matriz.append(fila)

    suma = 0

    for i in range(filas):
        suma = suma + matriz[i][i]

    print("\nMatriz ingresada:")
    for fila in matriz:
        print(fila)

    print("\nSuma de la diagonal principal:", suma)
