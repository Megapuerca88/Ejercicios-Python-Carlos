#Identificadores y variables
#Variables con snake_case


nombre_alumno = 'Juan Dominguez'
edad_alumno = 28
Promedio_final = 9.5

#Constantes con SCREAMING SNAKE CASE
TASA_IVA = 0.16
CALIFICACION_MINIMA = 7.0
PESO_PARCIAL = 0.20
PI = 3.1416
GRAVEDAD_PLANETA = 9.84
CAPACIDAD_MAXIMA_SALON = 25

#Tipado dinamico - La variable cambia de tipo
dato = 100
print(type(dato))
dato = 'cien'
print(type(dato))

#Uso de constantes en un calculo
precio_base = 5000.0
precio_final = precio_base * (1 + TASA_IVA)
print(f'Precio con IVA: ${precio_final:.2f}') #f sirve para unir 
#resultados cuando no es texto simple 

#3 Constantes
PESO_PARCIAL = 0.20
PESO_PROYECTO = 0.40
CALIFICACION_MINIMA = 6.0

Uno = 8
Dos = 8
Tres = 8
Cuatro = 8

Total = Uno + Dos + Tres + Cuatro
respuesta = Total * (1 + PESO_PARCIAL)
Proyecto = Total * (1 + PESO_PROYECTO)
Promedio = (respuesta + Proyecto)/4
print(Promedio)
print("Aprobado" if Promedio >= CALIFICACION_MINIMA
      else "Reprobado")





