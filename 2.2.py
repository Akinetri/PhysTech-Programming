#Задачка 2
class User():
    def __init__(self, username, role, age, email, country):
        self.username = username
        self.role = role
        self.age = age
        self.email = email
        self.country = country
        self.info = {}

    def set_info(self, username, role, age, email, country):
        self.info = {
            "username": username,
            "role": role,
            "age": age,
            "email": email,
            "country": country
        }
        return f"Информация о пользователе {self.username} обновлена!"

    def user_info(self):
        return f"Имя: {self.username}, Email: {self.email}, Возраст: {self.age}, Роль: {self.role}, Страна: {self.country}"

    def greet_user(self):
        return f"Привяу, {self.username}"


class Admin(User):
    def __init__(self, username, role, age, email, country):
        super().__init__(username, role, age, email, country)
        self.permissions = []

    def add_permissions(self, permission):
        self.permissions.append(permission)
        return f"Разрешение '{permission}' добавлено!"

    def remove_permission(self, permission):
        if permission in self.permissions:
            self.permissions.remove(permission)
            return f"Разрешение '{permission}' удалено."
        return f"Разрешение '{permission}' не найдено."

    def list_permissions(self):
        return f"Разрешения администратора: {', '.join(self.permissions)}"


admin1 = Admin('Nikitka', 'admin', 18, 'obed@gmail.com', 'donbass')
admin1.add_permissions('Просмотр действий пользователя')
admin1.add_permissions('Удаление мусора')
print(admin1.list_permissions())