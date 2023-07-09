import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    Path = '..\src\items.csv'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.total_price = self.price * self.quantity
        self.all.append(self)

    def __repr__(self):
        """
        Магический метод __repr__ возвращающий информацию экземпляра класса для разработчика
        """

        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Магический метод __str__ возвращающий информацию экземпляра класса для пользователя
        """

        return f"{self.name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, data_str: str):

        name = data_str
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, filename=Path):
        """
        Метод-класса инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        """
        Item.all = []
        with open(filename, newline='', encoding=" Windows-1251") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], float(row['price']), cls.string_to_number(row['quantity']))

    @staticmethod
    def string_to_number(number: str):
        return int(float(number))

    def __add__(self, other):
        """
        Магический метод операции сложения екземпляров классаб
        """
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise TypeError("Экземпляр класса не наследуется")
