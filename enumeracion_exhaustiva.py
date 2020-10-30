# Raiz cuadrada

objetivo = int(input("Escoge un numero: "))
respuesta = 0

while respuesta**2 < objetivo:
    print(respuesta**2)
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta')