#PDF 1. Desarrolla individualmente un programa en Python llamado 
# “Sistema de Registro de Calificaciones” para aplicar los temas vistos en clase.

#Una escuela necesita un programa que registre las calificaciones de 15 estudiantes,
#  verifique que cada dato ingresado sea correcto,
#  calcule los resultados del grupo y genere un informe final en pantalla.
print("Ingresa los datos de los 15 alumnos")

CALIFICACION_MINIMA = 6.0 #Cosntante que indica el valor mimimo para aprobar
NUM_ESTUDIANTES = 15

aprobados = 0 #Se pone en 0 porque nosotros mismos ingresaremos los valores
reprobados = 0
suma = 0

# Variables que son las que identifican mayor y menor nota obtenida
mayor_nota = -1 #Se pone -1 porque todas las notas seran mayores que esta
menor_nota = 11 #Es imposible que haya una nota de 11
nombre_mayor = "" #Son solo comillas cuando se imprima el resultado con el nombre
nombre_menor = ""

for i in range(NUM_ESTUDIANTES):
    nombre = input("Nombre: ")
    nota = float(input("Calificación: ")) #Convertimos los datos a float

    suma += nota

    if nota >= CALIFICACION_MINIMA:
        aprobados += 1 #Sirve para que sume 1 despues del numero anterior
        estado = "Aprobado"
    else:
        reprobados += 1
        estado = "Reprobado"#Se usa aca tambien por ser otra variable

    if nota > mayor_nota: #Cuando se obtiene el valor de la nota mayor 
        mayor_nota = nota #Escribira el nombre de la nota mas alta
        nombre_mayor = nombre

    if nota < menor_nota:
        menor_nota = nota
        nombre_menor = nombre

    print(nombre, nota, estado)

promedio = suma / NUM_ESTUDIANTES #El valor total de calificaciones entre 15 
porcentaje = (aprobados / NUM_ESTUDIANTES) * 100 #Se multiplica por 100
#Porque 100 es el porcentaje total que se podria obtener

print("\nResultados")
print("Promedio:", promedio)
print("Aprobados:", aprobados, "| Reprobados:", reprobados)
print("Mejor:", nombre_mayor, mayor_nota)
print("Peor:", nombre_menor, menor_nota)
print("Porcentaje:", porcentaje, "%")
#Se imprimen resultados las de comillas texto y las de naranja variables
#Al final del informe, muestra el nombre y la calificación del estudiante
#  con la puntuación más alta y del estudiante con la puntuación más baja.
#  No uses las funciones max() o min() de Python;
#  encuéntralos tú mismo usando la lógica del programa.  
#2. Calcula e imprime el porcentaje de estudiantes que aprobaron,
#  redondeado a un decimal y seguido del símbolo %.  
#La salida de estas dos mejoras debería verse así: