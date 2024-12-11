#Задачка 3
class Building:
    def __init__(self, tob, address):
        self.open = False
        self.type_of_building = tob
        self.address = address
        self.online = False
        self.info = {}

    def set_info(self, opened, online, site, floor, schedule, fio):
        self.info = {
            "site": site,
            "floor": floor,
            "schedule": schedule,
            "fio": fio
        }
        self.online = online
        self.open = opened

    def get_info(self):
        if self.info:
            koctil = list(self.info.values())

            return f"{', '.join(map(str, koctil))}"

        else:
            return "Информация ещё не добавлена"

    def open(self):
        self.open = True
        return f"{self.type_of_building} был открыт!"

    def close(self):
        self.open = False
        return f"{self.type_of_building} был закрыт"

    def is_open(self):
        if self.open == True:
            return f"{self.type_of_building} открыт"
        else:
            return f"{self.type_of_building} закрыт"

    def is_online(self):
        if self.online == True:
            return f"{self.type_of_building} имеет онлайн-формат"
        else:
            return f"{self.type_of_building} не онлайн-формата"
class Restaurant(Building):
    def __init__(self, tob, address):
        super().__init__(tob, address)


restaurant1 = Restaurant("Бомжатник", "ул. Колотушкина")
restaurant1.set_info(True, True, "/akinetri", 3, "11:30-12:00", "nikitushka")
print(restaurant1.get_info())
print(restaurant1.is_online())