import doctest


class Circle:
    def __init__(self, x: float, y: float, r: float):
        """
        Создание и подготовка к работе объекта "Стакан"

        :param x: центр окружности по оси x
        :param y: центр окружности по оси y
        :param r: радиус окружности


        Примеры:
        >>> circle = Circle(5, 5, 1)  # инициализация экземпляра класса
        """
        if not isinstance(x, (int, float)):
            raise TypeError("x координата должна быть типа int или float")
        self.x = x
        if not isinstance(y, (int, float)):
            raise TypeError("y координата должна быть типа int или float")
        self.y = y
        if not isinstance(r, (int, float)):
            raise TypeError("радиус окружности должен быть типа int или float")
        if r < 0:
            raise ValueError("Радиус окружности должен быть >= 0")
        self.r = r

    def move(self, x: float, y: float) -> None:
        """
        Перемещение окружности в новую точку

        :param x: Новая x координата
        :param y: Новая y координата
        :raise TypeError: если тип аргументов неверный выбрасываем TypeError
        Примеры:
        >>> circle = Circle(0, 0, 1)
        >>> circle.move(5,5)
        """
        if not isinstance(x, (int, float)):
            raise TypeError("x координата должна быть типа int или float")
        if not isinstance(y, (int, float)):
            raise TypeError("y координата должна быть типа int или float")
        ...

    def getArea(self) -> float:
        """
        :return: Площадь окружности
        Примеры:
        >>> circle = Circle(0, 0, 1)
        >>> circle.getArea()
        """
        ...


class UserAccount:
    def __init__(self, username: str, balance: float):
        """
        Создание и подготовка к работе объекта "UserAccount"

        :param username: Имя пользователя
        :param balance: Баланс пользователя

        Примеры:
        >>> account = UserAccount('JohnDoe', 1000.0)
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть строкой")
        if not username:
            raise ValueError("Имя пользователя не может быть пустым")
        self.username = username

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть числом")
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Пополнение счета пользователя.
        :param amount: Сумма для пополнения

        :raise ValueError: Если сумма пополнения отрицательная, то вызываем ошибку

        Примеры:
        >>> account = UserAccount('JohnDoe', 1000.0)
        >>> account.deposit(500.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount < 0:
            raise ValueError("Сумма пополнения должна быть положительным числом")
        ...

    def withdraw(self, amount: float) -> None:
        """
        Снятие средств со счета пользователя.

        :param amount: Сумма для снятия
        :raise ValueError: Если сумма снятия превышает баланс или отрицательная,
        то возвращается ошибка.

        Примеры:
        >>> account = UserAccount('JohnDoe', 1000.0)
        >>> account.withdraw(500.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount > self.balance or amount < 0:
            raise ValueError("Сумма снятия недействительна")
        ...


class Light:
    def __init__(self, is_on: bool, brightness: int):
        """
        Создание и подготовка к работе объекта "Лампочка"

        :param is_on: Состояние лампочки (включена или выключена)
        :param brightness: Уровень яркости лампочки

        Примеры:
        >>> light = Light(False, 0)  # инициализация экземпляра класса
        """
        if not isinstance(is_on, bool):
            raise TypeError("Состояние лампочки должно быть булевым значением")
        self.is_on = is_on

        if not isinstance(brightness, int) or brightness < 0 or brightness > 100:
            raise ValueError("Уровень яркости должен быть целым числом от 0 до 100")
        self.brightness = brightness

    def toggle(self) -> None:
        """
        Переключение состояния лампочки (вкл/выкл).

        Примеры:
        >>> light = Light(False, 0)
        >>> light.toggle()
        """
        ...

    def set_brightness(self, new_brightness: int) -> None:
        """
        Установка нового уровня яркости лампочки.

        :param new_brightness: Новый уровень яркости

        :raise ValueError: Если уровень яркости выходит за допустимый диапазон

        Примеры:
        >>> light = Light(True, 50)
        >>> light.set_brightness(80)
        """
        if not isinstance(new_brightness, int) or new_brightness < 0 or new_brightness > 100:
            raise ValueError("Уровень яркости должен быть целым числом от 0 до 100")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
