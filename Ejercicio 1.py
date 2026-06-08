#Realizado por: Carlos Antonio Vazquez Gonzalez
#Este es un comentario de una línea

#este es un comentario 
#que ocupa varias líneas

"""
Este es otro ejemplo 
de comentario multilínea
"""
'''
Este es otro ejemplo 
de comentario multilínea
'''

entero = 42 #Numeros enteros (int)
decimal = 3.1416 #Numeros decimales (float)
logico = True #Boolean
nombre = "Juan" #String

print((entero))
print(type(decimal))
print(type(logico))
print(type(nombre))

#Declara variables que alamacene su nombre, apellido materno, apellido paterno, edad y estatura 
nombre = "Carlos"
apellidop = "Vazquez"
apellidom = "Gonzalez"
edad = 18
estatura = 170.65

print((nombre))
print((apellidop))
print((apellidom))
print((edad))
print((estatura))

#List, tuple, set, dict, arrays, range, frozenset, nontype, complex

#String - inmutable
nombreMateria = "Programacion"
print(nombreMateria[0])
print(nombreMateria[-1])
print(nombreMateria[0:6])

#List - mutable
calificaciones = [8.5, 9.0, 7.5, 10.0]
calificaciones.append(9.5) #Pone en ultimo lugar el valor de una lista que ha sido creada
calificaciones[0] = 8.0 #Cambia un valor si lo ubicas si es que te equivocaste
print(calificaciones)

#tuple - inmutable
coordenadas = (19.4326, -99.1322)
print(coordenadas[0])

# dict - clave:valor
alumno = {"Nombre" : 'Bernardo', "Edad" : 18, "Promedio" : 9.4}
print(alumno["Nombre"])
alumno["Promedio"] = 9.9
print (alumno)

#Diccionario propio
Diccionario = {'Nombre' : 'Antonio', 'Edad' : 18, 'MateriaF' : 'Probabilidad y estadistica'}
print(Diccionario['Nombre'])