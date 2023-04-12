## Creamos la clase

class Coche:
    def __init__(self, marca, modelo, aceleracion):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_actual = 0
        self.aceleracion = aceleracion
    
    def acelerar(self, tiempo):
        self.velocidad_actual += self.aceleracion * tiempo
        return self.velocidad_actual
    
    def frenar(self):
        self.velocidad_actual = 0


## Creamos los objetos

coche1 = Coche('Seat', 'Ibiza', 10)
coche2 = Coche('Hyundai', 'I30', 15)

## Probamos los métodos 

print(coche1.acelerar(10))
print(coche2.acelerar(10))
print(coche1.frenar())
print(coche2.frenar())
