class MobilePhone():
    """Класс под функции мобильного телефона."""
    def __init__(self, number):
        self.number = number
        self.Switch = False
    def turn_on(self):
        self.Switch = True
        return f"Mobile phone {self.number} is enabled."
    def turn_off(self):
        self.Switch = False
        return f"Mobile phone {self.number} is turned off."
    def call(self, cally):
        if self.Switch == True:
            return f"Calling {cally}."
        return f"Mobile phone {self.number} is turned off."
