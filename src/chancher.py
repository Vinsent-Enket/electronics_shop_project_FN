class Changer:
    def __init__(self):
        super().__init__()
        self.__language = "EN"

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"

    @property
    def language(self):
        return f"{self.__language}"

    @language.setter
    def language(self, other):
        raise AttributeError("ты шо, сдурел? держи - property 'language' of 'Keyboard' object has no setter")
