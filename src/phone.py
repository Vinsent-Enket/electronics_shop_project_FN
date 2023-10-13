from src.item import Item


class Phone(Item):

    """
    Откровенно говоря не совсем понял принцип super() ибо не приходится
    все равно явно объявлять __name, в то время как прайс и количество явно объяляются
    так же как в Item, но код работает и это наверное главное
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim) -> None:
        super().__init__(name, price, quantity)
        self.__name = name
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __add__(self, other):
        return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        """
        возвращает наименование товара
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """Метод срабатывает при операции присваивания, устанавливая количество сим карт"""
        #по хорошему же стоит так сделать почти к каждому атрибуту?
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            #надеюсь сделал это не зря и это надо было длать и ранее
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
