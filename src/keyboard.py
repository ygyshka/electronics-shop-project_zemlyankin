from src.item import Item


class ChangeLang:

    def __init__(self):
        self.__language1 = 'EN'

    @property
    def language(self):
        return self.__language1

    def change_lang(self):
        if self.__language1 == 'EN':
            self.__language1 = 'RU'
        else:
            self.__language1 = 'EN'
        return self


class Keyboard(Item, ChangeLang):
    def change_lang(self):
        pass


