#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

def circle_area(radio):
    area = 3.1416 * (radio ** 2)
    #print(f'Un circulo con un radio de {radio} metros tiene un area de {area} metros cuadrados')
    return area

#circle_area(60)

def volume_cilinder(radio, altura):
    volume = (circle_area(radio)) * altura
    print(f"Un cilindro con un radio de {radio} metros y una altura de {altura} metros, posee un volumen de {volume} metros cubicos")
    return volume

volume_cilinder(8, 15)

               