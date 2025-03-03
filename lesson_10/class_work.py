Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Car:
    def __init__(self, brand, vol):
        self.brand = brand
        self.volume = vol
    def __str__(self):
        return f"{self.brand}: {self.volume}"

    
my_car = Car("Vaz", 1.8)
print(my_car)
Vaz: 1.8
\
class Car:
    def __init__(self, brand, vol):
        self.brand = brand
        self.volume = vol
    def __str__(self):
        return f"str - {self.brand}: {self.volume}"
    def __repr__(self):
        return f"repr - {self.brand}: {self.volume}"

    
my_car = Car("Vaz", 1.8)
my_car
repr - Vaz: 1.8
print(my_car)
str - Vaz: 1.8
class Car:
    def __init__(self, brand, vol):
        self.brand = brand
        self.volume = vol
    def __str__(self):
        return f"{self.brand}: {self.volume}"
    def __repr__(self):
        return f"Inst of Car:\n\tBrand:{self.brand}. \n\tVolume:{self.volume}"

    
my_car = Car("Vaz", 1.8)
my_car
Inst of Car:
	Brand:Vaz. 
	Volume:1.8
print(my_car)
Vaz: 1.8
my_car.brand
'Vaz'
my_car.volume
1.8
my_car.volume = 12.3
my_car.volume
12.3
class Car:
    counter = 0
    def __init__(self, brand, vol):
        self.brand = brand
        self.volume = vol
        Car.counter += 1
    def __str__(self):
        return f"{self.brand}: {self.volume}"
    def __repr__(self):
        return f"Inst of Car:\n\tBrand:{self.brand}. \n\tVolume:{self.volume}"

    
Car.counter
0
my_car = Car("Vaz", 1.8)
Car.counter
1
my_car = Car("Vaz", 1.8)
Car.counter
2
Car.__doc__
Car.__bases__
(<class 'object'>,)
class Empty:
    pass

my_car.__dict__
{'brand': 'Vaz', 'volume': 1.8}
Car.__dict__
mappingproxy({'__module__': '__main__', 'counter': 2, '__init__': <function Car.__init__ at 0x0000025128DAAA20>, '__str__': <function Car.__str__ at 0x0000025128DAAAC0>, '__repr__': <function Car.__repr__ at 0x0000025128DAAB60>, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None})
Car.__name__
'Car'
class Car:
    counter = 0
    def __init__(self, brand, vol):
        self.brand = brand
        self.volume = vol
        Car.counter += 1
    def drive(self, dist):
        print(f"Я проехал [dist} километров")
    def __str__(self):
        return f"{self.brand}: {self.volume}"
    def __repr__(self):
        return f"Inst of Car:\n\tBrand:{self.brand}. \n\tVolume:{self.volume}"
    
SyntaxError: f-string: single '}' is not allowed
class Car:
    counter = 0
    def __init__(self, brand, vol):
        self.brand = brand
        self.volume = vol
        Car.counter += 1
    def drive(self, dist):
        print(f"Я проехал {dist} километров")
    def __str__(self):
        return f"{self.brand}: {self.volume}"
    def __repr__(self):
        return f"Inst of Car:\n\tBrand:{self.brand}. \n\tVolume:{self.volume}"

    
my_car = Car("Zaz", 0.8)
my_car.drive(11)
Я проехал 11 километров
hasattr
<built-in function hasattr>
setattr
<built-in function setattr>
getattr
<built-in function getattr>
my_car
Inst of Car:
	Brand:Zaz. 
	Volume:0.8
my_car.brand
'Zaz'
getattr(my_car,"brand")
'Zaz'
getattr(my_car,"bran")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    getattr(my_car,"bran")
AttributeError: 'Car' object has no attribute 'bran'. Did you mean: 'brand'?
getattr(my_car,"brad", False)
False
res = getattr(my_car,"brad", False)
res
False
res = getattr(my_car,"brand")
res
'Zaz'
if getattr(my_car, "brand") != False:
    print(my_car.brand)

    
Zaz
hasattr
<built-in function hasattr>
hasattr(my_car, "brand")
True
hasattr(my_car, "bran")
False
if hasattr(my_car, "brand"):
    print(my_car.brand)

    
Zaz
if hasattr(my_car, "brand"):
    print(my_car.brand)
else:
    print(False)

    
Zaz
setattr(my_car, "bra", 12241)
my_car.__dict__
{'brand': 'Zaz', 'volume': 0.8, 'bra': 12241}
setattr(my_car, "brand", "sfdgs")
my_car.__dict__
{'brand': 'sfdgs', 'volume': 0.8, 'bra': 12241}
class Animal:
    def __init__(self, color, age):
        self.color = color
        self.age = age
    def eat(self):
        print(f"Животное {self.color} кушает...")
    def go(self):
        print("Животное двигается")
    def sleep(self):
        print("Zzzzz...")

...         
>>> class homeCat(Animal):
...     def __init__(self, name, color, age):
...         self.name = name
...         super().__init__(color, age)
... 
...         
>>> car = homeCat("Dima", "black", 1)
>>> car.color
'black'
>>> car.name
'Dima'
>>> car.age
1
>>> car.eat
<bound method Animal.eat of <__main__.homeCat object at 0x0000025128813990>>
>>> car.eat()
Животное black кушает...
>>> car.sleep()
Zzzzz...
>>> car.go()
Животное двигается
>>> class homeCat(Animal):
...     def __init__(self, name, color, age):
...         self.name = name
...         super().__init__(color, age)
...     def __repr__(self):
...         return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"
... 
...     
>>> cat = homeCat("Dima", "black", 1)
>>> car
<__main__.homeCat object at 0x0000025128813990>
>>> cat
Cat Name:Dima
	Age:1
	Color:black
>>> class Animal:
...     def __init__(self, color, age):
...         self.color = color
...         self.age = age
...     def eat(self):
...         print(f"Животное {self.color} кушает...")
...     def go(self):
...         print("Животное двигается")
...     def sleep(self):
...         print("Zzzzz...")
... 
...         
>>> class homeCat(Animal):
...     counter = 123
...     def __init__(self, name, color, age):
...         self.name = name
...         self.id = homeCat.counter
...         homeCat.counter += 1
...         super().__init__(color, age)
...     def __repr__(self):
...         return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"
... 
...     
>>> cat = homeCat("Dima", "black", 1)
>>> cat.id
123
>>> cat.id = 12534
>>> cat.id
12534
>>> class homeCat(Animal):
...     counter = 123
...     def __init__(self, name, color, age):
...         self.name = name
...         self._id = homeCat.counter
...         homeCat.counter += 1
...         super().__init__(color, age)
...     def __repr__(self):
        return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

    
cat = homeCat("Dima", "black", 1)
cat.__dict__
{'name': 'Dima', '_id': 123, 'color': 'black', 'age': 1}
cat._id
123
cat_id = 12521
cat_id
12521
class homeCat(Animal):
    counter = 123
    def __init__(self, name, color, age):
        self.name = name
        self.id_ = homeCat.counter
        homeCat.counter += 1
        super().__init__(color, age)
    def __repr__(self):
        return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

    
cat = homeCat("Dima", "black", 1)
cat.__dict__
{'name': 'Dima', 'id_': 123, 'color': 'black', 'age': 1}
cat._id
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    cat._id
AttributeError: 'homeCat' object has no attribute '_id'
cat.id_
123
cat.id_ = 12521
cat.id_
12521
class homeCat(Animal):
    counter = 123
    def __init__(self, name, color, age):
        self.name = name
        self.__id = homeCat.counter
        homeCat.counter += 1
        super().__init__(color, age)
    def __repr__(self):
        return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

    
cat = homeCat("Dima", "black", 1)
car.__id
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    car.__id
NameError: name 'car' is not defined. Did you mean: 'cat'?
cat.__id
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    cat.__id
AttributeError: 'homeCat' object has no attribute '__id'
car.__dict__
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    car.__dict__
NameError: name 'car' is not defined. Did you mean: 'cat'?
cat.__dict__
{'name': 'Dima', '_homeCat__id': 123, 'color': 'black', 'age': 1}
cat._homeCat__id
123
cat._homeCat__id = 1254
cat._homeCat__id
1254
class homeCat(Animal):
    counter = 123
    def __init__(self, name, color, age):
        self.name = name
        self.__id = homeCat.counter
        homeCat.counter += 1
        super().__init__(color, age)
    def get_id(self):
        print(f"cat id is: {self.__id}")
    def __repr__(self):
        return f"Cat Name:{self.name}\n\tAge:{self.age}\n\tColor:{self.color}"

    
cat = homeCat("Dima", "black", 1)
cat.get_id()
cat id is: 123

stack = []
def push(value):
    stack.append(value)

    
def pop():
    stack.pop()

    
push(1)
push(2)
push(3)
push(4)
pop()
stack
[1, 2, 3]
pop
<function pop at 0x000001A7A977EC00>
pop()
stack
[1, 2]
pop()
stack
[1]


class Stack:
    pass

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        self.stack.pop()

        
s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
KeyboardInterrupt
s1.stack
[1, 2, 3]
s2 = Stack()
s2.push(1)
s2.stack
[1]
s1.pop()
s1.stack
[1, 2]
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        self.stack.pop()
        return "OK"

    
class Stack:
    def __init__(self):
        self.__stack = []
    def push(self, value):
        self.__stack.append(value)
    def pop(self):
        try:
            self.__stack.pop()
        except:
            return "NE OK"
        return "OK"
    def show(self):
        return self.__stack

    
s1 = Stack()
s1.pop()
'NE OK'
s1.push(1)
s1.push(2)
s1.push(25)
s1.push(21)
s1.show()
[1, 2, 25, 21]
s1.pop()
'OK'
s.show()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s.show()
NameError: name 's' is not defined. Did you mean: 's1'?
s1.show()
[1, 2, 25]
s1.pop()
'OK'
s1.show()
[1, 2]
class Stack:
    def __init__(self):
        self.__stack = []
    def push(self, value):
        self.__stack.append(value)
    def pop(self):
        try:
            self.__stack.pop()
        except:
            return "NE OK"
        return "OK"
    def show(self):
        return self.__stack

    




class Stack:
    def __init__(self):
        self.__stack = []
    def push(self, value):
        self.__stack.append(value)
    def pop(self):
        try:
            self.__stack.pop()
        except:
            return "NE OK"
        return "OK"
    def show(self):
        return self.__stack

    
class countingStack(Stack)"
SyntaxError: unterminated string literal (detected at line 1)
class countingStack(Stack):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.summa = 0
    def push(self, value):
        self.counter += 1
        self.summa += value
        super().push(value)

        
s1 = Stack()
class Stack:
    def __init__(self):
        self.__stack = []
    def push(self, value):
        self.__stack.append(value)
    def pop(self):
        try:
            self.__stack.pop()
        except:
            return "NE OK"
        return "OK"
    def show(self):
        return self.__stack

    




class Stack:
    def __init__(self):
        self.__stack = []
    def push(self, value):
        self.__stack.append(value)
    def pop(self):
        try:
            self.__stack.pop()
        except:
            return "NE OK"
        return "OK"
    def show(self):
        return self.__stack

    
class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.summa = 0
    def push(self, value):
        self.counter += 1
        self.summa += value
        super().push(value)

        
s1 = CountingStack()
s1.show()
[]
s1.pop()
'NE OK'
s1.counter
0
s1.summa
0
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(54)
s1.show()
[1, 2, 3, 4, 54]
s1.counter
5
s1.summa
64
s1.pop
<bound method Stack.pop of <__main__.CountingStack object at 0x000001A7A9792910>>
s1.pop()
'OK'
s1.pop()
'OK'
s1.pop()
'OK'
a = 10
b = 21
a +
SyntaxError: invalid syntax
a + b
31
a.__add__(b)
31
a - b
-11
a.__sub__(b)
-11
a / b
0.47619047619047616
a.__truediv__(b)
0.47619047619047616
s = "dfhdf"
s1 = "hdfhdef"
s.__add__(s1)
'dfhdfhdfhdef'
s + s1
'dfhdfhdfhdef'
"s" in s
False
s.__contains__("d")
True
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __add__(self, nextcat):
        return self.age + nextcat.age
    def __contains__(self, key):
        return key in self.name
    def __len__(self):
        return self.age
    def __lt__(self, nextcat):
        return self.age < nextcat.age

    
c = Cat("Cat", 5)
c2 = Cat("Moa", 6)
c + c2
11
len(c)
5
len(c2)
6
c < c2
True
c2 < c
False
"a" in c
True
"d" in c
False


class Wallet
SyntaxError: expected ':'
class Wallet:
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, int_value):
        return self.amount + int_value
    def __sub__(self,int_value)
    
SyntaxError: expected ':'
class Wallet:
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, int_value):
        return self.amount + int_value
    def __sub__(self, int_value):
        return self.amount - int_value
    def __len__(self):
        return self.amount

    
my_wallet = Wallet(1000)
my_wallet + 100
1100
len(my_wallet)
1000
class Wallet:
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, int_value):
        self.amount += int_value
        return self.amount
    def __sub__(self, int_value):
        self.amount -= int_value
        return self.amount
    def __len__(self):
        return self.amount

    
my_wallet = Wallet(1000)
my_wallet + 100
1100
len(my_wallet)
1100
my_wallet - 50
1050
len(my_wallet)
1050
