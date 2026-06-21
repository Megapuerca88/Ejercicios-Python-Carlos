#Ciclo FOR //Repite un bloque para cada elemento de una secuencia.
#Se usa cuando sabes de antemano cuantas veces repetir o cuando 
#quieres recorrer los elementos de una lista, rango o cadena.

#Ejercicio: Variante de range()
print("range(5)")
for i in range(5):
    print(i, end=" ") #0 1 2 3 4
print()

#range(Inicio, fin) - desde inicio hasta fin
print("range(1,6):")
for i in range(1, 6):
    print(1, 6)
    print(i, end= " ")
print()

#range(Inicio, fin) - paso personalizado
print("pares del 0 al 10:")
for i in range(0, 11, 2):
    print(i, end= "")
print()

#Cuenta regresiva con paso negativo
print("Cuenta regresiva")
for i in range(5, 0, -1):
    print(i, end= " ")
print("¡Despegue")

#Tu turno: Escribe un for que imprima solo los múltiplos de 3 entre 3 y 
# 30 usando range() con los argumentos correctos.
#  No uses if dentro del for para filtrar — usa el paso de range().

print("multiplos del 3 al 30:")
for i in range(0, 31, 3):
    print(i, end= " ")
print("De tres en tres")
#Sencillo pones una sucesion en range el primero indica el inicio, el siguinete la
#cantidad de sucesion y el tercero el final de esta



calificaciones = [8.5, 9.0, 6.5, 10.0, 7.5, 5.0, 8.0,]

print("Calficaciones del grupo:")
for calificacion in calificaciones:
    print(f" {calificacion:.1f}")

total = 0
aprobados = 0

max_cal = calificaciones[0]
min_cal = calificaciones[0]

for calificacion in calificaciones:
    total = total + calificacion
    if calificacion >= 6.0:
        aprobados = aprobados + 1
    if calificacion> max_cal:
        max_cal = calificacion
    if calificacion< min_cal:
        min_cal = calificacion

promedio = total / len(calificaciones)
reprobados = len(calificaciones) - aprobados

print(f"\nPromedio del grupo: {promedio:.2f}")
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")

#Turno: encuentra e imprime la calificación más alta y la más baja.
#  Necesitarás dos variables que guarden el máximo
#  y el mínimo mientras recorres la lista.

print(f"Calificacion mas alta: {max_cal}")
print(f"Calificacion mas baja: {min_cal}")

#El cambio aqui es la creacion de ambas variables a las que se les da el valor 0,
#ponemos nombres identificables, tambien lo incluimos en la parte de for 
#y al final en el print con el mensaje que queremos

#-----------------------------
#Ejercicio for con enumerate(): Indica y valor juntos.
#emumerate() te da la posicion y el valor en cada iteracion. Muy
#util para reportes enumerados

alumnos = ["Iran", "Povedano", "Gisel", "Susana", "Zeus", "Carlos", "Sulub"]
notas = [9.0, 7.5, 8.0, 9.5, 6.0, 10.0, 9.8]

#Encabezado en la tabla
print(f"{'No':<5} {'Alumno':<12} {'Nota' :>6} {'Estado' :<10}")
print("-"*37)

for i, alumno in enumerate(alumnos):
    nota = notas[1]
    estado = "Aprobado" if nota >= 7.0 else "reprobado"
    print(f"{i+1:<5} {alumno:<12} {nota:>6.1f} {estado:<10}")
