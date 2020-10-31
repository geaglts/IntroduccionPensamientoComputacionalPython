def dividir_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista


lista = list(range(11))
divisor = 2

print(dividir_elementos_de_lista(lista, divisor))