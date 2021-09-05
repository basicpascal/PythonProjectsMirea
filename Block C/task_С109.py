"""
Каждый класс реализовать в отдельном модуле, импортируя их в производные модули.
Создать класс Person с полями имя, фамилия, возраст. Добавить конструктор класса.
Создать производный от Person класс Client. Новые поля: номер билета, параметры тренировок
    (словарь вида параметр: значение). Определить конструктор, с вызовом родительского конструктора.
    Определить функции добавления параметра в журнал тренировок, получения значения по параметру,
    форматированной печати всех параметров. Переопределить метод преобразования в строку для печати
    основной информации (ФИ, возраст, номер билета).
Создать производный от Person класс Trainer. Новые поля: номер удостоверения, должность, расписание
    работы (словарь вида день : время). Определить конструктор, с вызовом родительского конструктора. Определить
    функции изменения, добавления и удаления в расписание. Переопределить метод преобразования
    в строку для печати основной информации (ФИ, возраст, номер удостоверения, должность).
Создать класс Gym. Поля: адрес, список клиентов (список экземпляров класса Client), список тренеров
    (список экземпляров класса Trainer). Определить конструктор. Переопределить метод преобразования в строку для печати
    всей информации о спортзале (с использованием переопределения в классах Client и Trainer). Переопределить
    методы получения количества тренеров функцией len, получения тренеров по индексу, изменения
    по индексу, удаления по индексу. Переопределить операции + и - для добавления или удаления клиента.
    Добавить функцию создания txt-файла и записи всей информации в него (в том числе расписаний тренеров и
    журналов тренировок клиентов).
Предусмотреть хотя бы в 3 местах обработку возможных исключений.
В каждом модуле провести подробное тестирование всех создаваемых объектов и функций.
"""

from Person import Person
from Client import Client
from Trainer import Trainer
from Gym import Gym

# Тестирование модуля Person
print("Тестирование модуля Person".rjust(50, '.'))
person = Person("Ivan", "Petrov", 23)
assert person.first_name == "Ivan"
assert person.last_name == "Petrov"
assert person.age == 23

# Тестирование модуля Client
print("Тестирование модуля Client".rjust(50, '.'))
client = Client("Denis", "Ivanov", 18, 112233)
assert client.first_name == "Denis"
assert client.last_name == "Ivanov"
assert client.age == 18
assert client.ticket_number == 112233
print("Метод add_setting".rjust(40, '.'))
client.add_setting("Running", 100)
client.add_setting("Workout", 50)
print("Метод get_setting".rjust(40, '.'))
client.get_setting("Running")
print("Метод print_settings".rjust(40, '.'))
client.print_settings()
print("Метод __str__".rjust(40, '.'))
print(client)

# Тестирование модуля Trainer
print("Тестирование модуля Trainer".rjust(50, '.'))
trainer = Trainer("Alexander", "Filatov", 28, 131456, "Box Master")
assert trainer.first_name == "Alexander"
assert trainer.last_name == "Filatov"
assert trainer.age == 28
assert trainer.document_number == 131456
assert trainer.work_position == "Box Master"
day = "Friday"
time = "23:00"
print("Метод add_to_schedule".rjust(40, '.'))
trainer.add_to_schedule(day, time)
print("Метод edit_schedule".rjust(40, '.'))
trainer.edit_schedule("Friday", "18:00")
print("Метод remove_schedule".rjust(40, '.'))
trainer.remove_schedule("Friday")
print("Метод __str__".rjust(40, '.'))
print(trainer)

# Тестирование модуля Gym
print("Тестирование модуля Gym".rjust(50, '.'))
clients = [Client("Alex", "Deniskin", 21, 1235436), Client("Mark", "Deniskin", 21, 1235437)]
trainers = [Trainer("Artyom", "Gaechkin", 35, 1234, "Capitan"), Trainer("Joe", "Biden", 78, 1, "President of this gym")]
new_trainer = Trainer("Konstantin", "Dubov", 19, 181716, "Handball Teacher")
gym = Gym("Moscow, Prospekt Vernadskogo", clients, trainers)
print("Метод __str__".rjust(40, '.'))
print(str(gym))
print("Метод __len__".rjust(40, '.'))
print(len(trainers))
print("Метод __getitem__".rjust(40, '.'))
print(gym[0])
print("Метод __setitem__".rjust(40, '.'))
gym[0] = new_trainer
print(gym[0])
print("Метод __add__".rjust(40, '.'))
gym + clients[0]
print("Метод __sub__".rjust(40, '.'))
gym - clients[1]
print("Метод create_info_file".rjust(40, '.'))
gym.create_info_file()
