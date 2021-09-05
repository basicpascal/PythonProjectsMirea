# Написать функцию кодирования encode(message, key)
# Процесс шифрования: каждой букве латинского алфавита abcdefghijklmnopqrstuvwxyz
# последовательно ставится в соответствие число от 1 до 26.
# Дальше к каждому числу последовательно прибавляется цифры из ключа.
#
# Пример:
# слово: abcxyz, код: 4567 =>
# [a->1, b->2, c->3, x->24, y->25, z->26] =>
# [1 + 4, 2 + 5, 3 + 6, 24 + 7, 25 + 4, 26 + 5] => код: [5, 7, 8, 31, 29, 31]


import traceback
import itertools


def encode(message, key):
    # Тело функции
    vocabulary = list(enumerate("abcdefghijklmnopqrstuvwxyz"))  # латинский алфавит преобразовываем в список кортежей

    vocabulary = dict((y, x + 1) for x, y in vocabulary)  # прибавляем индекс

    message = [vocabulary[letter] for letter in message]  # преобразовываем message в код по алфавиту

    key = str(key)  # ключ преобразовываем в строку
    key = [int(digit) for digit in key]  # а здесь преобразовываем в список целых чисел

    for i in range(len(message)):
        message[i] += key[i % len(key)]  # к каждому элементу списка message прибавляем элемент ключа поочередно

    return message


# Тесты
try:
    assert encode("scout", 1939) == [20, 12, 18, 30, 21]
    assert encode("masterpiece", 1939) == [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
