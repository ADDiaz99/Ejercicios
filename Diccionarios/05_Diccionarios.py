#Escribir un programa que almacene el diccionario con los créditos de las 
#asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y 
#después muestre por pantalla los créditos de cada asignatura en el formato 
#<asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de 
#las asignaturas del curso, y <créditos> son sus créditos. Al final debe 
#mostrar también el número total de créditos del curso.

asignaturas = {                                 #Creamos el diccionario con la llave : valor
    'Matematicas' : 6,
    'Fisica' : 4,
    'Quimica' : 5
}

for materia in asignaturas:                                         #por cada materia en el diccionario,
    print(f'{materia} tiene {asignaturas[materia]} creditos')       #print {cada llave} tiene {diccionario[valores sin llave]} 

#por ultimo, hacemos una suma de todos los valores del diccionario "asignaturas"
print(f'Las asignaturas tienen un total de {sum(dict.values(asignaturas))} creditos')   

                                                                                

