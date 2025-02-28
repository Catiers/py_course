class NumberError(Exception):
    def __init__(self, number, message):
        self.number = number
        self.message = message
    def __str__(self):
        return f"NumberError: number: {self.number}, message: {self.message}"

    
class User:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"User name: {self.name}."
    def call(self, number):
        if len(number) < 8:
            raise NumberError(number, "Короткий номер")
        return f"Звоню {number}"

    
user1 = User("Vasia")
try:
    user1.call("1231")
except NumberError as e:
    print(e)
except:
    print("-1")


try:
    user1.call("1212313231")
except NumberError as e:
    print(e)
except:
    print("-1")

'Звоню 1212313231'