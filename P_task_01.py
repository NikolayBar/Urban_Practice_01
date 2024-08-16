class Database:

    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

    def show_base(self):
        for k, v in self.data.items():
            print(k, v)

    def __call__(self, *args, **kwargs):
        self.show_base()


class User:
    """
    Класс пользователя содержащий логин и пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':

    database = Database()
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    conf_pass = input('Повторите пароль: ')
    if password != conf_pass:
        exit()

    user = User(login, password, conf_pass)
    database.add_user(user.username, user.password)

    database()
