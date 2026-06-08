# - casting basico
# Implicita: int + float = automaticamente
resultado = 5 + 2.0
print(resultado)
print(type(resultado))

#Emplicita: str a int
texto_numero = '42'
numero_real = int(texto_numero)
print(numero_real + 8)

#Explicita: int a str para concatenar

edad = 28
mensaje = 'Hola soy Juan y mi edad es ' + str(edad)
print(mensaje)

#float a int. No redondea
precio = 9.99
print (int(precio))

numero = 7.35
redondeado = round(numero)
print(redondeado)

# Simularemos input con varibles fijas
dato_usuario = '25'
print(type(dato_usuario))
#print(dato_usuario + 5)

edad_correcta = int(dato_usuario)
print(edad_correcta + 5)

#Patron correcto para entrada de datos:
#edad = int(input('ingresa tu edad '))

#Tarea
nombre = input('Ingresa tu nombre ')
fecha = int(input('Ingresa tu fecha de nacimiento '))
edad = (2026 - fecha)
total = 'Tu nmobre es' + nombre + ' edad es ' + str(edad) #Se le pone STR debido a que la variable cambio
print(total)



