import Person as p


class Client(p.Person):
    def __init__(self, first_name, last_name, age, ticket_number):
        super(Client, self).__init__(first_name, last_name, age)
        self.ticket_number = ticket_number
        self.training_settings = {}

    def add_setting(self, setting, value):
        self.training_settings[setting] = value

    def get_setting(self, setting):
        try:
            return self.training_settings[setting]
        except KeyError:
            print("Нет такого параметра тренировки")

    def print_settings(self):
        # print(list(self.training_settings.items()))
        for setting in list(self.training_settings.items()):
            print(setting[0])

    def __str__(self):
        s = "Surname: {}, Name: {}\nAge: {}, Ticket number: {}".format(self.last_name, self.first_name, self.age,
                                                                       self.ticket_number)
        return s

# c = Client("Finn","Bradberry",0,112233)
# c.add_setting("Workout", 50)
# c.add_setting("Running", 100)
# c.print_settings()
# print(c)
