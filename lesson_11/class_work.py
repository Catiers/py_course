Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class User:
    __counter = 0
    def __init__(self, name):
        self.name = name
        User.__counter += 1
    @classmethod
    def get_counter(cls):
        return cls.__counter
    def __str__(self):
        return f"User name: {self.name}."

    
User.get_counter()
0
k = User("Kate")
print(k)
User name: Kate.
k.get_counter()
1
User.get_counter()
1
User.__counter
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    User.__counter
AttributeError: type object 'User' has no attribute '__counter'. Did you mean: 'get_counter'?
class User:
    __counter = 0
    def __init__(self, name):
        self.name = name
        User.__counter += 1
        
    @classmethod
    def get_counter(cls):
        return cls.__counter
        
    @classmethod
    def set_counter(cls, value):
        cls.__counter = value
        
    def __str__(self):
        return f"User name: {self.name}."

k = User("Kate")
k.get_counter()
1
User.get_counter()
1
User.set_counter(2)
User.get_counter()
2
k.set_counter(563)
User.get_counter()
563
class User:
    __counter = 0
    def __init__(self, name):
        self.name = name
        User.__counter += 1

    def __str__(self):
        return f"User name: {self.name}."
        
    @classmethod
    def get_counter(cls):
        return cls.__counter
        
    @classmethod
    def set_counter(cls, value):
        cls.__counter = value
        
    @staticmethod
    def checkname(name):
        return False if len(name) < 2 else True

    
user1 = "Kate"
if User.checkname(user1):
    inst1 = User(user1)
else:
    print("Имя слишком короткое")

    
inst1
<__main__.User object at 0x00000279FEA57250>
print(inst1)
User name: Kate.
user2 = "Ya"
if User.checkname(user2):
    inst1 = User(user2)
else:
    print("Имя слишком короткое")

    
inst1
<__main__.User object at 0x00000279FE7BF9D0>
print(inst1)
User name: Ya.
user2 = "a"
if User.checkname(user2):
    inst1 = User(user2)
else:
    print("Имя слишком короткое")

    
Имя слишком короткое
class User:
    __counter = 0
    def __init__(self, name):
        print("__init__")
        self.name = name
        User.__counter += 1

    @classmethod
    def init_age_including(cls, name, age):
        print("alt__init__")
        user = cls(name)
        user.age = age
        return user

    def __str__(self):
        return f"User name: {self.name}."
        
    @classmethod
    def get_counter(cls):
        return cls.__counter
        
    @classmethod
    def set_counter(cls, value):
        cls.__counter = value

        

u1 = User("Vova")
__init__
u2 = User.init_age_including("Vova",19)
alt__init__
__init__
User.get_counter()
2
u1.name
'Vova'
u1.age
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    u1.age
AttributeError: 'User' object has no attribute 'age'
u2.name
'Vova'
u2.age
19
from abc import ABC, abstractmethod
class Export(ABC):
    @abstractmethod
    def export(self):
        pass

    
class Export(ABC):
    @abstractmethod
    def export(self):
        pass
    @abstractmethod
    def prep(self):
        pass
    @abstractmethod
    def status(self):
        pass

    
class ExportToTXT(Export):
    def __init__(self, file_name):
        self.file_name = file_name
    def exp(self):
        print("export to txt", self.file_name)

        
inst = ExportToTXT("ddsg:")
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    inst = ExportToTXT("ddsg:")
TypeError: Can't instantiate abstract class ExportToTXT with abstract methods export, prep, status
class ExportToTXT(Export):
    def __init__(self, file_name):
        self.file_name = file_name
    def export(self):
        print("export to txt", self.file_name)
    def prep(self):
        print("prep")

        
KeyboardInterrupt

inst = ExportToTXT("ddsg:")
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    inst = ExportToTXT("ddsg:")
TypeError: Can't instantiate abstract class ExportToTXT with abstract method status
class ExportToTXT(Export):
    def __init__(self, file_name):
        self.file_name = file_name
    def export(self):
        print("export to txt", self.file_name)
    def prep(self):
        print("prep")
    def status(self):
        print("status")

        
inst = ExportToTXT("1.txt")
inst.status()
status
inst.prep
<bound method ExportToTXT.prep of <__main__.ExportToTXT object at 0x00000279FE9EF190>>
inst.prep()
prep
inst.export()
export to txt 1.txt
class ExportToCSV(Export):
    def __init__(self, file_name):
        self.file_name = file_name
    def export(self):
        print("export to txt", self.file_name)
    def preparation(self):
        print("prep")

        
inst2 = ExportToCSV("fg")
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    inst2 = ExportToCSV("fg")
TypeError: Can't instantiate abstract class ExportToCSV with abstract methods prep, status
class ExportToCSV(Export):
    def __init__(self, file_name):
        self.file_name = file_name
    def export(self):
        print("export to txt", self.file_name)
    def prep(self):
        print("prep")
    def status(self):
        print("status")

        
inst2 = ExportToCSV("fg.csv")
inst2.status()
status
inst2.prep
<bound method ExportToCSV.prep of <__main__.ExportToCSV object at 0x00000279FE74A9D0>>
inst2.prep()
prep
inst2.export()
export to txt fg.csv
li = [ExportToTXT("1.txt"), ExportToCSV("n1.csv")]
for inst in li:
    inst.export()

    
export to txt 1.txt
export to txt n1.csv
class A:
    pass

class B(A):
    pass

class C(B):
    pass

c.__mro__
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    c.__mro__
NameError: name 'c' is not defined. Did you mean: 'C'?
C.__mro__
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
C.mro()
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
class A:
    a = 10

    
class B(A):
    b = 100

    
class C(B):
    c = 1000

    
f = C()
f.c
1000
f.b
100
f.a
10
f.d
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    f.d
AttributeError: 'C' object has no attribute 'd'
class A:
    a = 10
    def __init__(self):
        aaa = 11

        
class B(A):
    b = 100
    def __init__(self):
        bbb = 111

        
class C(B):
    c = 1000
    def __init__(self):
        ccc = 1111
        super().__init()

        
f = C()
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    f = C()
  File "<pyshell#142>", line 5, in __init__
    super().__init()
AttributeError: 'super' object has no attribute '_C__init'
class C(B):
    c = 1000
    def __init__(self):
        ccc = 1111
        super().__init__()

        
f = C()
class C(B):
    c = 1000
    def __init__(self):
        self.ccc = 1111
        super().__init__()

        
class A:
    a = 10
    def __init__(self):
        self.aaa = 11

        
class B(A):
    b = 100
    def __init__(self):
        self.bbb = 111

        
class C(B):
    c = 1000
    def __init__(self):
        self.ccc = 1111
        super().__init__()

        
f = C()
f.c
1000
f.ccc
1111
f.b
100
f.bbb
111
f.a
10
f.aaa
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    f.aaa
AttributeError: 'C' object has no attribute 'aaa'
try:
    raise AttributeError
except:
    print("err")
else:
    print("ok")
finally:
    print("fin)
          
SyntaxError: unterminated string literal (detected at line 8)
try:
    raise AttributeError
except:
    print("err")
else:
    print("ok")
finally:
    print("fin")

    
err
fin
try:
    1+1
except:
    print("err")
else:
    print("ok")
finally:
    print("fin")

    
2
ok
fin
def a(number):
    try:
        return number
    except:
        return number + 1
    else:
        return number + 2
    finally:
        return number ** 10

    
a(10)
10000000000
def a(number):
    try:
        return number
    except:
        return number + 1
    else:
        return number + 2

    
a(10)
10
class User:
    def __init__(self, name):
        self.name = name
        User.__counter += 1
        
    def __str__(self):
        return f"User name: {self.name}."

    
class User:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"User name: {self.name}."

    
class User:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"User name: {self.name}."

    def call(self, number):
        
SyntaxError: unexpected indent
class User:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"User name: {self.name}."
    def call(self, number):
        if len(number) < 8:
            pass
        return "Звоню {number}"

    
class NumberError(Exception):
    def __init__(self, number, message):
        self.number = number
        self.message = message

        
raisw NumberError(12541, "Короткий номер")
SyntaxError: invalid syntax
raise NumberError(12541, "Короткий номер")
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    raise NumberError(12541, "Короткий номер")
NumberError: (12541, 'Короткий номер')
class NumberError(Exception):
    def __init__(self, number, message):
        self.number = number
        self.message = message

        
class User:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"User name: {self.name}."
    def call(self, number):
        if len(number) < 8:
            raise NumberError(number, "Короткий номер")
        return "Звоню {number}"

    
user1 = User("Vasia")
user1.call(1251)
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    user1.call(1251)
  File "<pyshell#210>", line 8, in call
    if len(number) < 8:
TypeError: object of type 'int' has no len()
user1.call("1251")
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    user1.call("1251")
  File "<pyshell#210>", line 9, in call
    raise NumberError(number, "Короткий номер")
NumberError: ('1251', 'Короткий номер')
try:
    user1.call("1231")
except NumberError as e:
    print(e)
except:
    print("-1")

    
('1231', 'Короткий номер')
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
        return "Звоню {number}"

    
user1 = User("Vasia")
>>> try:
...     user1.call("1231")
... except NumberError as e:
...     print(e)
... except:
...     print("-1")
... 
...     
NumberError: number: 1231, message: Короткий номер
>>> try:
...     user1.call("1212313231")
... except NumberError as e:
...     print(e)
... except:
...     print("-1")
... 
...     
'Звоню {number}'
>>> class User:
...     def __init__(self, name):
...         self.name = name
...         
...     def __str__(self):
...         return f"User name: {self.name}."
...     def call(self, number):
...         if len(number) < 8:
...             raise NumberError(number, "Короткий номер")
...         return f"Звоню {number}"
... 
...     
>>> user1 = User("Vasia")
>>> try:
...     user1.call("1212313231")
... except NumberError as e:
...     print(e)
... except:
...     print("-1")
... 
'Звоню 1212313231'
