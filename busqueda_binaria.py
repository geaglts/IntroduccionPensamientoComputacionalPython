def busquedaBinaria(objetivo):
    epsilon = 0.0000001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        # print(
        #     f'abs={abs(respuesta**2 - objetivo)}, alto={alto}, bajo={bajo}, respuesta={respuesta}'
        # )
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    return f'La raiz cuadrada de {objetivo} es {respuesta}'