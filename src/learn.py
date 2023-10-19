from src.keyboard import Keyboard


kb = Keyboard('Dark Project KD87A', 9600, 5)

assert str(kb) == "Dark Project KD87A"

assert str(kb.language) == "EN"

kb.change_lang()
assert str(kb.language) == "RU"

# Сделали EN -> RU -> EN
kb.change_lang()
print(str(kb.language))
assert str(kb.language) == "EN"

kb.language = 'CH'
# AttributeError: property 'language' of 'Keyboard' object has no setter
