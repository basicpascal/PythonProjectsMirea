# Написать функцию reverser, которая меняет порядок букв в каждом слове заданного
# предложения на противоположный, порядок слов при этом должен сохраниться
#
# Пример:
# reverser("reverse letters") ==> "esrever srettel"


import traceback


def reverser(sentence):
    return ' '.join(list(word[::-1] for word in sentence.split(' ')))  # делит строку на элементы списка с
    # разделителем пробел


# Тесты
try:
    assert reverser("reverse letters") == "esrever srettel"
    assert reverser("A fun little challenge!") == "A nuf elttil !egnellahc"
    assert reverser("  ") == "  "
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
