Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li = []
li
[]
type(li)
<class 'list'>
tp = ()
tp
()
type(tp)
<class 'tuple'>
tp2 = tuple()
tp2
()
type(tp2)
<class 'tuple'>
num = 2.
num
2.0
type(num)
<class 'float'>
num = 2,
num
(2,)
typenum)
SyntaxError: unmatched ')'
type(num)
<class 'tuple'>
li = [11,22,33]
st = "asd"
se = set(st)
\
se
{'d', 'a', 's'}
ss = {12,122,231,125}
t = (124,1251,14,12)
tt = 1,25,7,9,6,2
tt
(1, 25, 7, 9, 6, 2)
tuple()
()
t = tuple(se)
r
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    r
NameError: name 'r' is not defined
t
('d', 'a', 's')
type(t)
<class 'tuple'>
isinstance(t)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    isinstance(t)
TypeError: isinstance expected 2 arguments, got 1
isinstance(t, typle)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    isinstance(t, typle)
NameError: name 'typle' is not defined. Did you mean: 'tuple'?
isinstance(t,tuple)
True
isinstance(t,int)
False
t = 1.
t1 = 1.,
t2 = 1,
print(t,t1,t2)
1.0 (1.0,) (1,)
n = 1,2,3,4,5
n
(1, 2, 3, 4, 5)
type(n)
<class 'tuple'>
n[1]
2
n[-1]
5
n[2]
3
liN = list(n)
liN[2] = 443
liN
[1, 2, 443, 4, 5]
n
(1, 2, 3, 4, 5)
n = tuple(liN)
n
(1, 2, 443, 4, 5)
t
1.0
t1
(1.0,)
t = 1,23,5
t
(1, 23, 5)
a,b,c = t
a
1
b
23
c
5
s = "asssv"
abcde = "sfasd"
a
1
c
5
b
23
a,b,c,d = "asdf"
a
'a'
b
's'
c
'd'
d
'f'
t = (1,2,5,2,5,3,5,67)
t
(1, 2, 5, 2, 5, 3, 5, 67)
a,c,b = t
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a,c,b = t
ValueError: too many values to unpack (expected 3)
a,c,*b = t
a
1
b
[5, 2, 5, 3, 5, 67]
c
2
type(b)
<class 'list'>
*a,b,c = t
b
5
c
67
a
[1, 2, 5, 2, 5, 3]
st = "sdgggsdfga"
a,b,*c = st
a
's'
b
'd'
v
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    v
NameError: name 'v' is not defined
c
['g', 'g', 'g', 's', 'd', 'f', 'g', 'a']
se = {1,23,4,3,5,53,44213}
a,*b,c = se
a
1
b
[3, 4, 5, 44213, 53]
c
23
a,*b,*c = se
SyntaxError: multiple starred expressions in assignment
def numbers():
    return 1,2,3,4,5,6

numbers()
(1, 2, 3, 4, 5, 6)
a, b* = numbers()
SyntaxError: invalid syntax
a,*b = numbers()
a
1
b
[2, 3, 4, 5, 6]
def numbers():
    return "error:...",1,2,3,4,5,6

numbers()
('error:...', 1, 2, 3, 4, 5, 6)
err, *tp_n = numbers()
err
'error:...'
tp_n
[1, 2, 3, 4, 5, 6]
if err == "error:...":
    print(123)

    
123
t
(1, 2, 5, 2, 5, 3, 5, 67)
t[:]
(1, 2, 5, 2, 5, 3, 5, 67)
aa = t
aa
(1, 2, 5, 2, 5, 3, 5, 67)
t
(1, 2, 5, 2, 5, 3, 5, 67)
aa[1] = 99
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    aa[1] = 99
TypeError: 'tuple' object does not support item assignment
t
(1, 2, 5, 2, 5, 3, 5, 67)
t[1:]
(2, 5, 2, 5, 3, 5, 67)
t
(1, 2, 5, 2, 5, 3, 5, 67)
t[1:6]
(2, 5, 2, 5, 3)
t[1:-1]
(2, 5, 2, 5, 3, 5)
t[::2]
(1, 5, 5, 5)
t[::-2]
(67, 3, 2, 2)
t += 1
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    t += 1
TypeError: can only concatenate tuple (not "int") to tuple
t += 1,
t
(1, 2, 5, 2, 5, 3, 5, 67, 1)
t + t
(1, 2, 5, 2, 5, 3, 5, 67, 1, 1, 2, 5, 2, 5, 3, 5, 67, 1)
t * 9
(1, 2, 5, 2, 5, 3, 5, 67, 1, 1, 2, 5, 2, 5, 3, 5, 67, 1, 1, 2, 5, 2, 5, 3, 5, 67, 1, 1, 2, 5, 2, 5, 3, 5, 67, 1, 1, 2, 5, 2, 5, 3, 5, 67, 1, 1, 2, 5, 2, 5, 3, 5, 67, 1, 1, 2, 5, 2, 5, 3, 5, 67, 1, 1, 2, 5, 2, 5, 3, 5, 67, 1, 1, 2, 5, 2, 5, 3, 5, 67, 1)
t
(1, 2, 5, 2, 5, 3, 5, 67, 1)
t *= 2
t
(1, 2, 5, 2, 5, 3, 5, 67, 1, 1, 2, 5, 2, 5, 3, 5, 67, 1)
5 in t
True
9897 in t
False
41 in t
False
a
1
b
[2, 3, 4, 5, 6]
c
23
b = "wet"
a
1
c
23
b
'wet'
a,c,b
(1, 23, 'wet')
t = 1,24,15,a,b,c
t
(1, 24, 15, 1, 'wet', 23)
ordersId = 1,2,34,2,5,7,8,6
ordersId
(1, 2, 34, 2, 5, 7, 8, 6)
ordersid += (len(ordersId)+1,)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    ordersid += (len(ordersId)+1,)
NameError: name 'ordersid' is not defined. Did you mean: 'ordersId'?
ordersId += (len(ordersId)+1,)
ordersId += (len(ordersId)+1,)
ordersId += (len(ordersId)+1,)
ordersId += (len(ordersId)+1,)
ordersId += (len(ordersId)+1,)
ordersId
(1, 2, 34, 2, 5, 7, 8, 6, 9, 10, 11, 12, 13)
len(ordersId)
13
s
'asssv'
len(s)
5
len(li)
3
t = 1,2,34,5
155
155
144
144
t[1:-1]
(2, 34)
155,
(155,)
155,
(155,)
t = 155, + t[1:-1] + 144,
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    t = 155, + t[1:-1] + 144,
TypeError: bad operand type for unary +: 'tuple'
t = (155, ) + t[1:-1] + (144, )
t
(155, 2, 34, 144)
t
(155, 2, 34, 144)
for value in t:
    print(value)

    
155
2
34
144
for value in t:
    if value *2 ==4:
        continue
    print(value)

    
155
34
144
t
(155, 2, 34, 144)
n = len(t)
n
4
for i in range(n):
    print(i, ", value:", t[i])

    
0 , value: 155
1 , value: 2
2 , value: 34
3 , value: 144
di = {}
type(di)
<class 'dict'>
di = dict()
type(di1)
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    type(di1)
NameError: name 'di1' is not defined. Did you mean: 'di'?
di = {1:"value, "as":123}
      
SyntaxError: unterminated string literal (detected at line 1)
di = {1:"value", "as":123}
      
di
      
{1: 'value', 'as': 123}
se
      
{1, 3, 4, 5, 44213, 53, 23}
hash
      
<built-in function hash>
a, b, c = 3, 4., "dsg"
      
a
      
3
b
      
4.0
c
      
'dsg'
li = [1,2,3]
      
se = {1,2,3,4}
      
tp = (11,2,3,4)
      
hash(a)
      
3
hash(b)
      
4
hash(c)
      
-3582091894862742351
hash(tp)
      
-8881800982856668070
hash(se)
      
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    hash(se)
TypeError: unhashable type: 'set'
hash(li)
      
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    hash(li)
TypeError: unhashable type: 'list'
hash(di)
      
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    hash(di)
TypeError: unhashable type: 'dict'
dd = {1:"a", 2.:"asdf", "s":"asgrg", a:"asgrsd"}
      
dd
      
{1: 'a', 2.0: 'asdf', 's': 'asgrg', 3: 'asgrsd'}
dd[1]
      
'a'
dd[21]
      
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    dd[21]
KeyError: 21
dd[a]
      
'asgrsd'
dd["s"]
      
'asgrg'
fs = frozenset([12,125,463,32])
      
fs
      
frozenset({32, 12, 125, 463})
hash(fs)
      
-8129392369090525493
dd
      
{1: 'a', 2.0: 'asdf', 's': 'asgrg', 3: 'asgrsd'}
dd = {1:"a", 2.:"asdf", "s":"asgrg", a:"asgrsd", fs:"sdg"}
      
dd
      
{1: 'a', 2.0: 'asdf', 's': 'asgrg', 3: 'asgrsd', frozenset({32, 12, 125, 463}): 'sdg'}
dd[fs]
      
'sdg'
print(dd)
      
{1: 'a', 2.0: 'asdf', 's': 'asgrg', 3: 'asgrsd', frozenset({32, 12, 125, 463}): 'sdg'}
for k, v in dd:
    print(k, v)

      
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    for k, v in dd:
TypeError: cannot unpack non-iterable int object
for v in dd.values():
    print(v)

      
a
asdf
asgrg
asgrsd
sdg
for v in dd.keys():
    print(v)

      
1
2.0
s
3
frozenset({32, 12, 125, 463})
for k, v in dd.items():
    print(k, ":", v)

      
1 : a
2.0 : asdf
s : asgrg
3 : asgrsd
frozenset({32, 12, 125, 463}) : sdg
dd[1]
      
'a'
dd.get(1)
      
'a'
dd.get(12341)
      
dd[-4] = "sdgrgd"
      
for k, v in dd.items():
    print(k, ":", v)

      
1 : a
2.0 : asdf
s : asgrg
3 : asgrsd
frozenset({32, 12, 125, 463}) : sdg
-4 : sdgrgd
KeyboardInterrupt
for v in dd.items():
    print(v)

      
(1, 'a')
(2.0, 'asdf')
('s', 'asgrg')
(3, 'asgrsd')
(frozenset({32, 12, 125, 463}), 'sdg')
(-4, 'sdgrgd')
dd[0] = 0
      
for v in dd.items():
    print(v)

      
(1, 'a')
(2.0, 'asdf')
('s', 'asgrg')
(3, 'asgrsd')
(frozenset({32, 12, 125, 463}), 'sdg')
(-4, 'sdgrgd')
(0, 0)
dd.keys()
      
dict_keys([1, 2.0, 's', 3, frozenset({32, 12, 125, 463}), -4, 0])
sorted(dd.keys())
      
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    sorted(dd.keys())
TypeError: '<' not supported between instances of 'str' and 'float'
dd[1] = 785
      
dd
      
{1: 785, 2.0: 'asdf', 's': 'asgrg', 3: 'asgrsd', frozenset({32, 12, 125, 463}): 'sdg', -4: 'sdgrgd', 0: 0}
dd.update([55,"sdgdf"])
      
Traceback (most recent call last):
  File "<pyshell#243>", line 1, in <module>
    dd.update([55,"sdgdf"])
TypeError: cannot convert dictionary update sequence element #0 to a sequence
dd.update((55,"sdgdf"))
      
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    dd.update((55,"sdgdf"))
TypeError: cannot convert dictionary update sequence element #0 to a sequence
dd.update(55,"sdgdf")
      
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    dd.update(55,"sdgdf")
TypeError: update expected at most 1 argument, got 2
dd.update({55:"sdgdf"})
      
dd
      
{1: 785, 2.0: 'asdf', 's': 'asgrg', 3: 'asgrsd', frozenset({32, 12, 125, 463}): 'sdg', -4: 'sdgrgd', 0: 0, 55: 'sdgdf'}
dd.update([(2,222), (5,235), (214,12412)])
      
dd
      
{1: 785, 2.0: 222, 's': 'asgrg', 3: 'asgrsd', frozenset({32, 12, 125, 463}): 'sdg', -4: 'sdgrgd', 0: 0, 55: 'sdgdf', 5: 235, 214: 12412}
d = dict(name="jojo", age=888)
      
d
      
{'name': 'jojo', 'age': 888}
dd.update(gdfg="sdg")
      
dd
      
{1: 785, 2.0: 222, 's': 'asgrg', 3: 'asgrsd', frozenset({32, 12, 125, 463}): 'sdg', -4: 'sdgrgd', 0: 0, 55: 'sdgdf', 5: 235, 214: 12412, 'gdfg': 'sdg'}
dd
      
{1: 785, 2.0: 222, 's': 'asgrg', 3: 'asgrsd', frozenset({32, 12, 125, 463}): 'sdg', -4: 'sdgrgd', 0: 0, 55: 'sdgdf', 5: 235, 214: 12412, 'gdfg': 'sdg'}
len(dd)
      
11
d
      
{'name': 'jojo', 'age': 888}
dd.pop(1)
      
785
dd
      
{2.0: 222, 's': 'asgrg', 3: 'asgrsd', frozenset({32, 12, 125, 463}): 'sdg', -4: 'sdgrgd', 0: 0, 55: 'sdgdf', 5: 235, 214: 12412, 'gdfg': 'sdg'}
dd.popitem()
      
('gdfg', 'sdg')
dd
      
{2.0: 222, 's': 'asgrg', 3: 'asgrsd', frozenset({32, 12, 125, 463}): 'sdg', -4: 'sdgrgd', 0: 0, 55: 'sdgdf', 5: 235, 214: 12412}
del dd["s"]
      
dd
      
{2.0: 222, 3: 'asgrsd', frozenset({32, 12, 125, 463}): 'sdg', -4: 'sdgrgd', 0: 0, 55: 'sdgdf', 5: 235, 214: 12412}
2. in dd
      
True
2 in dd
      
True
key = input()
      
ff
ff
      
Traceback (most recent call last):
  File "<pyshell#266>", line 1, in <module>
    ff
NameError: name 'ff' is not defined. Did you mean: 'fs'?
dd
      
{2.0: 222, 3: 'asgrsd', frozenset({32, 12, 125, 463}): 'sdg', -4: 'sdgrgd', 0: 0, 55: 'sdgdf', 5: 235, 214: 12412}
if key in dd:
      dd.pop(kay)

      
if key in dd:
    dd.pop(kay)
else:
      print("Нет")

      
Нет
key = 2.
      
if key in dd:
    dd.pop(kay)
else:
      print("Нет")

      
Traceback (most recent call last):
  File "<pyshell#277>", line 2, in <module>
    dd.pop(kay)
NameError: name 'kay' is not defined. Did you mean: 'key'?
>>> if key in dd:
...     dd.pop(key)
... else:
...       print("Нет")
... 
...       
222
>>> di = {i:i**3 for i in range(50,60)}
...       
>>> di
...       
{50: 125000, 51: 132651, 52: 140608, 53: 148877, 54: 157464, 55: 166375, 56: 175616, 57: 185193, 58: 195112, 59: 205379}
>>> di = {i**3 for i in range(50,60)}
...       
>>> di
...       
{140608, 175616, 205379, 166375, 125000, 185193, 195112, 132651, 148877, 157464}
>>> type(di)
...       
<class 'set'>
