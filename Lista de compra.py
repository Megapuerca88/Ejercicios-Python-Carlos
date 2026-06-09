#Programa de compras 
nombre = input('Como te llamas? ')
producto = input('Que va a comprar? ')
precio = input('Precio estipulado en el mercado? ')
cuantos = input('Cuantos va a llevar? ')
cliente = 'Cliente ' + nombre
print(cliente)
print(producto)
costo = (float(precio))
mensaje = int(precio) * int(cuantos) #Se cambia a Int para poder sumar
print(costo)
subtotal = "El subtotal es " + str(mensaje) #Se cambia a STR para poder funcionar
print(subtotal)

#Constantes 
print('-------------------------------')
IVA = 0.16
DESCUENTO = 0.10
subtotalere = float(mensaje)# Llleva float porque para precios es mas facil usarlo
real = subtotalere * IVA
iva_real = 'El IVA estipulado es de ' + str(real)
print(iva_real)
oferta = subtotalere - subtotalere * DESCUENTO 
oferton = 'Precio con descuento '+ str(oferta)
print(oferton)
total = oferta - real
total_real = 'El total con el IVA y descuento es ' + str(total)
print(total)

print('-------------------------------')
costo_me = 'La variable de costo es float'
print(costo_me)
print(type(costo))
mensaje_me = 'La variable de mensaje es int'
print(mensaje_me)
print(type(mensaje))
cuantos_me = 'La variable de cuantos es str'
print(cuantos_me)
print(type(cuantos))

#Ticket
Ticket = 'Ticket de compra'
print('-------------------------------')
print('-------------------------------')
print(Ticket)
print('-------------------------------')
print(cliente)
print(producto)
print(costo)
print(subtotal)
politica = 'IVA y descuento'
print('-------------------------------')
print(politica)
print(iva_real)
print(oferton)
print(total_real)
print('-------------------------------')
print('Tipos de datos usados')
print(costo_me)
print(type(costo))
print(mensaje_me)
print(type(mensaje))
print(cuantos_me)
print(type(cuantos))
print('-------------------------------')
print('-------------------------------')
despedida = 'Gracias por su compra'
print(despedida)