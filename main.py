from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Абстрактный базовый класс для геометрических фигур.

    Атрибуты:
        x_center (float): Х-координата центра фигуры.
        y_center (float): Y-координата центра фигуры.

    Методы:
        area: Абстрактный метод для вычисления площади фигуры.
        get_center_info:  метод для получения информации о центре фигуры.
    """

    def __init__(self, x_center: float, y_center: float):
        """
        Консутрктор фигуры

        :param x_center: центр окружности по оси x
        :param y_center: центр окружности по оси y
        """
        self.x_center = x_center
        self.y_center = y_center

    def get_center_info(self) -> str:
        """
        :return:Возвращает информацию о центре фигуры."""
        return f"({self.x_center}, {self.y_center})"

    @property
    def y_center(self) -> float:
        """:return:Y-координата центра фигуры."""
        return self._y_center

    @property
    def x_center(self) -> float:
        """:return:X-координата центра фигуры."""
        return self._x_center

    @x_center.setter
    def x_center(self, x_center: float):
        """
        :param x_center: Устанавливает X-координату центра фигуры
        :raise TypeError: если тип аргументов неверный выбрасываем TypeError
        """
        if not isinstance(x_center, (int, float)):
            raise TypeError("x_center должен быть числом.")
        self._x_center = x_center

    @y_center.setter
    def y_center(self, y_center: float):
        """
        :param y_center: Устанавливает Y-координату центра фигуры
        :raise TypeError: если тип аргументов неверный выбрасываем TypeError
        """

        if not isinstance(y_center, (int, float)):
            raise TypeError("y_center должен быть числом.")
        self._y_center = y_center

    @abstractmethod
    def area(self) -> float:
        """
        Абстрактный метод
        :return: Возвращает площадь фигуры.
        """
        pass

    def __str__(self) -> str:
        """
        :return: Возвращает строковое представление фигуры.
        """
        return f"Фигура с центром {self.get_center_info()}"

    def __repr__(self) -> str:
        """
         :return: Возвращает 'официальное' строковое представление объекта.
         """
        return f"{self.__class__.__name__}(x_center={self.x_center!r}, y_center={self.y_center!r})"


class Circle(Shape):
    """
    Класс для представления круга.

    Атрибуты:
        radius (float): Радиус круга.

    Методы:
        area: Возвращает площадь круга.
    """

    def __init__(self, x_center: float, y_center: float, radius: float):
        """
        Консутрктор фигуры

        :param x_center: центр окружности по оси x
        :param y_center: центр окружности по оси y
        :param radius: радиус фигуры
        """
        super().__init__(x_center, y_center)
        self.radius = radius

    @property
    def radius(self) -> float:
        """
        :return: Радиус круга.
        """
        return self._radius

    @radius.setter
    def radius(self, radius: float):
        """
        Радиус имеет protected модификатор для обеспечения безопасной модификации
        :param radius: радиус, который необходимо установить
        :raise TypeError: если тип аргументов неверный выбрасываем TypeError
        :raise ValueError: Радиус должен быть больше нуля.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должен быть числом.")
        if radius <= 0:
            raise ValueError("Радиус должен быть больше нуля.")
        self._radius = radius

    def area(self) -> float:
        """
        :return: Возвращает площадь круга.
        """
        return math.pi * self.radius ** 2

    def __str__(self) -> str:
        """
        :return: Возвращает строковое представление круга с информацией о радиусе.
        """
        return f'{super().__str__()} и радиусом {self.radius}'

    def __repr__(self) -> str:
        """
        :return: Возвращает 'официальное' строковое представление круга.
        """
        return f"{self.__class__.__name__}(x_center={self.x_center!r}, y_center={self.y_center!r}, radius={self.radius})"
