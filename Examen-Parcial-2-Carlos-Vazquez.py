contador_ventas = 0 
contador_ventas += 1 #Ponerle + 1 para que identifique a la hora de escribirle
print(f"Venta {contador_ventas}") #Con este refleja el mensaje varias veces
# Asi te evuitas escribirlo tantas veces

c = int(input("¿Cuantos clientes va a registrar?"))

mayor_precio = -1

comi_1 = 0.3 #Los multiplique por o.3 por que es como multiplicarlo por 3%
comi_2 = 0.5
comi_3 = 0.8
comi_4 = 0.12

suma = 0 #mas de lo mismo se asigna en 0 y asi la variable se puede modificar

for i in range(c):
    nombre = input("Nombre: ")
    monto = int(input("Monto de la venta "))

    suma += monto

    if monto > mayor_precio:
        mayor_precio = monto

    if monto >= 1 and monto <= 499: #respetamos los avlores que nos pusieron
        comision = monto * comi_1
        estado = comi_1

    elif monto >= 500 and monto <= 1999: #asi tenemos un limite claro
        comision = monto * comi_2
        estado = comi_2

    elif monto >= 2000 and monto <= 4999:
        comision = monto * comi_3
        estado = comi_3

    elif monto >= 5000 and monto <= 100000: #Le puse un limite alto como referencia
        #Y asi no marque error porque con -1 no srivio
        comision = monto * comi_4
        estado = comi_4

    else:
        estado = "Monto no válido" #Si agregas 0, o cualquier tonteria que no sea
        #valida el progrma te enviara este mensaje

    print(nombre, monto, "Comisión:", comision)

print("Total vendido:", suma)
print("Mayor venta:", mayor_precio)

#No se acabo al completo pero al menos corre y casi un poc mas y casi

