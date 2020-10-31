def log(v):
    print(v)


my_tuple = ()
log(type(my_tuple))
my_tuple = (1, "dos", True)
log(my_tuple[2])
my_tuple = (1)
log(type(my_tuple))
my_tuple = (1, )
log(type(my_tuple))

# Suma de tuplas
my_other_tuple = (2, 3, 4)
my_tuple += my_other_tuple
log(my_tuple)

# Desempaquetar tuplas
x, y, z = my_other_tuple
log(f'x={x}, y={y}, z={z}')


# Desempaquetar tuplas
def coordenadas():
    """Retorna una tupla con 2 valores
    returns tupla
    """
    return (3, 4)


coordenada = coordenadas()
x, y = coordenada
log(f'x={x}, y={y}')