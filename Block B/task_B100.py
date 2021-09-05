# Написать функцию word_mesh, которая получает список строк и возвращает объединенную строку. 
# Слова в списке должны соединяться вместе, где одна или несколько букв в конце одного слова являются началом следующего слова в списке. 
# Но бывают случаи, когда все слова не совпадают. 
# Вернуть объединенную строку или "failed", если это невозможно.
#
# Примеры:
# word_mesh(["allow", "lowering", "ringmaster", "terror"]) ==> "lowringter" --> "low" + "ring" + "ter"

import traceback


def word_mesh(words: list):
    result = ""
    possible_mesh = ""
    found_mesh = False
    for word in range(0, len(words)-1):
        for i in range(0, len(words[word])):
            first_word = words[word][i:]
            for letter in range(0, min(len(first_word), len(words[word+1]))):
                if first_word[letter] == words[word+1][letter]:
                    found_mesh = True
                    possible_mesh += first_word[letter]
                else:
                    found_mesh = False
                    possible_mesh = ""
                    if letter == min(len(first_word), len(words[word + 1])) - 1:
                        return "failed"
                    break
            if found_mesh:
                result += possible_mesh
                possible_mesh = ""
                break
    return result


# Тесты
try:
    assert word_mesh(["beacon", "condominium", "umbilical", "california"]) == "conumcal"
    assert word_mesh(["abcdef", "defghi", "xyz"]) == "failed"
    assert word_mesh(["allow", "lowering", "ringmaster", "terror"]) == "lowringter"
    assert word_mesh(["abandon", "donation", "onion", "ongoing"]) == "dononon"
    assert word_mesh(
        ["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"]) == "ownhippuscartpher"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
