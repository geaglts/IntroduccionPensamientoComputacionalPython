def aproximacionSoluciones(objetivo):
    # Que tan preciso queremos que sea
    # Basicamente epsilon es la precison que queramos que tenga nuestro programa
    # Que tan cerca queremos llegar a la respuesta
    epsilon = 0.01
    # **2 eleva un numero al cuadrado
    # Paso representa que tanto nos vamos a acercar en cada iteracion
    paso = epsilon**2
    respuesta = 0.0

    # Iteracion
    # abs(valor) regresa un valor absoluto
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        # print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        return f'No se encontro la raiz cuadrada del {objetivo}'
    else:
        return f'La raiz cuadrada de {objetivo} es {respuesta}'
