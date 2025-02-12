Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> input("Give me your password")
Give me your passwordqwerty
'qwerty'
>>> password=input("Give me your password\n")
Give me your password
qwerty
>>> print(password)
qwerty
>>> ms= = """ wertyu
SyntaxError: unterminated triple-quoted string literal (detected at line 1)
>>> ms= """hgtfrd
... kjuhygtr
... kjhgf
... -->"""
>>> a = input(ms)
hgtfrd
kjuhygtr
kjhgf
-->qwertyguh
>>> print(a)
qwertyguh
>>> type(a)
<class 'str'>
a = input(ms)
hgtfrd
kjuhygtr
kjhgf
-->657
type(a)
<class 'str'>
number = input("Дай число:\n")
Дай число:
123451
result = number ** 2
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    result = number ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
a = "123453"
b = "5.9"
c = 195
type(a)
<class 'str'>
type(b)
<class 'str'>
type(c)
<class 'int'>
d = 3.8
type(d)
<class 'float'>
int()
0
float()
0.0
str()
''
a
'123453'
b
'5.9'
c
195
d
3.8
int(d)
3
str(d)
'3.8'
float(d)
3.8
int("1252 f")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int("1252 f")
ValueError: invalid literal for int() with base 10: '1252 f'
d
3.8
str(d)
'3.8'
d
3.8
d = str(d)
d
'3.8'
type(d)
<class 'str'>
q = .98
print(q)
0.98
о = 54.
print(o)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(o)
NameError: name 'o' is not defined
о = 54.
print(о)
54.0
12 / 0
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    12 / 0
ZeroDivisionError: division by zero
12 % 0
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    12 % 0
ZeroDivisionError: integer modulo by zero
0 / 6
0.0
0 % 5
0
s, s4 = "hi", "ui"
print(s, s4)
hi ui
resu = s + s + s4 + s
resu
'hihiuihi'
s4
'ui'
4*s4
'uiuiuiui'
len(s4)
2
len(s)
2
wre = "wetf" "qwer" "12rf"
wre
'wetfqwer12rf'
g = "/" * 42
g
'//////////////////////////////////////////'
len(g)
42
print(1, "+", 2, "=", 1+2)
1 + 2 = 3
a, b = 1, 2
print(a, "+", b, "=", a+b)
1 + 2 = 3
print(f"{a}+{b}={a+b}")
1+2=3
pass
import keyword
keyword,kwlist
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    keyword,kwlist
NameError: name 'kwlist' is not defined. Did you mean: 'list'?
keyword.kwlist
KeyboardInterrupt
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
first_perem = int(input("Your first: "))
Your first: 123
second_perem = int(input("Your second: "))
Your second: 543
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
first_perem = int(input("Your first: "))
Your first: 123
second_perem = int(input("Your second: "))
Your second: 543
SyntaxError: multiple statements found while compiling a single statement


KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
фыв
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    фыв
NameError: name 'фыв' is not defined
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt

================================ RESTART: Shell ================================
first_perem = int(input("Your first: "))
Your first: 123
second_perem = int(input("Your second: "))
