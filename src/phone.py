from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, count_sim):
        super().__init__(name, price, quantity)
        self.__count_sim = count_sim

    @property
    def number_of_sim(self):
        return self.__count_sim

    @number_of_sim.setter
    def number_of_sim(self, count_sim):
        if count_sim > 0:
            self.__count_sim = count_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self):
        return f'{self.__class__.__name__}{self.name, self.price, self.quantity, self.number_of_sim}'

    def __add__(self, other):
        """
        Магический метод операции сложения екземпляров класса, выполняет проверку на принадлежность к классу
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
