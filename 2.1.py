# Задачка 1 (МНЕ КСТАТИ ЛУК СЕГОДНЯ В ГЕНШИНЕ НА ЛИНИ УПАЛ)
class Restaurant():
    def __init__(self, name, cusine):
        self.name = name
        self.cusine = cusine
        self.open = False
        self.rating = []
        self.info = {}

    def set_info(self, schedule, owner, address, website, rating):
        self.info = {
            "schedule": schedule,
            "owner": owner,
            "address": address,
            "website": website,
            "rating": rating
        }

    def get_info(self):
        if self.info:
            return self.info
        else:
            return f"Информация о {self.name} не добавлена"

    def open(self):
        self.open = True
        return f"Ресторан {self.name} открыт"

    def close(self):
        self.open = False
        return f"Ресторан {self.name} закрыт"

    def get_rating(self, rating):
        if 0 <= rating <= 5:
            self.rating.append(rating)
            return f"Оценка {rating} была добавлена"
        else:
            return "Оценка переходит все границы :/"

    def set_rating(self):
        if self.rating:
            average_rating = sum(self.rating) / len(self.rating)
            self.info["rating"] = round(average_rating, 2)
            return f"Новый средний рейтинг: {self.info["rating"]}"
        else:
            return "Оценок нет :("


Restaurant1 = Restaurant('Макшава', "Помойка")
Restaurant2 = Restaurant("Насвай", "Индийская кухня")
Restaurant3 = Restaurant("Фывфыв", "Вкусняшка")

print(Restaurant1.close())
