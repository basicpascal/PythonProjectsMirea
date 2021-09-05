import Client as c
import Trainer as t


class Gym:
    def __init__(self, address, listOfClients: list = [], listOfTrainers: list = []):
        self.address = address
        self.listOfClients = listOfClients
        self.listOfTrainers = listOfTrainers

    def __str__(self):
        result = [self.address.center(20, '-')]
        result += [str(client) for client in self.listOfClients]
        result += [str(trainer) for trainer in self.listOfTrainers]
        return f"\n".join(result)

    def __len__(self):
        return len(self.listOfTrainers)

    def __getitem__(self, key):
        return self.listOfTrainers[key]

    def __setitem__(self, key, value):
        if type(value) is t.Trainer:
            self.listOfTrainers[key] = value
        else:
            raise TypeError("Нельзя добавить такой тип: {}".format(type(value)))

    def __add__(self, value):
        if type(value) is c.Client:
            self.listOfClients.append(value)
            return
        raise TypeError("Нельзя добавить такой тип: {}".format(type(value)))

    def __sub__(self, value):
        if type(value) is c.Client:
            self.listOfClients.remove(value)
            return
        raise TypeError("Нельзя добавить такой тип: {}".format(type(value)))

    def create_info_file(self):
        info_file = open("gym_info.txt", "w+")
        info_file.write("\"{}\" GYM".center(20, '-').format(self.address) + f"\n")
        info_file.write("CLIENTS".center(20, '-') + f"\n")
        for client in self.listOfClients:
            info_file.write(str(client) + f"\n")
        info_file.write("TRAINERS".center(20, '-') + f"\n")
        for trainer in self.listOfTrainers:
            info_file.write(str(trainer) + f"\n")

