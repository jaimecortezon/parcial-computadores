def calcular_division(dividendo, divisor):
    if not (isinstance(dividendo, (float, int)) and isinstance(divisor, (float, int))):
        print("Error: ambos argumentos deben ser números (float o int)")
        return 0
    
    if divisor == 0:
        print("Error: no se puede dividir entre cero")
        return None
    
    if not isinstance(dividendo, (float, int)):
        print("Error: el dividendo debe ser un número (float o int)")
        return 1
    if not isinstance(divisor, (float, int)):
        print("Error: el divisor debe ser un número (float o int)")
        return 1
   
    return dividendo / divisor
    
    
    
    
    
    
print(calcular_division(10, 2))      # Devuelve 5.0
print(calcular_division(10, 0))      # Devuelve None y muestra un mensaje de error
print(calcular_division(10, "2"))    # Devuelve 0 y muestra un mensaje de error
print(calcular_division("hola", 2))  # Devuelve 0 y muestra un mensaje de error
print(calcular_division(10.0, 2))    # Devuelve 5.0
print(calcular_division(10, 2.0))    # Devuelve 5.0
print(calcular_division(10.0, 2.0))  # Devuelve 5.0






