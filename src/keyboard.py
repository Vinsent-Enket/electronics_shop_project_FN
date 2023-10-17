from src.chancher import Changer
from src.item import Item


class Keyboard(Item, Changer):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

    @property
    def language(self):
        return self.language

    @language.setter
    def language(self, other):
        raise AttributeError("ты шо, сдурел? держи - property 'language' of 'Keyboard' object has no setter")


