#Escribir una función que calcule el total de una factura tras aplicarle el IVA.
#La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
#y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, 
#deberá aplicar un 21%.

#Solucion:

# def factura_iva(valor, iva):


def factura_iva(valor, iva = 21):
    valor_con_iva = valor + ((valor * iva) / 100)
    print(valor_con_iva)
    return valor_con_iva

factura_iva(1000)
factura_iva(1000, 65)

