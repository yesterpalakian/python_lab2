# Напишите программу, демонстрирующую работу try\except\finally.

try:
     x = int(input("Введите целое число: "))
     y = int(input("Введите целое число: "))
     print(x, y)
     result = x / y
except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")
except TypeError:
        print("Ошибка: Неверный тип данных для деления!")
else:
        print(f"Результат деления {x} на {y} равен {result}")
finally:
        print("Завершение программы")