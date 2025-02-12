C:\Windows\System32>py
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print
<built-in function print>
>>> print()

>>> print "Hello world!"
  File "<stdin>", line 1
    print "Hello world!"
    ^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>>
>>> print("Hello world!")
Hello world!
>>> Print("Hello world!")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> print "Hello world!")
  File "<stdin>", line 1
    print "Hello world!")
                        ^
SyntaxError: unmatched ')'
>>> print "Hello\nworld!")
  File "<stdin>", line 1
    print "Hello\nworld!")
                         ^
SyntaxError: unmatched ')'
>>> print ("Hello\nworld!")
Hello
world!
>>> print ("\tHello\nworld!")
        Hello
world!
>>> print ("\tHello\n"world!"")
  File "<stdin>", line 1
    print ("\tHello\n"world!"")
           ^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print ("\tHello\n'world!'")
        Hello
'world!'
>>> print ("Hm\tHello\n'world!'")
Hm      Hello
'world!'
>>> print ("Hm\tHello\nnn'world!'")
Hm      Hello
nn'world!'
>>> print ("Hm\tHello\nn'world!'")
Hm      Hello
n'world!'
>>> print ("Hm\tHello\n\nn'world!'")
Hm      Hello

n'world!'
>>> print ("Hm\tHello\n'world!'")
Hm      Hello
'world!'
>>> print ("Hm\tHello\n'world!'","alright","Goog")
Hm      Hello
'world!' alright Goog
>>> print ("Hm\tHello\n'world!'","alright","Goog")
Hm      Hello
'world!' alright Goog
>>> print(1,2,3,4,5,6,7)
1 2 3 4 5 6 7
>>> print(1, 2, 3, 4, 5, 6, 7, sep="***")
1***2***3***4***5***6***7
>>> print(1, 2, 3, 4, 5, 6, 7, sep="*")
1*2*3*4*5*6*7
>>> print()

>>> print(end="\n\n\n")



>>> print(end="\n\n\n", sep="*")



>>> print(1, 2, 4, "hi", end="*******", sep="+")
1+2+4+hi*******>>> print(1, 2, 4, "hi", end="*******\n", sep="+")
1+2+4+hi*******
>>> print("Programming", "Esesntial", "in", sep="***", end="...Python")
Programming***Esesntial***in...Python>>> print("Programming", "Essential", "in", sep="***", end="...Python")
Programming***Essential***in...Python>>> print("Programming", "Essential", "in", sep="***", end="...Python\n")
Programming***Essential***in...Python
>>> print("Programming", "Essential", "in", sep="***", end="...Python\n")
Programming***Essential***in...Python
>>> print(11_111)
11111
>>> print(11_111-32)
11079
>>> print(0o123)
83
>>> print(2,3)
2 3
>>> print(2.3)
2.3
>>> print(2e3)
2000.0
>>> print(2E3)
2000.0
>>> print(2E3)
2000.0
>>> print(2.e3)
2000.0
>>> print("""hi
... 543
... html
... \n
... 234123")
...
...
... efs""")
hi
543
html


234123")


efs
>>> print(""""I'm"
... ""Learning""
... """Python"""
  File "<stdin>", line 3
    """Python"""
             ^
SyntaxError: unterminated triple-quoted string literal (detected at line 3)
>>> print(""""I'm"
... ""Learning""
... """, end=""""Python"""")
  File "<stdin>", line 3
    """, end=""""Python"""")
                          ^
SyntaxError: unterminated string literal (detected at line 3)
>>> print(""""I'm"
...
... asd"""
... """)
... asd
... asd""")
"I'm"

asd)
asd
asd
>>> print("""
... "I'm"
... ""Learning""
... \"""Python\""")
... """)

"I'm"
""Learning""
"""Python""")

>>> name = "Vladislav"
>>> print(name)
Vladislav
>>> 1cat = 77
  File "<stdin>", line 1
    1cat = 77
    ^
SyntaxError: invalid decimal literal
>>> print(1cat)
  File "<stdin>", line 1
    print(1cat)
          ^
SyntaxError: invalid decimal literal
>>> my dog =99
  File "<stdin>", line 1
    my dog =99
       ^^^
SyntaxError: invalid syntax
>>> sdf+f4=2345
  File "<stdin>", line 1
    sdf+f4=2345
    ^^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> 342&2f=231
  File "<stdin>", line 1
    342&2f=231
        ^
SyntaxError: invalid decimal literal
>>> name
'Vladislav'
>>> name = True
>>> type(name)
<class 'bool'>
>>> name = 234*3
>>> name
702
>>> type(name)
<class 'int'>
>>> x=4234
>>> y=523
>>> c=123
>>> z="qwerty"
>>> result = x+y+c
>>> result
4880
>>> a,b,c=153,346,234
>>> q=w=e=r=t=y=234
>>> q
234
>>> w
234
>>> e
234
>>> r
234
>>> t
234
>>> y
234
>>> y
234
>>> 5 * (9/3) +432
447.0
>>> John = 35
>>> Mary = 32
>>> Adam = 12
>>> total_apples = John + Mary + Adam
>>> total_apples
79
>>> John = 35
>>> Mary = 32
>>> Adam = 12
>>> total_apples = John + Mary + Adam
>>>