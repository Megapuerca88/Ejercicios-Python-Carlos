# Python usa la sangria (espacios al inicio de la 
# linea) para delimitar bloques de codigo.{}, python
#usa 4 espacios por nivel. Esta es la diferecia
#visual mas importabte entre python y otros lenguajes.

#if condicion:
#   instrcuccion1
#else:
#   instruccion2

#Toda estructura de control termina su primera linea
#con dos puntos ":". Los dos puntos le dicen Python:
#el bloque de esta estructura comienza en la siguiente
#linea. Si se omiten, Python genera: SyntaxError:
# expected ':'

#= asignar un valor
#== comparar dos valores igual que
#!= Diferente de
#> Mayor que / >= Mayor o igual que
#< Menor que / <= Menor o igual que
# and Ambas condiciones True / or Al menops una es
# true / Not Negación lógica 

#IF ejecuta un bloque unicamente si la condición es True. Si la condición
#es es False, el bloque se salta por completo y el programa continua.
#Solo tiene una rama posible.

#Si condicion Entonces
#   Instruccion
#FIN SI
    #SI FALSE -> se omite el bloque

nota = 8.5

if nota >= 6.0:
    print("El alumno aprobó")

print("Fin del programa")

#CONDICIONAL DOBLE - IF/ELSE
#EL else garantiza que SIEMPRE se ejecuta algo. Sin
#imporatar la condición es True o False, el programa
#toma uno de los caminos. Nunca quedan caosos sin respuesta.

#Ejercicio 2

CALIFICACION_MINIMA = 7.0

nota = float(input("Ingresa tu calificacion "))

if nota >= CALIFICACION_MINIMA:
    print(f"Aprobado con {nota:.1f} ")
else:
    print(f"Reprobado con {nota:.1f} ")
    faltaron = CALIFICACION_MINIMA - nota
    print(f"Te faltaron {faltaron:.1f} puntos para aprobar")

#Condiciones compuestas: and/or en accion

edad = int(input("Tu edad: "))
tiene_ine = input("¿Tienes INE (si/no): ")

if edad >= 18 and tiene_ine == "si":
    print("puedes votar")
else: 
    print("No puedes votar aún")

#Validaciones de rango con AND or No
calificacion = float(input("Calificacion (0-10) "))
if calificacion <0 or calificacion >10:
    print("Calificacion fuera de rango")
else:
    print(f"calificacion registrada: {calificacion:.1f}")

# Crea una condición que verifique si un año es bisiesto. 
# Un año es bisiesto si es divisible entre 4, Y si es divisible entre 100, 
# también debe ser divisible entre 400. Pista: usa el operador % (módulo).

anio = int(input("Ingresa un año: "))

if (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")
#% Es para el residuo es decir, si divides 4 entre 100 no da, pero entre 4 si
#y entre 400 lo que da que sea un año bisiesto
# #! es diferente de, es como este == pero en vez de compararlos como iguales
#los separa como diferentes