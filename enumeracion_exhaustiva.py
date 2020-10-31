# Raiz cuadrada
# objetivo = int(input("Escoge un numero: "))


def enumeracionExhaustiva(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        # print(respuesta**2)
        respuesta += 1

    if respuesta**2 == objetivo:
        return f'La raiz cuadrada de {objetivo} es {respuesta}'
    else:
        return f'{objetivo} no tiene una raiz cuadrada exacta'