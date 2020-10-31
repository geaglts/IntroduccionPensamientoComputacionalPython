def log(v):
    print(v)


# Los diccionarios se crean de la siguiente manera
my_dict = {"Juan": 10, "Maria": 30, "Jose": 17}

# Podemos acceder a un elemento con su llave, y el metodo get
log(my_dict["Juan"])
log(my_dict.get("Juan", 80))
# Si el elemento no existe retorna el valor por defecto
log(my_dict.get("Miguel", 80))

# Eliminar un elemento con el metodo del
del my_dict["Jose"]
log(my_dict)

# Agregar un nuevo elemento
my_dict["Miguel"] = 16
log(my_dict)

# Iterar el diccionario
for llave in my_dict.keys():
    log(f'llave={llave}')

for valor in my_dict.values():
    log(f'valor={valor}')

for llave, valor in my_dict.items():
    log(f'llave={llave}, valor={valor}')

# Ver si un valor esta en mi diccionario
log("Juan" in my_dict)
log("Alberto" in my_dict)