#Escribir una función que calcule el área de un círculo y otra que calcule el volumen
#de un cilindro usando la primera función.

#Área de un círculo
print("Área de un circulo")
def calcular_area_circulo(radio):
    pi = 3.14
    area = pi * (radio * radio)
    return area

radio = float(input("Ingrese el radio del círculo: "))

print(f"El área del circulo es: {calcular_area_circulo(radio)}")
print(" ")

#Área de un cilindro
print("Área de un cilindro")
def calcular_area_cilindro(altura, radio):
    pi = 3.14
    area = ((2 * pi) * radio * altura) + ((2 * pi) * (radio * radio))
    return area

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

print(f"El área del cilindro es: {calcular_area_cilindro(altura, radio)}")