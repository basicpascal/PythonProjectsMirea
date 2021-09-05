import Person as p


class Trainer(p.Person):
    def __init__(self, first_name, last_name, age, document_number, work_position):
        super(Trainer, self).__init__(first_name, last_name, age)
        self.document_number = document_number
        self.work_position = work_position
        self.work_schedule = {}

    def edit_schedule(self, day, time):
        if not day in self.work_schedule.keys():
            raise KeyError("В расписании еще нет такого дня")
        self.work_schedule[day] = time

    def add_to_schedule(self, day, time):
        if not day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            raise KeyError("Такого дня не существует")
        else:
            self.work_schedule[day] = time

    def remove_schedule(self, day):
        try:
            self.work_schedule.pop(day)
        except KeyError:
            print("В расписании еще нет такого дня")

    def __str__(self):
        s = "Surname: {}, Name: {}\nAge: {}, Document number: {}, Work position: {}".format(self.last_name,
                                                                                           self.first_name, self.age,
                                                                                           self.document_number,
                                                                                           self.work_position)
        return s

