numeros = input("Introduce una lista de números separados por comas: ").split(",")
numeros = [int(num) for num in numeros]

# Obtener el número más grande y el más pequeño
maximo = max(numeros)
minimo = min(numeros)

# Sumar los números y calcular la media
suma = sum(numeros)
media = suma / len(numeros)

# Obtener una lista con los números únicos
unicos = list(set(numeros))

# Crear un diccionario con los números únicos y su frecuencia
frecuencias = {}
for num in numeros:
    if num not in frecuencias:
        frecuencias[num] = 1
    else:
        frecuencias[num] += 1

# Imprimir los resultados
print("Número más grande:", maximo)
print("Número más pequeño:", minimo)
print("Suma de los números:", suma)
print("Media de los números:", media)
print("Números únicos:", unicos)
print("Frecuencias:", frecuencias)