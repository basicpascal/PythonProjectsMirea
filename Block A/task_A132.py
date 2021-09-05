# Написать функцию special_number(number), которая определяет является ли число особенным.
# Назовем число особенным, если сумма цифр числа, возведенных в степень, равную позиции цифры, равна самому числу.
#
# Примеры:
# special_number(89) => True -> 8^1 + 9^2 = 8 + 81 = 89

import traceback


def special_number(number):
    # Тело функции
    n = number
    i = len(str(abs(n)))
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit ** i
        n = n // 10
        i -= 1
    return sum == number


# Тесты
try:
    assert special_number(1) == True
    assert special_number(2) == True
    assert special_number(89) == True
    assert special_number(77) == False
    assert special_number(518) == True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
