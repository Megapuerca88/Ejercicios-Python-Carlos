#Condicional multiple y anidada

#elif {else if} - agrega ramas intermedias
#Clasificador de calificaciones

nota = float(input("Calificacion (0-10): "))

if nota < 0 or nota > 10:
    print("Calificacion inválida")
elif nota >=9.0:
    letra = "A - Excelente"
elif nota >=8.0:
    letra = "B - Bien"
elif nota >=7.0:
    letra = "C - Suficiente"
elif nota >=6.0:
    letra = "D - Aprobado mínimo"
else:
    letra = "F - Reprobado"

if 0 <= nota <=10:
    print(f"Nota: {nota:.1f} -> {letra}")

# Agrega  un mensaje que diga cuántos puntos le faltan para subir de letra.
# Por ejemplo, si obtuvo 7.2 (letra C), necesita 0.8 puntos para llegar a la B.

promedio = 10 - nota #Variable que usamos para calcular cuantos puntos

if nota < 0 or nota > 10:
    print("Promedio no valido")
elif nota >= 9.0:
    puntos = "Ya tienes la calificación más alta"
elif nota >= 8.0:
    promedio = 9.0 - nota
    puntos = f"Te faltan {promedio:.1f} para llegar a A"
elif nota >= 7.0:
    promedio = 8.0 - nota
    puntos = f"Te faltan {promedio:.1f} para llegar a B"
elif nota >= 6.0:
    promedio = 7.0 - nota
    puntos = f"Te faltan {promedio:.1f} para llegar a C"
else:
    promedio = 6.0 - nota
    puntos = f"Te faltan {promedio:.1f} para llegar a D"

print(f"Nota: {nota:.1f} -> {puntos}")
#Importante ordenar de mayor a menor, si no, no funciona

#Tu turno: Reescribe el Ejercicio  usando una sola condición
#  con and en lugar del if anidado. Luego compara las dos versiones:
#  ¿cuál da mensajes de error más específicos y por qué? El anidado al ser subramas,
#ya que sus errores pueden ser mas especificos por eso, ademas que alarga mas el
#codigo pero lo vuelve mas unico, una falla en el and afecta todo y es notable.

# - Ejercicio 5: if anidado - sistema de acceso
USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "1234"

usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

if usuario == USUARIO_CORRECTO:
#Solo llegamos aqui si el usuario es correcto
    if contrasena == CONTRASENA_CORRECTA:
        print("Acceso concedido. Bienvenido")
    else:
        print("Usuario correcto pero contraseña iincorrecta")
else:
    print("Usuario no reconocido.")

#Version con AND mas facil y menos especifica, pero igual sirve
USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "1234"

usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
    print("Acceso concedido. Bienvenido")
else:
    print("Usuario o contraseña incorrectos")

#En conclusion se especifica menos pero es un codigo muy facil de leer
#La verdad prefiero el and, menos problemas casi mismo resultado general
