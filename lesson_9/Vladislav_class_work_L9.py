Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Dog:
    pass

class Wallet:
    pass

class Car:
    pass

class User:
    pass

d = Dog()
type(d)
<class '__main__.Dog'>
class God:
    def __int__(self, name, age):
        self.name = name
        self.age = age

        
d = Dog()

d = God()
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
SyntaxError: unexpected indent


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
d = Dog()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d = Dog()
TypeError: Dog.__init__() missing 2 required positional arguments: 'name' and 'age'
d = Dog("Bobik", 12)

class User:
    def __init__(self, name, email)
    
SyntaxError: incomplete input
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        
dima = User("Dima", "diam@gsdg.com")
dima
<__main__.User object at 0x00000232F40D7BD0>
type(dima)
<class '__main__.User'>
isinstance(dima, User)
True
dima.name
'Dima'
dima.email
'diam@gsdg.com'
d.age
12
d.name
'Bobik'
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        
dima = User("Dima", "diam@gsdg.com")
vova = User("Vova", "vova@gsdg.com")
dima.name
'Dima'
vova.name
'Vova'
User.name
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    User.name
AttributeError: type object 'User' has no attribute 'name'
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email

        
User.users_counter
0
User.users_counter = 666
User.users_counter
666
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.users_counter += 1

        
User.users_counter
0
dima = User("di", "2")
User.users_counter
1
vika = User("vi", "2")
User.users_counter
2
dima.name
'di'
User.users_counter
2
vika.users_counter
2
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.users_counter = 1

        
User.users_counter
0
d = User("Di", "2")
User.users_counter
0
d.users_counter
1
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.users_counter += 1

        
d = User("Di", "2")
v = User("Di", "2")
c = User("Di", "2")
User.users_counter
3
c.users_counter
3
c.users_counter = 555
User.users_counter
3
d.users_counter
3
c.users_counter
555
d.mobile = "2123512"
d.mobile
'2123512'
User.jojo = 999
User.jojo
999
d.jojo = 8
c.jojo
999
class Wallet:
    """Представляет структуру полей для описания кошелька."""
    counter = 0
    def __init__(self, owner, currency, amoun, address="", color="silver"):
        self.owner = owner
        self.currency = currency
        self. amount = amount
        self.address = address
        self.color = color
        Wallet.counter += 1
        self.wallet_id = Wallet.counter * 10

        
Wallet.counter
0
fw = Wallet("S F", "BYN", 1000)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    fw = Wallet("S F", "BYN", 1000)
  File "<pyshell#103>", line 7, in __init__
    self. amount = amount
NameError: name 'amount' is not defined. Did you mean: 'amoun'?
class Wallet:
    """Представляет структуру полей для описания кошелька."""
    counter = 0
    def __init__(self, owner, currency, amount, address="", color="silver"):
        self.owner = owner
        self.currency = currency
        self. amount = amount
        self.address = address
        self.color = color
        Wallet.counter += 1
        self.wallet_id = Wallet.counter * 10

        
Wallet.counter
0
fw = Wallet("S F", "BYN", 1000)

Wallet.counter
1
fw.owner
'S F'
fw.currency
'BYN'
fw.wallet_id
10
sw = Wallet("D F", "RUB", 100000, color="Gold!")
Wallet.counter
2
sw.color
'Gold!'
sw.wallet_id
20
Wallet.__doc__
'Представляет структуру полей для описания кошелька.'
Wallet.__name__
'Wallet'
Wallet.__module__
'__main__'
Wallet.__bases__
(<class 'object'>,)
fw.__dict__
{'owner': 'S F', 'currency': 'BYN', 'amount': 1000, 'address': '', 'color': 'silver', 'wallet_id': 10}
sw.__dict__
{'owner': 'D F', 'currency': 'RUB', 'amount': 100000, 'address': '', 'color': 'Gold!', 'wallet_id': 20}
for k, v fw.__dict__.items():
    
SyntaxError: invalid syntax
for k, v sw.__dict__.items():
    
SyntaxError: invalid syntax
for k, v in fw.__dict__.items():
    print(k, ":", v)

    
owner : S F
currency : BYN
amount : 1000
address : 
color : silver
wallet_id : 10
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f"{self.name} says {message}!")

        
di = User("Dima", "@")
di.email
'@'
di.name
'Dima'
di.hello
<bound method User.hello of <__main__.User object at 0x00000232F4123310>>
print
<built-in function print>
di.hello()
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    di.hello()
TypeError: User.hello() missing 1 required positional argument: 'message'
di.hello("Helo there")
Dima says Helo there!
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f"{self.name} says {message}!")
    def bye(self)
    
SyntaxError: incomplete input
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f"{self.name} says {message}!")
    def bye(self):
        print(f"{self.name} says bye bye!")

        
di = User("Dima", "@")
di.hello("asgsdgdf")
Dima says asgsdgdf!
di.bye()
Dima says bye bye!
st = "hello"
print(st)
hello
print(di)
<__main__.User object at 0x00000232F4101C90>
print(di.name)
Dima
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f"{self.name} says {message}!")
    def bye(self):
        print(f"{self.name} says bye bye!")
    def __str__(self):
        return f"User: name-{self.name}, email-{self.email}"

    
kate = User("Kate", "@gdfh.com")
kate.hello("fhgfsd")
Kate says fhgfsd!
kate.bye()
Kate says bye bye!
print(kate)
User: name-Kate, email-@gdfh.com
dir(User)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bye', 'hello']
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f"{self.name} says {message}!")
    def bye(self):
        print(f"{self.name} says bye bye!")
    def __str__(self):
        return f"User: name-{self.name}, email-{self.email}"

    
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
        def add_user(self, user)"
        
SyntaxError: incomplete input
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({counter_id:user})
    def show_all(self):
        for k, v in self.storage.items():
            print(f"user id:{k}")
            print(f"     Name:{user.name}")
            print(f"     Email:{user.email}")
            print("__str__")
            print(user)
            print(user.bye())

            
strg = Storage()
dima = User("Dima", "dfhsdgfh
            
SyntaxError: incomplete input
dima = User("Dima", "dfhsdgfh")
            
kolya = User("Kolya", "dfhsdgfh")
            

vasia = User("Vasia", "fdhsbfdb")
            


strg.add_user(dima)
            
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    strg.add_user(dima)
  File "<pyshell#185>", line 7, in add_user
    self.storage.update({counter_id:user})
NameError: name 'counter_id' is not defined
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({Storage.counter_id:user})
    def show_all(self):
        for k, v in self.storage.items():
            print(f"user id:{k}")
            print(f"     Name:{user.name}")
            print(f"     Email:{user.email}")
            print("__str__")
            print(user)
            print(user.bye())

            
strg = Storage()
dima = User("Dima", "aSgafdg@")
kate = User("Kate", "fhsfdg@")
vasia = User("Vasia", "fdghgdh@")
strg.add_user(dima)
strg.add_user(kate)
strg.add_user(vasia)
strg.show_all()
user id:1
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    strg.show_all()
  File "<pyshell#196>", line 11, in show_all
    print(f"     Name:{user.name}")
NameError: name 'user' is not defined. Did you mean: 'User'?
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({Storage.counter_id:user})
    def show_all(self):
        for iser_id, user in self.storage.items():
            print(f"user id:{k}")
            print(f"     Name:{user.name}")
            print(f"     Email:{user.email}")
            print("__str__")
            print(user)
            print(user.bye())

            
strg = Storage()
dima = User("Dima", "aSgafdg@")

kate = User("Kate", "fhsfdg@")
vasia = User("Vasia", "fdghgdh@")
strg.add_user(dima)
strg.add_user(kate)
strg.add_user(vasia)
strg.show_all()
user id:wallet_id
     Name:Dima
     Email:aSgafdg@
__str__
User: name-Dima, email-aSgafdg@
Dima says bye bye!
None
user id:wallet_id
     Name:Kate
     Email:fhsfdg@
__str__
User: name-Kate, email-fhsfdg@
Kate says bye bye!
None
user id:wallet_id
     Name:Vasia
     Email:fdghgdh@
__str__
User: name-Vasia, email-fdghgdh@
Vasia says bye bye!
None
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({Storage.counter_id:user})
    def show_all(self):
        for user_id, user in self.storage.items():
            print(f"user id:{k}")
            print(f"     Name:{user.name}")
            print(f"     Email:{user.email}")
            print("__str__")
            print(user)
            print(user.bye())

            
strg = Storage()
dima = User("Dima", "aSgafdg@")
kate = User("Kate", "fhsfdg@")
vasia = User("Vasia", "fdghgdh@")
strg.add_user(dima)
strg.add_user(kate)
strg.add_user(vasia)
strg.show_all()
user id:wallet_id
     Name:Dima
     Email:aSgafdg@
__str__
User: name-Dima, email-aSgafdg@
Dima says bye bye!
None
user id:wallet_id
     Name:Kate
     Email:fhsfdg@
__str__
User: name-Kate, email-fhsfdg@
Kate says bye bye!
None
user id:wallet_id
     Name:Vasia
     Email:fdghgdh@
__str__
User: name-Vasia, email-fdghgdh@
Vasia says bye bye!
None
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({Storage.counter_id:user})
    def show_all(self):
        for user_id, user in self.storage.items():
            print(f"user id:{user_id}")
            print(f"     Name:{user.name}")
            print(f"     Email:{user.email}")
            print("__str__")
            print(user)
            print(user.bye())

            
strg = Storage()
dima = User("Dima", "aSgafdg@")
kate = User("Kate", "fhsfdg@")
vasia = User("Vasia", "fdghgdh@")
strg.add_user(dima)
strg.add_user(kate)
strg.add_user(vasia)
strg.show_all()
user id:1
     Name:Dima
     Email:aSgafdg@
__str__
User: name-Dima, email-aSgafdg@
Dima says bye bye!
None
user id:2
     Name:Kate
     Email:fhsfdg@
__str__
User: name-Kate, email-fhsfdg@
Kate says bye bye!
None
user id:3
     Name:Vasia
     Email:fdghgdh@
__str__
User: name-Vasia, email-fdghgdh@
Vasia says bye bye!
None
hatchback
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    hatchback
NameError: name 'hatchback' is not defined
sedan
Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    sedan
NameError: name 'sedan' is not defined
wagon
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    wagon
NameError: name 'wagon' is not defined
c
ar
Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    ar
NameError: name 'ar' is not defined. Did you mean: 'Car'?
class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name
    def __str__(self):
        return "привет из родительского класса"

class Sedan:
    pass

class Wagon:
    pass

Sedan.__bases__
(<class 'object'>,)
s = Sedan()
s
<__main__.Sedan object at 0x00000232F4116210>
class Sedan(Car):
    pass

class Wagon(Car):
    pass

Sedan.__bases__
(<class '__main__.Car'>,)
Wagon.__bases__
(<class '__main__.Car'>,)
s = Sedan()
Traceback (most recent call last):
  File "<pyshell#265>", line 1, in <module>
    s = Sedan()
TypeError: Car.__init__() missing 3 required positional arguments: 'vin', 'volume', and 'model_name'
s = Sedan("124124", 1.4, "Megane")
Traceback (most recent call last):
  File "<pyshell#266>", line 1, in <module>
    s = Sedan("124124", 1.4, "Megane")
  File "<pyshell#246>", line 5, in __init__
    self.model_name
AttributeError: 'Sedan' object has no attribute 'model_name'
class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__(self):
        return "привет из родительского класса"

    
class Sedan(Car):
    pass

class Wagon(Car):
    pass

Sedan.__bases__
(<class '__main__.Car'>,)
s = Sedan("124124", 1.4, "Megane")
print(s)
привет из родительского класса
isinstance(s, Sedan)
True
isinstance(s, Car)
True
class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__(self):
        return "привет из родительского класса"
    def drive(self)
    
SyntaxError: incomplete input
class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__(self):
        return "привет из родительского класса"
    def drive(self):
        print("Врум Врум")

        
class Sedan(Car):
    pass

class Wagon(Car):
    pass

w = Wagon(12412, 1.4, "21412")
w
<__main__.Wagon object at 0x00000232F41104D0>
w.__dict__
{'vin': 12412, 'volume': 1.4, 'model_name': '21412'}
Sedan.__dict__
mappingproxy({'__module__': '__main__', '__doc__': None})
w.drive()
Врум Врум
class Sedan(Car):
    def drive(self):
        print("Седан делает ыыы")

    
s = Sedan(124,1.2,"322")
s.drive()
Седан делает ыыы
class Sedan(Car):
    def drive(self):
        super().
        
SyntaxError: incomplete input
class Sedan(Car):
    def drive(self):
        super().drive()
        print("Седан делает ыы")

        
w = Wagon (124, 1.2, "244t3")
s = Sedan(12512, 1.5, "231t")
w.drive()
Врум Врум
s.drive()
Врум Врум
Седан делает ыы
class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__(self):
        return "привет из родительского класса"
    def drive(self):
        print("Врум Врум")
    def show_car(self):
        print(self.vin, self.volume, self.model_name)

        
class Sedan(Car):
    def __init__(self):
        self.body_type = "Sedan"
    def drive(self):
        super().drive()
        print("Седан делает ыы")

        
s = Sedan()
print(s)
привет из родительского класса
s.drive()
Врум Врум
Седан делает ыы
s.show_car
<bound method Car.show_car of <__main__.Sedan object at 0x00000232F4121410>>
s.show_car()
Traceback (most recent call last):
  File "<pyshell#321>", line 1, in <module>
    s.show_car()
  File "<pyshell#314>", line 11, in show_car
    print(self.vin, self.volume, self.model_name)
AttributeError: 'Sedan' object has no attribute 'vin'
class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
...         self.model_name = model_name
...     def __str__(self):
...         return "привет из родительского класса"
...     def drive(self):
...         print("Врум Врум")
...     def show_car(self):
...         print(self.vin, self.volume, self.model_name)
... 
...         
>>> class Sedan(Car):
...     def __init__(self, vin, volume, model_name):
...         self.body_type = "Sedan"
...         super().__init__(vin, volume, model_name)
...     def drive(self):
...         super().drive()
...         print("Седан делает ыы")
... 
...         
>>> s = Sedan(12512, 1.5, "231t")
>>> s.body_type()
Traceback (most recent call last):
  File "<pyshell#328>", line 1, in <module>
    s.body_type()
TypeError: 'str' object is not callable
>>> s.vin
12512
>>> s.volume
1.5
>>> s.model_name()
Traceback (most recent call last):
  File "<pyshell#331>", line 1, in <module>
    s.model_name()
TypeError: 'str' object is not callable
>>> s.model_name
'231t'
>>> s.show_car()
12512 1.5 231t
>>> money = 125123
>>> money = -12412
