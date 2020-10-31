def fibonacci(n):
    """Genera la serie de fibonacci de n

    param n cualquier valor entero positivo
    return serie de n
    """

    if n == 0 or n == 1:
        return 1

    return (fibonacci(n - 1) + fibonacci(n - 2))


n = int(input('Ingresa un numero: '))
print(fibonacci(n))
