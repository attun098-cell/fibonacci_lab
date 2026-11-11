def fibonacci(n):
    """Вычисление n-го числа Фибоначчи."""
    if n < 0:
        raise ValueError("Число должно быть неотрицательным")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def triangular_number(n):
    """Вычисление n-го треугольного числа: T(n) = n*(n+1)/2."""
    if n < 0:
        raise ValueError("Число должно быть неотрицательным")
    return n * (n + 1) // 2