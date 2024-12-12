#Escribir una función que calcule el total de una factura tras aplicarle el IVA.
#La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
#y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA,
#deberá aplicar un 21%.

def calcular_iva(precio, tasa_iva):
    iva = precio * (tasa_iva / 100)
    total_a_pagar = precio + iva
    return total_a_pagar

precio = float(input("Ingrese el precio del producto: "))
aplicar_iva = input("Desea ingresar un IVA diferente (sí/no): ").lower()

if aplicar_iva == "sí" or aplicar_iva == "si":
   tasa_iva = float(input("Ingrese la tasa del IVA a aplicar: "))
else:
    tasa_iva = 21


print(f"El precio del producto sin IVA es: {precio}")
print(f"EL precio del proucto con IVA es: {calcular_iva(precio, tasa_iva)}")