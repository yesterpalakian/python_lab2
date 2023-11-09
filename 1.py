# Написать функцию для вычисления факториала числа.
def factorial(f):
    if f == 0:
        return 1
    else:
        return f * factorial(f - 1)


n = int(input("Введите число:"))
result = factorial(n)
print(f"Факториал числа {n} равен {result}")
