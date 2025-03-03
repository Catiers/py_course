Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1/0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
s = "wte"
s.capitalize    ()
'Wte'
s.decapitalize()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s.decapitalize()
AttributeError: 'str' object has no attribute 'decapitalize'. Did you mean: 'capitalize'?
li = [1,2,3]
li[0.5]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    li[0.5]
TypeError: list indices must be integers or slices, not float
1 /0
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    1 /0
ZeroDivisionError: division by zero
try:
    1/0
except:
    print(-1)

    
-1
try:
    li = [1,2,3]
    li[0.5]
except:
    print(-1)

    
-1
try:
    int("sfg34gsdf")
except:
    print(-1)

    
-1
try:
    int("sfg34gsdf")
except ValueError:
    print("ValueError")
except:
    print(-1)

    
ValueError
try:
    1/0
except ZeroDivisionError:
    print("ZeroDivisionError X/0")
except ValueError:
    print("ValueError")
except:
    print(-1)

    
ZeroDivisionError X/0
try:
    1/0
except ZeroDivisionError:
    print("ZeroDivisionError X/0")
except ValueError:
    print("ValueError")

    
ZeroDivisionError X/0
try:
    int("sfg34gsdf")
except ZeroDivisionError:
    print("ZeroDivisionError X/0")
except ValueError:
    print("ValueError")

    
ValueError
try:
    li[0.5]
except ZeroDivisionError:
    print("ZeroDivisionError X/0")
except ValueError:
    print("ValueError")

    
Traceback (most recent call last):
  File "<pyshell#29>", line 2, in <module>
    li[0.5]
TypeError: list indices must be integers or slices, not float
try:
    li[0.5]
except ZeroDivisionError:
    print("ZeroDivisionError X/0")
except ValueError:
    print("ValueError")
except:
    print(-1)

    
-1
try:
    li[0.5]
except:
    print(-1)
except ZeroDivisionError:
    print("ZeroDivisionError X/0")
except ValueError:
    print("ValueError")

SyntaxError: default 'except:' must be last
try:
    try:
        li[0.5]
    except ZeroDivisionError:
        print("ZeroDivisionError X/0")
    except ValueError:
        print("ValueError")
    except:
        print(-1)
except:
    print(-1)

    
-1
try:
    try:
        li[0.5]
    except:
        print(-1)
    except ZeroDivisionError:
        print("ZeroDivisionError X/0")
    except ValueError:
        print("ValueError")
except:
    print(-1)
    
SyntaxError: incomplete input

try:
    li[0.5]
except ZeroDivisionError as zde:
    print("ZeroDivisionError X/0", zde.args)
except ValueError as ve:
    print("ValueError", ve.args)
except:
    print(-1)

    
-1
try:
    13 / 0
except ZeroDivisionError as zde:
    print("ZeroDivisionError X/0", zde.args)
except ValueError as ve:
    print("ValueError", ve.args)
except:
    print(-1)

    
ZeroDivisionError X/0 ('division by zero',)
try:
    int("2142g")
except ZeroDivisionError as zde:
    print("ZeroDivisionError X/0", zde.args)
except ValueError as ve:
    print("ValueError", ve.args)
except:
    print(-1)

    
ValueError ("invalid literal for int() with base 10: '2142g'",)
try:
    raise ValueError
except ZeroDivisionError as zde:
    print("ZeroDivisionError X/0", zde.args)
except ValueError as ve:
    print("ValueError", ve.args)
except:
    print(-1)

    
ValueError ()
try:
    raise ZeroDivisionError
except ZeroDivisionError as zde:
    print("ZeroDivisionError X/0", zde.args)
except ValueError as ve:
    print("ValueError", ve.args)
except:
    print(-1)

    
ZeroDivisionError X/0 ()
raise IndexError
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    raise IndexError
IndexError
try:
    123 / 0
except (ValueError, ZeroDivisionError):
    print("ZeroDivisionError OR ValueError")
except:
    print(-1)

    
ZeroDivisionError OR ValueError
try:
    raise ValueError
except (ValueError, ZeroDivisionError):
    print("ZeroDivisionError OR ValueError")
except:
    print(-1)

    
ZeroDivisionError OR ValueError
import ewrwegds
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    import ewrwegds
ModuleNotFoundError: No module named 'ewrwegds'
a = 6
if a == 8:
    try:
        import time
    except:
        pass
else:
    print("Делай без time")

    
Делай без time
a = 8
if a == 8:
    try:
        import time
    except:
        pass
else:
    print("Делай без time")

    
try:
    raise ZeroDivisionError
except:
    print("default")

    
default
try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("default")

    
ZeroDivisionError
try:
    raise ZeroDivisionError
except ArithmeticError:
    print("ArithmeticError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("default")

    
ArithmeticError
try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except:
    print("default")

    
ZeroDivisionError
try:
    raise ZeroDivisionError
except Exception as e:
    print(e.args)
except:
    print("default")

    
()
try:
    raise ZeroDivisionError('1/0')
except Exception as e:
    print(e.args)
except:
    print("default")

    
('1/0',)
try:
    raise IndexError("[5] out of the range")
except Exception as e:
    print(e.args)
except:
    print("default")

    
('[5] out of the range',)
def a(x):
    try:
        res = int(x)
    except:
        print("123")

        
a(123)
a("43gzdf")
123
def a(x):
    try:
        res = int(x)
    except:
        print("123")
        raise

    
a(123)
a("23g2")
123
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a("23g2")
  File "<pyshell#106>", line 3, in a
    res = int(x)
ValueError: invalid literal for int() with base 10: '23g2'
def b(x):
    try:
        a(x)
    except:
        print("312")
        raise

    
>>> 
>>> b(231)
>>> b("23g")
123
312
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    b("23g")
  File "<pyshell#114>", line 3, in b
    a(x)
  File "<pyshell#106>", line 3, in a
    res = int(x)
ValueError: invalid literal for int() with base 10: '23g'
>>> assert 1
>>> assert 0
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    assert 0
AssertionError
>>> assert ""
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    assert ""
AssertionError
>>> assert []
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    assert []
AssertionError
>>> assert "3"
>>> assert [1]
>>> res = 10
>>> assert res == 10
>>> res = 11
>>> assert res == 10
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    assert res == 10
AssertionError
