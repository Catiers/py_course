Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
count = 1
while count < 10:
    count += 2
    if count == 5:
        print("go")
        continue
    print("exit")

exit
go
exit
exit
exit
while count < 10:
    count += 2
    if count == 5:
        print("go")
        continue
    print(count)

count = 1
while count < 10:
    count += 2
    if count == 5:
        print("go")
        continue
    print(count)

3
go
7
9
11
for i in range(5):
    print(i)

0
1
2
3
4
for i in range(1, 9, 2):
    print(i)

1
3
5
7
for i in range(4, 9):
    print(i)

    
4
5
6
7
8
import time
time.sleep(3)
for i in range(4, 9):
    print("sleep",i)
    time.sleep(1)

    
sleep 4
sleep 5
sleep 6
sleep 7
sleep 8
da = " hi 534"
to_find = "2"
to_find in da
False
to_find = "3"
to_find in da
True
if to_find in st:
    print("3 in st")
else:
    print("nope")

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    if to_find in st:
NameError: name 'st' is not defined. Did you mean: 'set'?
if to_find in da:
    print("3 in st")
else:
    print("nope")

    
3 in st
noPri = "вапролдж"
word = input("give me your words: ")
give me your words: всеп мирнгигошщшльошрнеакек ыва
word
'всеп мирнгигошщшльошрнеакек ыва'
for char in word:
    print(char)

    
в
с
е
п
 
м
и
р
н
г
и
г
о
ш
щ
ш
л
ь
о
ш
р
н
е
а
к
е
к
 
ы
в
а
for char in word:
    if char in noPri:
        continue
    print(char)

    
с
е
 
м
и
н
г
и
г
ш
щ
ш
ь
ш
н
е
к
е
к
 
ы
for char in word:
    if char not in noPri:
        continue
    print(char)

    
в
п
р
о
л
о
р
а
в
а
for char in word:
    if char in noPri:
        continue
    print(char)
else:
    print("dead...")

    
с
е
 
м
и
н
г
и
г
ш
щ
ш
ь
ш
н
е
к
е
к
 
ы
dead...
for char in word:
    if char in noPri:
        break
    print(char)
else:
    print("dead...")

    
age = 23
money = 1000
if age > 18 and money >= 900:
    prind("Good")

    
Traceback (most recent call last):
  File "<pyshell#57>", line 2, in <module>
    prind("Good")
NameError: name 'prind' is not defined. Did you mean: 'print'?
if age > 18 and money >= 900:
    print("Good")

    
Good
age = 16
if age > 18 and money >= 900:
    print("Good")

    
age = 21
if age > 18 or money >= 900:
    print("Good")

    
Good
if age > 18 and money >= 900:
    print("Good")

    
Good
age = 16
if age > 18 and money >= 900:
    print("Good")

    
if age > 18 or money >= 900:
    print("Good")

    
Good
money = 100
if age > 18 or money >= 900:
    print("Good")

    
age = 21
>>> if age > 18 or money >= 900:
...     print("Good")
... 
...     
Good
>>> not True
False
>>> not False
True
>>> age
21
>>> age >15
True
>>> not age >15
False
>>> not not not False
True
>>> 60
60
>>> number = int("10101001010101", 2)
>>> number
10837
>>> number2 = int("11101001011001", 2)
>>> number2
14937
>>> number = int("10101001010101", 2)
>>> number2 = int("11101001011001", 2)
>>> bin(number)
'0b10101001010101'
>>> bin(number2)
'0b11101001011001'
>>> bin(number & number2)  # 10101001010001
'0b10101001010001'
>>> bin(number & number2)  # 11101001011101
'0b10101001010001'
>>> bin(number | number2)  # 11101001011101
'0b11101001011101'
>>> bin(number ^ number2)  # 01000000001000
'0b1000000001100'
