vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
contador_vocales = 0

while contador_vocales < 10:
    palabra = input("Introduce una palabra: ")
    if palabra == ".":
        break
    num_vocales = 0
    for letra in palabra:
        if letra in vocales:
            num_vocales += 1
    contador_vocales += num_vocales
    print(f"El número de vocales totales es: {contador_vocales}")