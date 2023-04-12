vocales = "AEIOU"
contador_vocales = 0

while True:
    palabra = input("Introduce una palabra (o '.' para salir): ")
    
    if palabra == ".":
        print("¡Adiós!")
        break
    
    for letra in palabra:
        if letra.upper() in vocales:
            contador_vocales += 1
    
    print("Número de vocales:", contador_vocales)
    
    if contador_vocales >= 10:
        print("¡Has alcanzado 10 vocales!")
        break





