# Напишите функцию, которая будет принимать один аргумент.
# Если в функцию передаётся список, найти сумму отрицательных чисел.
# Удалить из списка все повторяющиеся элементы.
# Если множество, посчитать количество слов.
# Число – определить простое, или нет.
# Строка – найти количество гласных и согласных. Определить самое длинное слово.
# Сделать проверку со всеми этими случаями.
def argument(input_arg):
    if isinstance(input_arg, list):
        negative_sum = sum(x for x in input_arg if x < 0)

        obtained_elements = list(set(input_arg))

        return f"Сумма отрицательных чисел: {negative_sum}, Полученные элементы: {obtained_elements}"

    elif isinstance(input_arg, set):
        word_count = len(input_arg)

        return f"Количество слов в множестве: {word_count}"

    elif isinstance(input_arg, int):
        if input_arg > 1:
            for i in range(2, int(input_arg ** 0.5) + 1):
                if input_arg % i == 0:
                    return f"{input_arg} - не простое число"
            return f"{input_arg} - простое число"
        else:
            return f"{input_arg} - не простое число"

    elif isinstance(input_arg, str):
        vowels = sum(1 for char in input_arg if char.lower() in "аеёиоуыэюя")
        consonants = sum(1 for char in input_arg if char.lower() in "бвгджзклмнпрстфхцчшщ")
        words = input_arg.split()
        longest_word = max(words, key=len)

        return f"Гласных: {vowels}, Согласных: {consonants}, Самое длинное слово: {longest_word}"
    else:
        return "Не выполняется"


#Проверка
print(argument([1, 2, 3, -4, -5, 3, 2]))
print(argument({"я", "люблю", "python"}))
print(argument(18))
print(argument("следствие вели"))
