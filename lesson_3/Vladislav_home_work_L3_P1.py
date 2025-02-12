Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> gaf = [1,2,3,4,5]
... len(gaf)
... 5
... gaf[int(len(gaf)/2)] = int(input("Введите любое целое число: "))
... Введите любое целое число: 98
... gaf
... [1, 2, 98, 4, 5]
... gaf.pop(-1)
... 5
... gaf
... [1, 2, 98, 4]
... len(gaf)
... 4
... gaf
... [1, 2, 98, 4]
... rint(gaf)
... Traceback (most recent call last):
...   File "<pyshell#109>", line 1, in <module>
...     rint(gaf)
... NameError: name 'rint' is not defined. Did you mean: 'print'?
... print(gaf)
... [1, 2, 98, 4]
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> gaf = [1,2,3,4,5]
>>> len(gaf)
5
>>> gaf[int(len(gaf)/2)] = int(input("Введите любое целое число: "))
Введите любое целое число: 896
>>> gaf.pop()
5
>>> len(gaf)
4
>>> print(gaf)
[1, 2, 896, 4]
