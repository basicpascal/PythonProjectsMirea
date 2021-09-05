"""
1) Создать текстовый txt-файл.
2) Вставить туда англоязычную статью из Википедии.
3) Написать функцию со следующим функционалом:
3.1) Прочитать файл построчно, вывести на печать.
3.2) Создать список и добавить туда непустые строки.
3.3) В строках оставить только латинские буквы и пробелы. Прочие символы удалить.
3.4) Объединить список в единую строку. вывести на печать.
3.5) Подсчитать количество вхождений различных слов в тескте. Подсчет вести в словаре.
3.6) Вывести на печать 10 наиболее популярных и наименее популярных слов (“ 1) -- hello -- 15”).
3.7) Заменить наименее популярные слова на “PYTHON”.
3.8) Создать новый txt-файл.
3.9) Записать текст в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов и не делить слова.
"""

from os import read


import codecs


def is_empty(string: str):
    if string == "":
        return True

    only_contains_empty_characters = True
    for character in string:
        if not character in ['\n', ' ', '']:
            only_contains_empty_characters = False

    return only_contains_empty_characters


def wiki_function(filename):
    file = codecs.open(filename, 'r', encoding='utf-8', errors='ignore')

    # 3.1) Прочитать файл построчно, вывести на печать.
    print("#" * 100 + f'\n')
    print("ORIGINAL".center(100) + f'\n')
    print("#" * 100)
    raw_lines = []
    for line in file:
        print(line)
        raw_lines.append(line)

    # 3.2) Создать список и добавить туда непустые строки.
    no_empty_string_lines = []
    for line in raw_lines:
        if not is_empty(line):
            no_empty_string_lines.append(line.rstrip())

    print("#" * 100 + f'\n')
    print("NO EMPTY STRING LINES".center(100) + f'\n')
    print("#" * 100)
    for line in no_empty_string_lines:
        print(line)

    # 3.3) В строках оставить только латинские буквы и пробелы. Прочие символы удалить.
    only_latin_lines = []
    for line in no_empty_string_lines:
        latin_line = ""
        for character in line:
            if character.isascii() and character.isalpha() or character in [' ', f'\n']:
                latin_line += character
            else:
                latin_line += ' '
        if not is_empty(latin_line):
            only_latin_lines.append(latin_line)

    print("#" * 100 + f'\n')
    print("ONLY LATIN CHARACTERS".center(100) + f"\n")
    print("#" * 100)
    for line in only_latin_lines:
        print(repr(line))

    # 3.4) Объединить список в единую строку. вывести на печать.
    combined_lines_to_string = ""
    for line in only_latin_lines:
        combined_lines_to_string += line + f"\n"
    print("#" * 100 + f'\n')
    print("COMBINED LINES TO STRING".center(100) + f'\n')
    print("#" * 100)
    print(combined_lines_to_string)

    # 3.5) Подсчитать количество вхождений различных слов в тескте. Подсчет вести в словаре.
    reading_a_word = False
    word = ""
    words = {}
    for character in combined_lines_to_string:
        if character.isalpha():
            reading_a_word = True
            word += character
        else:
            if reading_a_word:
                try:
                    words[word] += 1
                except KeyError:
                    words[word] = 1
                word = ""
                reading_a_word = False
    print("#" * 100 + f'\n')
    print("AMOUNT OF WORDS".center(100) + f'\n')
    print("#" * 100)
    print(words)

    # 3.6) Вывести на печать 10 наиболее популярных и наименее популярных слов (“ 1) -- hello -- 15”).
    words = sorted(words.items(), key=lambda w: w[1])
    least_popular_words = []
    print("#" * 100 + f'\n')
    print("10 LEAST POPULAR WORDS".center(100) + f'\n')
    print("#" * 100)
    i = 0
    for w in words:
        if i < 10:
            least_popular_words.append(w[0])
            print(w)
            i += 1
        else:
            break
    print(least_popular_words)

    print("#" * 100 + f'\n')
    print("10 MOST POPULAR WORDS".center(100) + f'\n')
    print("#" * 100)
    words = reversed(words)
    i = 0
    for w in words:
        if i < 10:
            print(w)
            i += 1
        else:
            break



    # 3.8) Создать новый txt-файл.
    new_file = open("Python_new.txt", "w")

    # 3.9) Записать текст в файл, разбивая на строки,
    # при этом на каждой строке записывать не более 100 символов
    # и не делить слова.
    words = combined_lines_to_string.split()
    line_to_append = ""
    for word in words:
        if (len(line_to_append) + 1 + len(word)) < 100:  # + 1 because of the ' ' character.
            if not word in least_popular_words:
                line_to_append += word + ' '  # 3.7
            else:
                line_to_append += "PYTHON" + " "
        else:
            line_to_append += f"\n"
            new_file.write(line_to_append)
            line_to_append = word + ' '
    new_file.close()
    return 0


# Вызов функции
wiki_function("wiki.txt")
