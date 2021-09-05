# Создать список (супермаркет), состоящий из словарей (товары). Словари должны содержать как минимум 5 полей
# (например, номер, наименование, отдел продажи, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# market = [{"id":123456, "product":"coca-cola 0.5", "department": "drinks", ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех товарах;
# – вывода информации о товаре по введенному с клавиатуры номеру;
# – вывода количества товаров, продающихся в определенном отделе;
# – обновлении всей информации о товаре по введенному номеру;
# – удалении товара по номеру.
# Провести тестирование функций.

import traceback

market = [{'id': 1, 'product': 'Coca-Cola', 'importer': 'USA', 'department': 'drinks', 'amount': 50},
          {'id': 2, 'product': 'Borjomi', 'importer': 'Georgia', 'department': 'drinks', 'amount': 20},
          {'id': 32, 'product': 'Doshirak', 'importer': 'South Korea', 'department': 'food', 'amount': 100},
          {'id': 4, 'product': 'Oranges', 'importer': 'Brazil', 'department': 'food', 'amount': 200},
          {'id': 5, 'product': 'Ice-cream', 'importer': 'Switzerland', 'department': 'food', 'amount': 25},
          {'id': 6, 'product': 'Bananas', 'importer': 'Ecuador', 'department': 'food', 'amount': 300},
          {'id': 707, 'product': 'Lays', 'importer': 'USA', 'department': 'food', 'amount': 100},
          {'id': 8, 'product': 'Apple juice', 'importer': 'Poland', 'department': 'drinks', 'amount': 15},
          {'id': 9, 'product': 'Snickers', 'importer': 'USA', 'department': 'food', 'amount': 300},
          {'id': 10, 'product': 'Baikal', 'importer': 'Russia', 'department': 'drinks', 'amount': 50}]


def info_about_all(market):
    print(market)
    return market


def info_about_id(id):
    for elem in market:
        for key, value in elem.items():
            if key == 'id' and value == id:
                print(elem)
                return elem


def amount_of_department(department):
    count = 0
    for elem in market:
        for key, value in elem.items():
            if key == 'department' and value == department:
                count += elem.get('amount')
    print(count)
    return count


def update_info_about_item(id, update_info):
    for elem in market:
        for key, value in elem.items():
            if key == 'id' and value == id:
                elem.update(update_info)
    print(market)
    return market


def remove_item(id):
    for elem in market:
        for key, value in elem.items():
            if key == 'id' and value == id:
                elem.clear()
                break
    print(market)
    return market


try:
    assert info_about_all(market) == market
    assert info_about_id(707) == market[6]
    assert amount_of_department('food') == 1025
    assert update_info_about_item(707, {'amount': 30}) == market
    assert remove_item(10) == market
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
