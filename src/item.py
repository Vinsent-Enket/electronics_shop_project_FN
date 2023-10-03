import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

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
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        """
        возвращает наименование товара
        """
        return f'{self.__name}'

    @name.setter
    def name(self, name):
        """Метод срабатывает при операции присваивания, устанавливая наименование товара"""
        if len(name) >= 10:
            name = name[:10]
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls, path_file):
        cls.all = []
        # немного помучался с кодировкой, так и должно быть)))?
        # на стороннем сайте вбил текст из файла и он подсказал мне кодировку,
        # на маке он пытался воспринять его как utf-8
        with open(path_file, 'r', encoding='WINDOWS-1251') as csvfile:
            file = csv.DictReader(csvfile)
            for line in file:
                Item(line['name'], line['price'], line['quantity'])

    @staticmethod
    def string_to_number(string):
        return int(float(string))
