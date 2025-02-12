Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
int
<class 'int'>
print
<built-in function print>
import time
time
<module 'time' (built-in)>
time.sleep(1)
copy
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    copy
NameError: name 'copy' is not defined
deepcopy()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    deepcopy()
NameError: name 'deepcopy' is not defined
import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


n = 10
users = []
user_A_password = input("Enter your pass: ")
Enter your pass: 55555
user_A_name = input("Your name: ")
Your name: John
users.append([user_A_name,user_A_password])
users
[['John', '55555']]
def register():
    user_A_name = input("Your name: ")
    user_A_password = input("Enter your pass: ")
    users.append([user_A_name,user_A_password])
    primt("Done ...")

    
register()
Your name: Kolay
Enter your pass: 54321
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    register()
  File "<pyshell#21>", line 5, in register
    primt("Done ...")
NameError: name 'primt' is not defined. Did you mean: 'print'?
def register():
    user_A_name = input("Your name: ")
    user_A_password = input("Enter your pass: ")
    users.append([user_A_name,user_A_password])
    print("Done ...")

    
register()

Your name: john
Enter your pass: 5321
Done ...
n = 8
for i in n:
    register()

    
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    for i in n:
TypeError: 'int' object is not iterable
n = 3
for i in range(n):
    register()

    
Your name: gdf
Enter your pass: arg
Done ...
Your name: asg
Enter your pass: aewg
Done ...
Your name: asdg
Enter your pass: aeg
Done ...
users
[['John', '55555'], ['Kolay', '54321'], ['john', '5321'], ['gdf', 'arg'], ['asg', 'aewg'], ['asdg', 'aeg']]
users[2]
['john', '5321']
def hello():
    print("Hello")

    
hello()
Hello
Hello
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    Hello
NameError: name 'Hello' is not defined. Did you mean: 'hello'?
hello
<function hello at 0x0000012B8768DDA0>
def hello():
    user = input("Your name: ")
    print(f"Hello, {user}")

    
hello()
Your name: Kostya
Hello, Kostya
def hello():
    user = input("Your name: ")
    print(f"Hello, {user}")
    for i in range(3):
        print(i, end=" ")
    d = 88
    if d == 88:
        print("XXX")
    print(53463)

    
hello()
Your name: Katya
Hello, Katya
0 1 2 XXX
53463
dete()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dete()
NameError: name 'dete' is not defined
hello = 55
hello()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    hello()
TypeError: 'int' object is not callable
print(hello)
55
change_password()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    change_password()
NameError: name 'change_password' is not defined
def hi():
    print("hi")

    
hi()
hi
hi(1)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    hi(1)
TypeError: hi() takes 0 positional arguments but 1 was given
print(24,234634,856)
24 234634 856
def hello(user):
    print(f"Hello, {user}")

    
hello()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    hello()
TypeError: hello() missing 1 required positional argument: 'user'
hello(12)
Hello, 12
hello(36237gdf)
SyntaxError: invalid decimal literal
hello(sbfs)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    hello(sbfs)
NameError: name 'sbfs' is not defined
hello("fdg")
Hello, fdg
hello(1,2)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    hello(1,2)
TypeError: hello() takes 1 positional argument but 2 were given
def hello(a,b,c):
    print(f"Hello, {a},{b},{c}")

    
hello(1)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    hello(1)
TypeError: hello() missing 2 required positional arguments: 'b' and 'c'
hello(1,2,4)
Hello, 1,2,4
hello(b=33,c=25,a=215)
Hello, 215,33,25
hello(33,c=25,a=215)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    hello(33,c=25,a=215)
TypeError: hello() got multiple values for argument 'a'
hello(325,b=33,c=25)
Hello, 325,33,25
hello(b=33,c=25,215)
SyntaxError: positional argument follows keyword argument
def hello(a,b,c,d):
    print(f"Hello, {a},{b},{c},{d}")

    
hello(1,3,7,9)
Hello, 1,3,7,9
hello(1,2,d=362,c=3262)
Hello, 1,2,3262,362
def hello(name, age):
    print(f"Hello, {name},{age}")

    
hello("John
      
SyntaxError: unterminated string literal (detected at line 1)
hello("John", 13)
      
Hello, John,13
hello(13, "john")
      
Hello, 13,john
hello(age=13, name="john")
      
Hello, john,13
def
SyntaxError: invalid syntax




def create_order(name, phone, age, msg):
    print("Order 2634: created.")
    print("order detailes")
    print(f"   Name:{name}")
    print(f"   Your phone:{phone}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    print()

    
create(1)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    create(1)
NameError: name 'create' is not defined
create_order(2)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    create_order(2)
TypeError: create_order() missing 3 required positional arguments: 'phone', 'age', and 'msg'
def create_order(name, phone, age='', msg=''):
    print("Order 2634: created.")
    print("order detailes")
    print(f"   Name:{name}")
    print(f"   Your phone:{phone}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    print()

    
create_order(John, 32532)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    create_order(John, 32532)
NameError: name 'John' is not defined
create_order("John", 32532, 24, "dfgdfg")
Order 2634: created.
order detailes
   Name:John
   Your phone:32532
   Your age:24
   Your message:dfgdfg

create_order("John", 32532)
Order 2634: created.
order detailes
   Name:John
   Your phone:32532
   Your age:
   Your message:

create_order("John")
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    create_order("John")
TypeError: create_order() missing 1 required positional argument: 'phone'
def create_order(name='As', phone='654323', age='', msg=''):
    print("Order 2634: created.")
    print("order detailes")
    print(f"   Name:{name}")
    print(f"   Your phone:{phone}")

    
create_order(2)
Order 2634: created.
order detailes
   Name:2
   Your phone:654323
name = input("-->")
-->fghjkl
name
'fghjkl'
def hello():
    pass

res = hello()
res
print(res)
None
def hello():
    print(1*44)

    
res = hello()
44
print(res)
None
def create_order(name, phone, age='', msg=''):
    if len(name) < 2:
        returm False
    if str(phone).isallnum() != True:
        return False        
    print("Order 2634: created.")
    print("order detailes")
    print(f"   Name:{name}")
    print(f"   Your phone:{phone}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    print()
    return True
SyntaxError: invalid syntax

def create_order(name, phone, age='', msg=''):
    if len(name) < 2:
        return False
    if str(phone).isallnum() != True:
        return False        
    print("Order 2634: created.")
    print("order detailes")
    print(f"   Name:{name}")
    print(f"   Your phone:{phone}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    print()
    return True

create_order('',24534)
False
res = create_order('',24534)
res
False
print(res)
False
def create_order(name, phone, age='', msg=''):
    if len(name) < 2:
        return False
    if str(phone).isalnum() != True:
        return False        
    print("Order 2634: created.")
    print("order detailes")
    print(f"   Name:{name}")
    print(f"   Your phone:{phone}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    print()
    return True

res = create_order('Iun',24534)
Order 2634: created.
order detailes
   Name:Iun
   Your phone:24534
   Your age:
   Your message:

def create_order(name, phone, age='', msg=''):
    if len(name) < 2:
        return False
    if phone.isalnum() != True:
        return False        
    print("Order 2634: created.")
    print("order detailes")
    print(f"   Name:{name}")
    print(f"   Your phone:{phone}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    print()
    return True

res = create_order('Iun','24534')
Order 2634: created.
order detailes
   Name:Iun
   Your phone:24534
   Your age:
   Your message:

res = create_order('Iun','24s534')
Order 2634: created.
order detailes
   Name:Iun
   Your phone:24s534
   Your age:
   Your message:

res = create_order('Iun',' +24534')
res
False
res = create_order('Iun','24asf534')
Order 2634: created.
order detailes
   Name:Iun
   Your phone:24asf534
   Your age:
   Your message:

def create_order(name, phone, age='', msg=''):
    if len(name) < 2 or phone.isalnum() != True:
        return False        
    print("Order 2634: created.")
    print("order detailes")
    print(f"   Name:{name}")
    print(f"   Your phone:{phone}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    print()
    return True

def Up(name):
    print(name.upper())

    
Up("gfdg")
GFDG
def Up(name):
    return name.upper()

Up("gsfdg")
'GSFDG'
name
'fghjkl'
ph = 46347
ph = "35346"
age = 12
msg = "dhfdh"
create_order("asgsg","8536")
Order 2634: created.
order detailes
   Name:asgsg
   Your phone:8536
   Your age:
   Your message:

True
name
'fghjkl'
ph
'35346'
help
Type help() for interactive help, or help(object) for help about object.
help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.
    
    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.

help(create_order)
Help on function create_order in module __main__:

create_order(name, phone, age='', msg='')

def create_order(name, phone, age='', msg=''):
    """Функция для создания ордера
    Параметры:
    name - строка, обязательно
    phobe - обязательно
    age - необязательно
    msg - необязательно
"""
    
    
    if len(name) < 2 or phone.isalnum() != True:
        return False        
    print("Order 2634: created.")
    print("order detailes")
    print(f"   Name:{name}")
    print(f"   Your phone:{phone}")
    print(f"   Your age:{age}")
    print(f"   Your message:{msg}")
    print()
    return True

help(create_order)
Help on function create_order in module __main__:

create_order(name, phone, age='', msg='')
    Функция для создания ордера
    Параметры:
    name - строка, обязательно
    phobe - обязательно
    age - необязательно
    msg - необязательно

create_order.__doc__
'Функция для создания ордера\n    Параметры:\n    name - строка, обязательно\n    phobe - обязательно\n    age - необязательно\n    msg - необязательно\n'
def a():
    print(1)

    
def b():
    print(2)

    
def c():
    print(3)

    
c
<function c at 0x0000012B876C9120>
c()
3
del c
c()
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    c()
NameError: name 'c' is not defined
b()
2
qwe = b
qwe()
2
del b
b
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    b
NameError: name 'b' is not defined
b()
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    b()
NameError: name 'b' is not defined
qwe
<function b at 0x0000012B876C9260>
qwe()
2
id(a)
1286467018304
sss = a
sss()
1
a()
1
id(sss)
1286467018304
del(a)
a()
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    a()
NameError: name 'a' is not defined
\
sss
<function a at 0x0000012B8768DE40>
sss()
1
def members(num):
    if num % 2 == 0:
        return True
    return None
members(2)
SyntaxError: invalid syntax
def members(num):
    if num % 2 == 0:
        return True
    return None

members(2)
True
members(3)
def members(num):
    if num % 2 == 0:
        return True

    
members(3)

members(2)
True
def members(num):
    return num % 2 == 0

members(3)
False
members(2)
True
a = 35
s = "asgs"
isinstance(a,int)
True
isinstance(s,int)
False
isinstance(a,str)
False
isinstance(s,str)
True
if isinstance(a,int):
    print("Int")
elif isinstance(a,str):
    print("str")

    
Int
isinstance(a,(int,float,list))
True
a = "fdg"
isinstance(a,(int,float,list))
False
def check(a):
    if isinstance(a,int):
    print("Int")
elif isinstance(a,str):
    print("str")
    
SyntaxError: expected an indented block after 'if' statement on line 2
def check(a):
    if isinstance(a,int):
        print("Int")
    elif isinstance(a,str):
        print("str")

        
check(325236)
Int
check("sdgs")
str
total()
Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    total()
NameError: name 'total' is not defined
total = 0
\
def add_to_total(n):
    total += n

    
add_to_total(5)
Traceback (most recent call last):
  File "<pyshell#241>", line 1, in <module>
    add_to_total(5)
  File "<pyshell#240>", line 2, in add_to_total
    total += n
UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
def add_to_total(n):
    total = total + n

    
add_to_total(5)
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    add_to_total(5)
  File "<pyshell#243>", line 2, in add_to_total
    total = total + n
UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
def add_to_total(n):
    global total
    total += n

    
add_to_total(5)
print(total)
5
x = 52
def add(x):
    print("Inside ", x, id(x))
    x += 7686
    print("Inside ", x, id(x))

    
x
52
add(x)
Inside  52 140726296017288
Inside  7738 1286461089776
x
52
x = 52
def add(number):
    print("Inside ", number, id(number))
    number += 7686
    print("Inside ", number, id(number))

    
add(x)
Inside  52 140726296017288
Inside  7738 1286461090256
x
52
number = 52
def add():
    global number
    print("Inside ", number, id(number))
    number += 7686
    print("Inside ", number, id(number))

    
add()
Inside  52 140726296017288
Inside  7738 1286461090480
number
7738
def a():
    print(1)

    
def b():
    print(2)

    
def c():
    print(3)

    
li = [a,b,c]

li
[<function a at 0x0000012B876CA3E0>, <function b at 0x0000012B876C89A0>, <function c at 0x0000012B876C8860>]
li = [a,b,c, print, int]
li
[<function a at 0x0000012B876CA3E0>, <function b at 0x0000012B876C89A0>, <function c at 0x0000012B876C8860>, <built-in function print>, <class 'int'>]
li()
Traceback (most recent call last):
  File "<pyshell#280>", line 1, in <module>
    li()
TypeError: 'list' object is not callable
for i in li:
    i()

    
1
2
3

0
def noname(number):
    if number > 20:
        return True
    return number + noname(number * 4)

noname(1)
22
def noname(number):
    if number > 20:
        return True
    return number + noname(number + 4)

noname(1)
46
import sys
sys.getrecursionlimit()
1000
sys.setrecursionlimit(1000000)
sys.getrecursionlimit()
1000000
f1 = f2 = 1
f1
1
f2
1
f1, f2 = f2, f1+f2
f1
1
f2
2
f1, f2 = f2, f1+f2
f1
2
f2
3
>>> f1, f2 = f2, f1+f2
>>> f1
3
>>> f2
5
>>> f1, f2 = f2, f1+f2
>>> f1
5
>>> f2
8
>>> f1, f2 = f2, f1+f2
>>> r1
Traceback (most recent call last):
  File "<pyshell#313>", line 1, in <module>
    r1
NameError: name 'r1' is not defined. Did you mean: 'f1'?
>>> f1
8
>>> f2
13
>>> f1, f2 = f2, f1+f2
>>> f1
13
>>> f2
21
>>> f1, f2 = f2, f1+f2
>>> f1
21
>>> f2
34
>>> f1 = f2 = 1
>>> for i in range(10):
...     f1, f2 = f2, f1+f2
... 
...     
>>> f1
89
>>> f2
144
