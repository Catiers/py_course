Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
var = []
print(var)
[]
vars = list()
print(vars)
[]
vari = [1, 2, 3, 4, True, "easd"]
vari
[1, 2, 3, 4, True, 'easd']
vari[5]
'easd'
len(vari)
6
vari[1]
2
vari["1"]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    vari["1"]
TypeError: list indices must be integers or slices, not str
vari[9]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    vari[9]
IndexError: list index out of range
type(var)
<class 'list'>
type(vars)
<class 'list'>
type(vari[3])
<class 'int'>
vari[3]
4
print(42, True, vari)
42 True [1, 2, 3, 4, True, 'easd']
sr = "hi"
sr.upper()
'HI'
ue = 8765
ue.upper()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    ue.upper()
AttributeError: 'int' object has no attribute 'upper'
vari.upper()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    vari.upper()
AttributeError: 'list' object has no attribute 'upper'
"fvghbjnmk,l".upper()
'FVGHBJNMK,L'
k = [3, 5, 123, 5243, 354, 123, 435]
k
[3, 5, 123, 5243, 354, 123, 435]
k.append
<built-in method append of list object at 0x00000255407C5AC0>
2
2

k.append(879)
k
[3, 5, 123, 5243, 354, 123, 435, 879]
k.insert(3, 126)
k
[3, 5, 123, 126, 5243, 354, 123, 435, 879]
len(k)
9
k.insert(5, 135)
k
[3, 5, 123, 126, 5243, 135, 354, 123, 435, 879]
k.reverse()
k
[879, 435, 123, 354, 135, 5243, 126, 123, 5, 3]
k.reverse()
k
[3, 5, 123, 126, 5243, 135, 354, 123, 435, 879]
k
k.pop()
879
k
[3, 5, 123, 126, 5243, 135, 354, 123, 435]
as = k.pop(3)
SyntaxError: invalid syntax
aas = k.pop(3)
aas
126
del k[5]
l
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    l
NameError: name 'l' is not defined
;
SyntaxError: invalid syntax
k'
SyntaxError: unterminated string literal (detected at line 1)
k
[3, 5, 123, 5243, 135, 123, 435]
del var
var
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    var
NameError: name 'var' is not defined. Did you mean: 'vars'?
k.remove(2)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    k.remove(2)
ValueError: list.remove(x): x not in list
k.remove(3)
k
[5, 123, 5243, 135, 123, 435]
k.pop(65)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    k.pop(65)
IndexError: pop index out of range
dele = 63
if dele in k:
    k.remove(dele)

    
k.count(123)
2
k.count(89)
0
k
[5, 123, 5243, 135, 123, 435]
k.clear
<built-in method clear of list object at 0x00000255407C5AC0>
k.clear()
k = [5, 123, 5243, 135, 123, 435]
k.index(123)
1
k.index(123, k.index(123)+1)
4
ue
8765
k += ue
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    k += ue
TypeError: 'int' object is not iterable
ue = [12,423,123,1245,345,62]
k += ue
k
[5, 123, 5243, 135, 123, 435, 12, 423, 123, 1245, 345, 62]
req = [3,1,5,7,9,56,2,5,7,8,9]
req
[3, 1, 5, 7, 9, 56, 2, 5, 7, 8, 9]
len(req)
11
req[10]
9
req[-1]
9
req[-11]
3
gaf = [1,2,3,4,5]
len[gaf]
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    len[gaf]
TypeError: 'builtin_function_or_method' object is not subscriptable
gaf = [1,2,3,4,5]
len(gaf)
5
gaf.pop(-1)
5
len(gaf)
4
gaf[2] = input("Введите любое целое число: ")
Введите любое целое число: 3
пфа
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    пфа
NameError: name 'пфа' is not defined
gaf
[1, 2, '3', 4]
gaf[2] = int(input("Введите любое целое число: "))
Введите любое целое число: 2
gaf
[1, 2, 2, 4]
gaf = [1,2,3,4,5]
len(gaf)
5
gaf[2] = int(input("Введите любое целое число: "))
Введите любое целое число: 7
gaf.pop(-1)
5
len(gaf)
4
gaf = [1,2,3,4,5]
len(gaf)
5
gaf[len(gaf)/2] = int(input("Введите любое целое число: "))
Введите любое целое число: 6
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    gaf[len(gaf)/2] = int(input("Введите любое целое число: "))
TypeError: list indices must be integers or slices, not float
gaf[int(len(gaf)/2)] = int(input("Введите любое целое число: "))
Введите любое целое число: 3
gaf
[1, 2, 3, 4, 5]
gaf = [1,2,3,4,5]
len(gaf)
5
gaf[len(gaf)/2] = int(input("Введите любое целое число: "))
Введите любое целое число: 98
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    gaf[len(gaf)/2] = int(input("Введите любое целое число: "))
TypeError: list indices must be integers or slices, not float
gaf = [1,2,3,4,5]
len(gaf)
5
gaf[int(len(gaf)/2)] = int(input("Введите любое целое число: "))
Введите любое целое число: 98
gaf
[1, 2, 98, 4, 5]
gaf.pop(-1)
5
gaf
[1, 2, 98, 4]
len(gaf)
4
gaf
[1, 2, 98, 4]
rint(gaf)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    rint(gaf)
NameError: name 'rint' is not defined. Did you mean: 'print'?
print(gaf)
[1, 2, 98, 4]
for i in gaf:
    print(i)

    
1
2
98
4
asd = []
for i in range(5):
    li.append(int(input("-->")))

    
Traceback (most recent call last):
  File "<pyshell#117>", line 2, in <module>
    li.append(int(input("-->")))
NameError: name 'li' is not defined. Did you mean: 'i'?
for i in range(5):
    asd.append(int(input("-->")))

    
-->2
-->4
-->6
-->2
-->3
asd
[2, 4, 6, 2, 3]
for i in range(int(input("n-->"))):
    asd.append(int(input("v-->")))

    
n-->6
v-->3
v-->1
v-->5
v-->7
v-->5
v-->2
asd
[2, 4, 6, 2, 3, 3, 1, 5, 7, 5, 2]
for val in asd:
    print(val)

    
2
4
6
2
3
3
1
5
7
5
2
for i in range(len(asd)):
    print(asd[i])

    
2
4
6
2
3
3
1
5
7
5
2
summa = 0
for i in range(len(asd));
SyntaxError: invalid syntax
for i in range(len(asd)):
    summa +=asd[i]

    
\

summa
40
summa = 0
for val in asd:
    summa += val

    
summa
40
asd.reverse
<built-in method reverse of list object at 0x00000255432E1B00>
asd.reverse()
asd
[2, 5, 7, 5, 1, 3, 3, 2, 6, 4, 2]
asd.append(123)
print(asd)
[2, 5, 7, 5, 1, 3, 3, 2, 6, 4, 2, 123]
for i in sorted(asd):
    print(i, sep=" ")

    
1
2
2
2
3
3
4
5
5
6
7
123
asd
[2, 5, 7, 5, 1, 3, 3, 2, 6, 4, 2, 123]
for i in sorted(asd):
    print(i, end=" ")

    
1 2 2 2 3 3 4 5 5 6 7 123 
sorted(asd, reverse=True)
[123, 7, 6, 5, 5, 4, 3, 3, 2, 2, 2, 1]
asd
[2, 5, 7, 5, 1, 3, 3, 2, 6, 4, 2, 123]
oi = [3, 12, 63, 5, 213, 5, 1]
a, c = 78, 88
tmp = a
a = b
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    a = b
NameError: name 'b' is not defined
a == b
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    a == b
NameError: name 'b' is not defined
a = c
c = tmp
a
88
c
78
tmp
78
a, c = 76, 87
a, c = c, a
a
87
c
76
oi
[3, 12, 63, 5, 213, 5, 1]
oi = [3, 12, 63, 5, 213, 5, 1]
oi[3], oi[1] = oi[1], oi[3]
oi
[3, 5, 63, 12, 213, 5, 1]
oi[2], oi[3] = oi[3], oi[2]
oi
[3, 5, 12, 63, 213, 5, 1]
oi[6], oi[0] = oi[0], oi[6]
oi
[1, 5, 12, 63, 213, 5, 3]
oi
[1, 5, 12, 63, 213, 5, 3]
max(oi)
213
min(oi)
1
sum(oi)
302
\
sum(oi)/len(oi)
43.142857142857146
ui = [1,2,3,4]
gh = ui
gh
[1, 2, 3, 4]
ui
[1, 2, 3, 4]
id(gh)
2565222635072
id(ui)
2565222635072
gh[1] = 32
ui
[1, 32, 3, 4]
gh = ui.copy()
id(gh)
2565222529792
id(ui)
2565222635072
gh[1] = 2
gh
[1, 2, 3, 4]
ui
[1, 32, 3, 4]
gh = ui[:]
gh
[1, 32, 3, 4]
id(gh)
2565222647936
id(ui)
2565222635072
ui = [1,2,3,4]
ui[:3]
[1, 2, 3]
ui[1:]
[2, 3, 4]
ui += ui
ui
[1, 2, 3, 4, 1, 2, 3, 4]
kk = li[::2]
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    kk = li[::2]
NameError: name 'li' is not defined. Did you mean: 'i'?
kk =ui[::2}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
kk = ui[::2]
kk
[1, 3, 1, 3]
ui
[1, 2, 3, 4, 1, 2, 3, 4]
ui[::-1]
[4, 3, 2, 1, 4, 3, 2, 1]
se = {}
type(se)
<class 'dict'>
se = set{}
SyntaxError: invalid syntax
se = set{}
SyntaxError: invalid syntax
se = set()
type(se)
<class 'set'>
se = {"da", 1, 23, 123, 1235, 12312, 1, 1, 1, 1,}
se
{1, 'da', 1235, 23, 12312, 123}
se.add(1)
se
{1, 'da', 1235, 23, 12312, 123}
for v in se:
    print(v, end=" ")

    
1 da 1235 23 12312 123 
999 in s
Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    999 in s
NameError: name 's' is not defined. Did you mean: 'sr'?
999 in se
False
1 in se
True
se.update({1,2,3,63,234,234,1})
se
{1, 2, 3, 234, 'da', 1235, 23, 12312, 123, 63}
se.clear()
se
set()
se = {1, 2, 3, 234, 'da', 1235, 23, 12312, 123, 63}
se.remove(444)
Traceback (most recent call last):
  File "<pyshell#234>", line 1, in <module>
    se.remove(444)
KeyError: 444
se.remove(1)
se
{2, 3, 234, 'da', 1235, 23, 12312, 123, 63}
se.discard(2)
se
{3, 234, 'da', 1235, 23, 12312, 123, 63}
'
len(se)
8
oi
[1, 5, 12, 63, 213, 5, 3]
oi = list(set(oi))
oi
[1, 3, 5, 12, 213, 63]
set(oi)
{1, 3, 5, 12, 213, 63}
list(se)
[3, 234, 'da', 1235, 23, 12312, 123, 63]
st
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    st
NameError: name 'st' is not defined. Did you mean: 'sr'?
sr
'hi'
list(sr)
['h', 'i']
set(sr)
{'h', 'i'}
se
{3, 234, 'da', 1235, 23, 12312, 123, 63}
sr
'hi'
print(oi)
[1, 3, 5, 12, 213, 63]
str(oi)
'[1, 3, 5, 12, 213, 63]'
ppp = str(oi)
ui
[1, 2, 3, 4, 1, 2, 3, 4]
ppp
'[1, 3, 5, 12, 213, 63]'
list(ppp)
['[', '1', ',', ' ', '3', ',', ' ', '5', ',', ' ', '1', '2', ',', ' ', '2', '1', '3', ',', ' ', '6', '3', ']']
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list = set(my_list)
,y_list
SyntaxError: invalid syntax
my_list
{1, 2, 4, 6, 9}
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list[::-1]
[9, 2, 6, 2, 4, 1, 4, 4, 2, 1]
oi
[1, 3, 5, 12, 213, 63]
resList = []
for v in oi:
    resList.append(v**2)

    
oi
[1, 3, 5, 12, 213, 63]
resList
[1, 9, 25, 144, 45369, 3969]
oi
[1, 3, 5, 12, 213, 63]
resList = [v**2 for v in oi]
resList
[1, 9, 25, 144, 45369, 3969]
oi = [1,2,3,4,5,6,7,8,9,10]
resList = [v**2 for v in oi if v%2==0]
resList
[4, 16, 36, 64, 100]
number = [int(input("-->")) for i in range(int(input("n-->")))]
n-->8
-->6
-->8
-->9
-->0
-->8
-->5
-->4
-->3

number
[6, 8, 9, 0, 8, 5, 4, 3]
number = []
n = int(input("n-->"))
n-->3
for i in range(n):
    numbers.append(int(input("-->")))

    
Traceback (most recent call last):
  File "<pyshell#283>", line 2, in <module>
    numbers.append(int(input("-->")))
NameError: name 'numbers' is not defined. Did you mean: 'number'?
for i in range(n):
    number.append(int(input("-->")))

-->
Traceback (most recent call last):
  File "<pyshell#285>", line 2, in <module>
    number.append(int(input("-->")))
ValueError: invalid literal for int() with base 10: ''
for i in range(n):
    number.append(int(input("-->")))

    
-->3
-->4
-->5
number
[3, 4, 5]
li = input("x x x : --> ")
x x x : --> 2 2 2
li
'2 2 2'
li = li.split()
li
['2', '2', '2']
li = [int(v) for v in li]
li
[2, 2, 2]
sum(li)
6
li = [int(v) for v in input("x x x : --> ").split()]
x x x : --> 2 3 4
li
[2, 3, 4]
suma = sum([int(v) for v in input("x x x : --> ").split()])
x x x : --> 2 3 4
suma
9
li = [1,2,3,4]
>>> li = [[],[],[]]
>>> li = [[1,2,3],[11,24,12],[4,1,5]]
>>> li[0]
[1, 2, 3]
>>> li[0[0]]
Traceback (most recent call last):
  File "<pyshell#304>", line 1, in <module>
    li[0[0]]
TypeError: 'int' object is not subscriptable
>>> li[0][2]
3
>>> li[1][1]
24
>>> li
[[1, 2, 3], [11, 24, 12], [4, 1, 5]]
>>> li[0].append(1235)
>>> li
[[1, 2, 3, 1235], [11, 24, 12], [4, 1, 5]]
>>> li[0][2] = 125
>>> li
[[1, 2, 125, 1235], [11, 24, 12], [4, 1, 5]]
>>> li = [[[1],[2],[3]],[[11],[22],[33]],[[111],[222],[333]]]
>>> li
[[[1], [2], [3]], [[11], [22], [33]], [[111], [222], [333]]]
>>> li[0][0].clear()
>>> li
[[[], [2], [3]], [[11], [22], [33]], [[111], [222], [333]]]
