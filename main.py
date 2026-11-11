import sys
from math_module import fibonacci, triangular_number

def main():
    if len(sys.argv) != 3:
        print("Использование: python main.py [fib|tri] [число]")
        sys.exit(1)

    command = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except ValueError:
        print("Ошибка: необходимо ввести целое число.")
        sys.exit(1)

    if command == "fib":
        print(f"Число Фибоначчи F({n}) = {fibonacci(n)}")
    elif command == "tri":
        print(f"Треугольное число T({n}) = {triangular_number(n)}")
    else:
        print("Ошибка: команда должна быть fib или tri.")
        sys.exit(1)

if __name__ == "__main__":
    main()