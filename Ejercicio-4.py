#CICLO WHILE - Repite un bloque MIENTRAS una condicion sea TRUE. Se usa cuando NO
#sabes de antemano cunatas veces necesitas repetir - el número de repetivciones
#depende de lo que ocurra durante la ejecucion

#Regla critica: algo dentro del while DEBE cambiar en cada iteracion para que la
#condicion eventualmente sea False. Sin eso, el ciclo nunca termina.

#Ejercicio - While basico: contador y acumulador.

N = int(input("Suma del 1 hasta: "))
i = 1 #Contador - empieza en 1
suma = 0 #Acumulador - empieza en 0

while i <= N:
    suma = suma + i
    i = i + 1

print(f"suma de 1 a {N}: {suma}")

#Verificacion matematica: N*(N+1)/2
formula = N * (N + 1) /2
print(f"Verificacion con formúla : {formula}")

#Tu turno: Reescribe el ejercicio usando for en lugar de while.


N = int(input("Suma del 1 hasta: "))
suma = 0

for i in range(1, N + 1):
    suma = suma + i

print(f"Suma de 1 a {N}: {suma}")

# verificación
formula = N * (N + 1) / 2
print(f"Verificación con fórmula: {formula}")
# ¿Cuál versión es más natural para este problema?
#La de for es mas natural sabes tu mismo cuantos ciclos vas a repetir
#en el while tu mismo debes controlar la variable i, for es mas sencillo y menos complejo

#Ejercicio - while para verificar entrada: el patron de reintento.

nota = float(input("Calificacion del 0-10: "))

while nota < 0 or nota > 10:
    print("Calificacion invalida. Debe ser entre 0 y 10.")
    nota = float(input("Calificacion (0-10)"))

print(f"Calificacion registrada: {nota:.1f}")
print()

#While True + Break
i = 0
while True:
    edad = int(input("Tu edad(1-80): "))
    if i <= edad <=120:
        break
    print("Edad invalida, intente de nuevo.")

print(f"Edad registrada: {edad}")

#Tu turno: Crea un programa que pida al usuario adivinar un número secreto
#(define tú el número con una constante). Con while,
#sigue pidiendo hasta que lo adivine e imprime cuántos intentos necesitó.

numero_secreto = 7
intentos = 0

while True:
    intento = int(input("Adivina el número: "))
    intentos += 1

    if intento == numero_secreto:
        print(f"¡Correcto! Lo lograste en {intentos} intentos")
        break

#El while true funciona para repetir en ciclos hasta que des con el correcto
#En print añadimos la variable intentos con el que usamos el famoso +1 para
#sume la cantidad empezando desde el 1 hasta que acertemos
