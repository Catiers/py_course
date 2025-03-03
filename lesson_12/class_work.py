Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print()

print(1,2,3,4)
1 2 3 4
print(2)
2
def Pront(values):
    for val in values:
        print(val, end=" ")
    print()

    
Pront([1,2,4,5])
1 2 4 5 
Pront("sdgsdf")
s d g s d f 
Pront(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    Pront(1,2,3,4)
TypeError: Pront() takes 1 positional argument but 4 were given
def Pront(*values):
    for val in values:
        print(val, end=" ")
    print()

    
Pront(1,2,4,5)
1 2 4 5 
Pront("dsgsdf")
dsgsdf 
def Pront(*values):
    print(type(values))
    for val in values:
        print(val, end=" ")
    print()

    
Pront(1,2,4,5)
<class 'tuple'>
1 2 4 5 
Pront(1,2,4,5, [1,2,4,6], "fdsgdf")
<class 'tuple'>
1 2 4 5 [1, 2, 4, 6] fdsgdf 
print(1,2,4,5, [1,2,4,6], "fdsgdf")
1 2 4 5 [1, 2, 4, 6] fdsgdf
def Pront(*args):
    print(type(args))
    
    for val in args:
        print(val, end=" ")
    print()

    
Pront(1,2,4,5, [1,2,4,6], "fdsgdf")
<class 'tuple'>
1 2 4 5 [1, 2, 4, 6] fdsgdf 
Pront([1,2,4,6])
<class 'tuple'>
[1, 2, 4, 6] 
Pront(1,2,4,5, [1,2,4,6], "fdsgdf")
<class 'tuple'>
1 2 4 5 [1, 2, 4, 6] fdsgdf 
def Pront(*args):
    print(type(args))
    print(args)
    
    for val in args:
        print(val, end=" ")
    print()

    
Pront(1,2,4,5, [1,2,4,6], "fdsgdf")
<class 'tuple'>
(1, 2, 4, 5, [1, 2, 4, 6], 'fdsgdf')
1 2 4 5 [1, 2, 4, 6] fdsgdf 
a,b, *c = [1,2,3,4,5]
a
1
b
2
c
[3, 4, 5]
def Pront(*args, sep1 = " ", end1 = "\n"):
    
    for val in args:
        print(val, sep = sep1, end=end1)
    print()

    
def Pront(*args, sep1 = " ", end1 = "\n"):
    
    for val in args:
        print(val, sep = sep1)
    print( end=end1)

    
Pront(1,2,4,5, [1,2,4,6], "fdsgdf")
1
2
4
5
[1, 2, 4, 6]
fdsgdf

def Pront(*args, sep1 = " ", end1 = "\n"):
    
    for val in args:
        print(val, sep = sep1, end = " ")
    print( end=end1)

    
Pront(1,2,4,5, [1,2,4,6], "fdsgdf")
1 2 4 5 [1, 2, 4, 6] fdsgdf 
def Pront(*args, sep1 = " ", end1 = "\n"):
    
    for val in args:
        print(val, end = sep1)
    print( end=end1)

    
Pront(1,2,4,5, [1,2,4,6], "fdsgdf")
1 2 4 5 [1, 2, 4, 6] fdsgdf 


def balances(**balance):
    print(balance)
    print(type(balance))
    for k, w in balance.items():
        print(f"\t{k}:{w}")
    print()

    
balance(1,2,3,45)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    balance(1,2,3,45)
NameError: name 'balance' is not defined. Did you mean: 'balances'?
balances(1,2,3,4,54)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    balances(1,2,3,4,54)
TypeError: balances() takes 0 positional arguments but 5 were given
balances(name="Vasz", cash=12512)
{'name': 'Vasz', 'cash': 12512}
<class 'dict'>
	name:Vasz
	cash:12512

def numbers(name="Joe",*args,**kwargs):
    print(name)
    print(args)
    print(kwargs)

    
numbers()
Joe
()
{}
def numbers(args,kwargs,name="Joe"):
    print(name)
    print(args)
    print(kwargs)

    
numbers()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    numbers()
TypeError: numbers() missing 2 required positional arguments: 'args' and 'kwargs'
def numbers(name="Joe",*args,**kwargs):
    print(name)
    print(args)
    print(kwargs)

  
numbers()
Joe
()
{}
numbers("Hloya",13,2,3,5,6,3,"rhgrthr",age=100,apples=99)
Hloya
(13, 2, 3, 5, 6, 3, 'rhgrthr')
{'age': 100, 'apples': 99}
def numbers(name="Joe",**kwargs,*args):
    print(name)
    print(args)
    print(kwargs)
    
SyntaxError: arguments cannot follow var-keyword argument

def num_sum(*args):
    s = 0
    for i in args:
        s += i
    print(s)

    
def numbers(*args,**kwargs):
    print(args)
    print(kwargs)
    num_sum(args)

    
numbers(1,2,4,5,6)
(1, 2, 4, 5, 6)
{}
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    numbers(1,2,4,5,6)
  File "<pyshell#78>", line 4, in numbers
    num_sum(args)
  File "<pyshell#75>", line 4, in num_sum
    s += i
TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
def num_sum(*args):
    print(args)
    s = 0
    for i in args:
        s += i
    print(s)

    
def numbers(*args,**kwargs):
    print(args)
    print(kwargs)
    num_sum(args)

    
numbers(1,2,4,5,6)
(1, 2, 4, 5, 6)
{}
((1, 2, 4, 5, 6),)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    numbers(1,2,4,5,6)
  File "<pyshell#83>", line 4, in numbers
    num_sum(args)
  File "<pyshell#81>", line 5, in num_sum
    s += i
TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
def numbers(*args,**kwargs):
    print(args)
    print(kwargs)
    num_sum(*args)

    
numbers(1,2,4,5,6)
(1, 2, 4, 5, 6)
{}
(1, 2, 4, 5, 6)
18
li1, li2 = [1,2,3], [4,5,6]
li1
[1, 2, 3]
li2
[4, 5, 6]
li3 = li1+li2
li3
[1, 2, 3, 4, 5, 6]
li3 = [li1, li2]
li3
[[1, 2, 3], [4, 5, 6]]
li3 = [*li1, *li2]
li3
[1, 2, 3, 4, 5, 6]
st = "sdgfsdgdf"
li = [st]
li = [*st]
li
['s', 'd', 'g', 'f', 's', 'd', 'g', 'd', 'f']
di = {"1":2, "2":3}
di1 = {"11":22, "22":33}
di3 = {**di, **di1}
di3
{'1': 2, '2': 3, '11': 22, '22': 33}
*ttt, = "sdfgdfg"
ttt
['s', 'd', 'f', 'g', 'd', 'f', 'g']
*ttt = "sdgdfb"
SyntaxError: starred assignment target must be in a list or tuple
a, *ttt = "sdgsfd"
a
's'
ttt
['d', 'g', 's', 'f', 'd']
# b^2 - 4*a*c
def D(b,a,c):
    return b**2 - 4*a*c
d
SyntaxError: invalid syntax
def D(b,a,c):
    return b**2 - 4*a*c

D
<function D at 0x000002C9F563CF40>
lambda: 2
<function <lambda> at 0x000002C9F563C040>
def retTwo():
    return 2
retTwo()
SyntaxError: invalid syntax
def retTwo():
    return 2

retTwo()
2
(lambda: 2)()
2
lambda a,b,c: a*b-c
<function <lambda> at 0x000002C9F563F9C0>
(lambda a,b,c: a*b-c)
<function <lambda> at 0x000002C9F563C0E0>
(lambda a,b,c: a*b-c)()
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    (lambda a,b,c: a*b-c)()
TypeError: <lambda>() missing 3 required positional arguments: 'a', 'b', and 'c'
(lambda a,b,c: a*b-c)(1,2,3)
-1
def cond(z,x,y,b,a,c):
    return z+x+y + ((lambda b,a,c: b**2 - 4*a*c)(b,a,c))

cond(1,2,3, 4,5,6)
-98
li = [2,3,5,7,4,2]
for i in li:
    print(i)

    
2
3
5
7
4
2
li_iter = iter(li)
li_iter
<list_iterator object at 0x000002C9F55E7280>
next(li_iter)
2
next(li_iter)
3
next(li_iter)
5
next(li_iter)
7
next(li_iter)
4
next(li_iter)
2
next(li_iter)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    next(li_iter)
StopIteration
next(li_iter)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    next(li_iter)
StopIteration
next(li_iter)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    next(li_iter)
StopIteration
s = "dfgdfg"
s_iter = iter(s)
s_iter
<str_ascii_iterator object at 0x000002C9F5619780>
next(s_iter)
'd'
next(s_iter)
'f'
next(s_iter)
'g'
next(s_iter)
'd'
next(s_iter)
'f'
next(s_iter)

next(s_iter)
'g'
next(s_iter)
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    next(s_iter)
StopIteration
class powFive:
    def __init__(self,maxn):
        self.maxn = maxn

        
class powFive:
    def __init__(self,maxn):
        self.maxn = maxn
KeyboardInterrupt
class powFive:
    def __init__(self,maxn):
        self.maxn = maxn
    def __iter__(self):
        self.counter = 1
        return self
    def __next__(self):
        if self.counter <= self.maxn:
            res = 5 ** self.counter
            self.counter += 1
            return res
        raise StopIteration

    
p = powFive(15)
p
<__main__.powFive object at 0x000002C9F5101AD0>
p_iter = iter(p)
next(p_iter)
5
next(p_iter)
25
next(p_iter)
125
next(p_iter)
625
next(p_iter)
3125
next(p_iter)
15625
next(p_iter)
78125
next(p_iter)
390625
next(p_iter)

next(p_iter)
1953125
next(p_iter)
9765625
next(p_iter)
48828125
next(p_iter)
244140625
next(p_iter)
1220703125
next(p_iter)
6103515625
next(p_iter)
30517578125
next(p_iter)
Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    next(p_iter)
  File "<pyshell#177>", line 12, in __next__
    raise StopIteration
StopIteration
p = powFive(5)
p_iter = iter(p)
next(p_iter)
5
next(p_iter)
25
next(p_iter)
125
next(p_iter)
625
next(p_iter)
3125
next(p_iter)
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    next(p_iter)
  File "<pyshell#177>", line 12, in __next__
    raise StopIteration
StopIteration
p = powFive(5)
for i in p:
    print(i)

    
5
25
125
625
3125
li = [i**2 for i in range(10)]
li
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
li
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
gen = (i**2 for i in range(10))
gen
<generator object <genexpr> at 0x000002C9F5608AD0>
gen()
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    gen()
TypeError: 'generator' object is not callable
for val in gen:
    print(val)

    
0
1
4
9
16
25
36
49
64
81
gen
<generator object <genexpr> at 0x000002C9F5608AD0>
gen()
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    gen()
TypeError: 'generator' object is not callable
for val in gen:
    print(val)

    
gen = (i**2 for i in range(10))
\
next(gen)
0
next(gen)

1
next(gen)

4
next(gen)

9
next(gen)

16
next(gen)
25
next(gen)
36
next(gen)
49
next(gen)
64
next(gen)
81
next(gen)
Traceback (most recent call last):
  File "<pyshell#234>", line 1, in <module>
    next(gen)
StopIteration
next(gen)
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    next(gen)
StopIteration
gen = (i**2 for i in range(10))

li = [i**2 for i in gen]

li
[0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561]
def retNumber(n):
    for i in range(n):
        return i

    
r = retNumber(4)
r
0
def retNumber(n):
    for i in range(n):
        yield i

        
def retNumber(n):
    for i in range(n):
        yield i**2

        
r = retNumber(5)
r
<generator object retNumber at 0x000002C9F5609150>
next(r)
0
next(r)
1
next(r)
4
next(r)
9
next(r)
16
next(r)
Traceback (most recent call last):
  File "<pyshell#258>", line 1, in <module>
    next(r)
StopIteration
next(r)
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    next(r)
StopIteration
for i in retNumber(10):
    print(i)

    
0
1
4
9
16
25
36
49
64
81
def mulFive(n):
    return n * 5

li = [1,2,5,3]
res_li = list(map(mulFive, li))
res_li
[5, 10, 25, 15]
def a():
    x = 10

    
def a():
    x = 10
    
    def inner(number):
        return number**x
    
    return inner

res = a()
res
<function a.<locals>.inner at 0x000002C9F562D4E0>
res(5)
9765625
def numPowTwo():
    num = 0
    def inner():
        nonlocal num
        num **= 2
        return num
    return inner

res = numPowTwo()
res
<function numPowTwo.<locals>.inner at 0x000002C9F562DB20>
res()
0
def numPowTwo():
    num = 2
    def inner():
        nonlocal num
        num **= 2
        return num
    return inner

res = numPowTwo()
res()
4
res()
16
res()
256
res()
65536
res()

res()
4294967296
res()
18446744073709551616
res()
340282366920938463463374607431768211456
res()
115792089237316195423570985008687907853269984665640564039457584007913129639936
res()
13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084096
res()
179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137216
res()
32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385521914333389668342420684974786564569494856176035326322058077805659331026192708460314150258592864177116725943603718461857357598351152301645904403697613233287231227125684710820209725157101726931323469678542580656697935045997268352998638215525166389437335543602135433229604645318478604952148193555853611059596230656
import sys
res()
1044388881413152506691752710716624382579964249047383780384233483283953907971557456848826811934997558340890106714439262837987573438185793607263236087851365277945956976543709998340361590134383718314428070011855946226376318839397712745672334684344586617496807908705803704071284048740118609114467977783598029006686938976881787785946905630190260940599579453432823469303026696443059025015972399867714215541693835559885291486318237914434496734087811872639496475100189041349008417061675093668333850551032972088269550769983616369411933015213796825837188091833656751221318492846368125550225998300412344784862595674492194617023806505913245610825731835380087608622102834270197698202313169017678006675195485079921636419370285375124784014907159135459982790513399611551794271106831134090584272884279791554849782954323534517065223269061394905987693002122963395687782878948440616007412945674919823050571642377154816321380631045902916136926708342856440730447899971901781465763473223850267253059899795996090799469201774624817718449867455659250178329070473119433165550807568221846571746373296884912819520317457002440926616910874148385078411929804522981857338977648103126085903001302413467189726673216491511131602920781738033436090243804708340403154190336
res()
1090748135619415929462984244733782862448264161996232692431832786189721331849119295216264234525201987223957291796157025273109870820177184063610979765077554799078906298842192989538609825228048205159696851613591638196771886542609324560121290553901886301017900252535799917200010079600026535836800905297805880952350501630195475653911005312364560014847426035293551245843928918752768696279344088055617515694349945406677825140814900616105920256438504578013326493565836047242407382442812245131517757519164899226365743722432277368075027627883045206501792761700945699168497257879683851737049996900961120515655050115561271491492515342105748966629547032786321505730828430221664970324396138635251626409516168005427623435996308921691446181187406395310665404885739434832877428167407495370993511868756359970390117021823616749458620969857006263612082706715408157066575137281027022310927564910276759160520878304632411049364568754920967322982459184763427383790272448438018526977764941072715611580434690827459339991961414242741410599117426060556483763756314527611362658628383368621157993638020878537675545336789915694234433955666315070087213535470255670312004130725495834508357439653828936077080978550578912967907352780054935621561090795845172954115972927479877527738560008204118558930004777748727761853813510493840581861598652211605960308356405941821189714037868726219481498727603653616298856174822413033485438785324024751419417183012281078209729303537372804574372095228703622776363945290869806258422355148507571039619387449629866808188769662815778153079393179093143648340761738581819563002994422790754955061288818308430079648693232179158765918035565216157115402992120276155607873107937477466841528362987708699450152031231862594203085693838944657061346236704234026821102958954951197087076546186622796294536451620756509351018906023773821539532776208676978589731966330308893304665169436185078350641568336944530051437491311298834367265238595404904273455928723949525227184617404367854754610474377019768025576605881038077270707717942221977090385438585844095492116099852538903974655703943973086090930596963360767529964938414598185705963754561497355827813623833288906309004288017321424808663962671333528009232758350873059614118723781422101460198615747386855096896089189180441339558524822867541113212638793675567650340362970031930023397828465318547238244232028015189689660418822976000815437610652254270163595650875433851147123214227266605403581781469090806576468950587661997186505665475715792896
res()
Traceback (most recent call last):
  File "<pyshell#309>", line 1, in <module>
    res()
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
sys.set_int_max_str_digits()
Traceback (most recent call last):
  File "<pyshell#310>", line 1, in <module>
    sys.set_int_max_str_digits()
TypeError: set_int_max_str_digits() missing required argument 'maxdigits' (pos 1)
sys.set_int_max_str_digits(88888888)
res()

res()

res()

res()

res()

res()



class Dog:
    pass

d = Dog()
type(d)
<class '__main__.Dog'>
type(Dog)
<class 'type'>
isinstance(d, Dog)
True
isinstance(Dog, type)
True
isinstance(list, type)
True
list.__bases__
(<class 'object'>,)

isinstance(list, type)
True
d = Dog()
isinstance(d, type)
False
class Number:
    Num = 99
    def get_number(self):
        return 55

    
n = Number()
n.Num
99
n.get_number()
55
def get_number(self):
...     return 55
... 
>>> NumberFormType = type("NumberFormType", (object,), {"get_number":get_number, "Num":99, "name":"Jojo"})
>>> NumberFormType
<class '__main__.NumberFormType'>
>>> nn = NumberFormType()
>>> type(nn)
<class '__main__.NumberFormType'>
>>> nn.Num
99
>>> nn.name
'Jojo'
>>> nn.get_number()
55
>>> class Number:
...     Num = 99
...     def get_number(self):
...         return 55
... 
...     
>>> NumberFormType = type("NumberFormType", (object,), {"get_number":get_number, "Num":99, "name":"Jojo"})
>>> di = {"VIN":12315, "Body Type":"Sedan", "counter":0}
>>> new_user_type = type(name, (object,), di)
Traceback (most recent call last):
  File "<pyshell#353>", line 1, in <module>
    new_user_type = type(name, (object,), di)
NameError: name 'name' is not defined
>>> name = input()
Car
>>> new_user_type = type(name, (object,), di)
>>> new_user_type
<class '__main__.Car'>
>>> my_car = new_user_type()
>>> my_car.VIN
12315
>>> my_car.Body Type
SyntaxError: invalid syntax
