from src.item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    # Вывел принт чтобы посмотреть наглядно, но не понимаю почему assert выдает ошибку
    assert str(item1) == 'Смартфон'
