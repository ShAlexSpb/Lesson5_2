class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, new_name):
        self._name = new_name

    def info(self):
        print(f"User ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level}")



class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._users = []

    def add_user(self, user):
        for usr in self._users:
            if usr.get_user_id() == user.get_user_id():
                print(f"Пользватель {user.get_name()}  уже есть.")
                return 1
        self._users.append(user)
        print(f"Пользватель {user.get_name()} добавлен успешно.")
        return 0

    def remove_user(self, user_id):
        for i, user in enumerate(self._users):
            if user.get_user_id() == user_id:
                self._users.pop(i)
                print(f"Пользователь ID {user_id} успешно удален.")
                return 0
        print(f"Пользователь ID {user_id} не найден.")
        return 1

    # Вывод списка пользователей
    def list_users(self):
        for user in self._users:
            print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Доступ: {user.get_access_level()}")

    def info(self):
        print(f"Администратор ID: {self._user_id}, Имя: {self._name}, Доступ: {self._access_level}")


# Создание экземпляра администратора
admin = Admin(user_id = 1, name = "Евгений")

# Создание нескольких пользователей
user1 = User(user_id = 2, name = "Дмитрий")
user2 = User(user_id = 3, name ="Катерина")
user3 = User(user_id = 4, name ="Анастасия")

# Администратор добавляет пользователей
admin.add_user(user1)  # Должно вывести, что пользователь добавлен успешно
admin.add_user(user2)  # Должно вывести, что пользователь добавлен успешно
admin.add_user(user3)  # Должно вывести, что пользователь добавлен успешно

# Попытка добавить пользователя, который уже существует
admin.add_user(user2)  # Должно вывести, что пользователь уже существует


# Вывод списка всех пользователей
print("Текущий список:")
admin.list_users()

# Удаление одного из пользователей
admin.remove_user(3)  # Должно вывести, что пользователь удален успешно

# Вывод списка всех пользователей после удаления
print("Список обновленный:")
admin.list_users()

# Вывод информации об администраторе
admin.info()