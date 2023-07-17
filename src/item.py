import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = 'Файл item__bed.csv.csv поврежден'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.message})"

    def __str__(self):
        return f"{self.message}"


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
        super().__init__()
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
    def instantiate_from_csv(cls):
        cls.all = []
        try:
            filename = cls.Path
            with open(filename, newline='', encoding=" Windows-1251") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls.all.append(cls(row['name'], row['price'], cls.string_to_number(row['quantity'])))

        except FileNotFoundError:
            raise FileNotFoundError(f'FileNotFoundError: Отсутствует файл {cls.Path}')
        except (IndexError, KeyError):
            raise InstantiateCSVError(f'Файл {cls.Path} поврежден')

    @staticmethod
    def string_to_number(number: str):
        return int(float(number))

    def __add__(self, other):
        """
        Магический метод операции сложения екземпляров классаб
        """
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
