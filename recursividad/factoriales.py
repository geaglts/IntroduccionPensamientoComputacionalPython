def factorial(n):
    """Obtiene el factorial de n

    param n valor entero mayor a 0
    returns n!
    """
    if n == 1:
        return 1

    return n * factorial(n - 1)


n = int(input("Ingresa un entero: "))
print(factorial(n))
