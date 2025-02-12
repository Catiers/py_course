Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = [1,2,3,4]
id(a)
2429378448896
aa = a
aa
[1, 2, 3, 4]
a
[1, 2, 3, 4]
id(a)
2429378448896
id(aa)
2429378448896
aa[0] = 2
aa
[2, 2, 3, 4]
a
[2, 2, 3, 4]
aa = a[:]
id(aa)
2429378580096
id(a)
2429378448896
aa[2] = 24
aa
[2, 2, 24, 4]
a
[2, 2, 3, 4]
qq = a.copy()
qq
[2, 2, 3, 4]
a
[2, 2, 3, 4]
qq[2] = 12
id(qq)
2429370943040
id(a)
2429378448896







spisok = [1,2,3]
a = [21, 22, 352,521]
a = [21, 21, spisok, 214]
a
[21, 21, [1, 2, 3], 214]
bb = a{:}
SyntaxError: invalid syntax
bb = a[:]
bb
[21, 21, [1, 2, 3], 214]
spisok[2] = 12
bb
[21, 21, [1, 2, 12], 214]
a
[21, 21, [1, 2, 12], 214]
cc = c.copy()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    cc = c.copy()
NameError: name 'c' is not defined
cc = a.copy()
spisok[1] = 1251
spisok
[1, 1251, 12]
a
[21, 21, [1, 1251, 12], 214]
bb
[21, 21, [1, 1251, 12], 214]
cc
[21, 21, [1, 1251, 12], 214]
a = [21, 23, spisok.copy(), 12]
a
[21, 23, [1, 1251, 12], 12]
spisok[1] = 95
a
[21, 23, [1, 1251, 12], 12]
import copy
dd = copy.deepcopy(a)
dd
[21, 23, [1, 1251, 12], 12]
lit[1] = 214
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    lit[1] = 214
NameError: name 'lit' is not defined. Did you mean: 'list'?
NameError: name 'lit' is not defined. Did you mean: 'list'?
SyntaxError: invalid syntax

spisok[1]=214
spisok
[1, 214, 12]
dd
[21, 23, [1, 1251, 12], 12]
cc
[21, 21, [1, 214, 12], 214]
имя = "Джонни
SyntaxError: unterminated string literal (detected at line 1)
имя = "Джонни"
print(имя)
Джонни
li = [1,2,3,4]
li[1] = 24
li
[1, 24, 3, 4]
a = 89
a = 213
st = "12345"
st
'12345'
st[1]
'2'
st[2] = "21"
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    st[2] = "21"
TypeError: 'str' object does not support item assignment
len(st)
5
st
'12345'
st23 = "12345"
st
'12345'
st23
'12345'
id(st)
2429378499696
id(st23)
2429378499696
jj = [1,2,3,4]
ff = [1,2,3,4]
id(jj)
2429378582464
id(ff)
2429378581696
"afsder'sdfsd'sdfsd'fsdfs'df
SyntaxError: unterminated string literal (detected at line 1)
"afsder'sdfsd'sdfsd'fsdfs'df"
"afsder'sdfsd'sdfsd'fsdfs'df"
'dsfsd"sdfsd"sdfrsf"'
'dsfsd"sdfsd"sdfrsf"'
st
'12345'
st * 21
'123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345'
res = st * 22
res
'12345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345'
st+res
'1234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345'
ch
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    ch
NameError: name 'ch' is not defined. Did you mean: 'cc'?
ch = "f"
ch1 = "v"
ord(ch)
102
ord(ch1)
118
codeF = 102
codeV = ord(ch1)
codeF
102
codeV
118
chr(codeF)
'f'
li = []
for i in range(250, 298):
    li.append(chr(i))

    
li
['ú', 'û', 'ü', 'ý', 'þ', 'ÿ', 'Ā', 'ā', 'Ă', 'ă', 'Ą', 'ą', 'Ć', 'ć', 'Ĉ', 'ĉ', 'Ċ', 'ċ', 'Č', 'č', 'Ď', 'ď', 'Đ', 'đ', 'Ē', 'ē', 'Ĕ', 'ĕ', 'Ė', 'ė', 'Ę', 'ę', 'Ě', 'ě', 'Ĝ', 'ĝ', 'Ğ', 'ğ', 'Ġ', 'ġ', 'Ģ', 'ģ', 'Ĥ', 'ĥ', 'Ħ', 'ħ', 'Ĩ', 'ĩ']
for i in range(1000, 1123):
    li.append(chr(i))

    
li
['ú', 'û', 'ü', 'ý', 'þ', 'ÿ', 'Ā', 'ā', 'Ă', 'ă', 'Ą', 'ą', 'Ć', 'ć', 'Ĉ', 'ĉ', 'Ċ', 'ċ', 'Č', 'č', 'Ď', 'ď', 'Đ', 'đ', 'Ē', 'ē', 'Ĕ', 'ĕ', 'Ė', 'ė', 'Ę', 'ę', 'Ě', 'ě', 'Ĝ', 'ĝ', 'Ğ', 'ğ', 'Ġ', 'ġ', 'Ģ', 'ģ', 'Ĥ', 'ĥ', 'Ħ', 'ħ', 'Ĩ', 'ĩ', 'Ϩ', 'ϩ', 'Ϫ', 'ϫ', 'Ϭ', 'ϭ', 'Ϯ', 'ϯ', 'ϰ', 'ϱ', 'ϲ', 'ϳ', 'ϴ', 'ϵ', '϶', 'Ϸ', 'ϸ', 'Ϲ', 'Ϻ', 'ϻ', 'ϼ', 'Ͻ', 'Ͼ', 'Ͽ', 'Ѐ', 'Ё', 'Ђ', 'Ѓ', 'Є', 'Ѕ', 'І', 'Ї', 'Ј', 'Љ', 'Њ', 'Ћ', 'Ќ', 'Ѝ', 'Ў', 'Џ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'ѐ', 'ё', 'ђ', 'ѓ', 'є', 'ѕ', 'і', 'ї', 'ј', 'љ', 'њ', 'ћ', 'ќ', 'ѝ', 'ў', 'џ', 'Ѡ', 'ѡ', 'Ѣ']
for char in li:
    print(ord(char), end = " ")

    
250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 1000 1001 1002 1003 1004 1005 1006 1007 1008 1009 1010 1011 1012 1013 1014 1015 1016 1017 1018 1019 1020 1021 1022 1023 1024 1025 1026 1027 1028 1029 1030 1031 1032 1033 1034 1035 1036 1037 1038 1039 1040 1041 1042 1043 1044 1045 1046 1047 1048 1049 1050 1051 1052 1053 1054 1055 1056 1057 1058 1059 1060 1061 1062 1063 1064 1065 1066 1067 1068 1069 1070 1071 1072 1073 1074 1075 1076 1077 1078 1079 1080 1081 1082 1083 1084 1085 1086 1087 1088 1089 1090 1091 1092 1093 1094 1095 1096 1097 1098 1099 1100 1101 1102 1103 1104 1105 1106 1107 1108 1109 1110 1111 1112 1113 1114 1115 1116 1117 1118 1119 1120 1121 1122 
for value in st:
    print(value)

    
1
2
3
4
5
excl = "29"
for value in st:
    if value in excl:
        continue
    print(value)

    
1
3
4
5
for i in range(len(st)):
    print("index: ", i, "| value: ", st[i])

    
index:  0 | value:  1
index:  1 | value:  2
index:  2 | value:  3
index:  3 | value:  4
index:  4 | value:  5
st = "sell"
for i in range(len(st)):
    print("index: ", i, "| value: ", st[i])

    
index:  0 | value:  s
index:  1 | value:  e
index:  2 | value:  l
index:  3 | value:  l
st = "Hi, team. We are from England)."
secret = 4
secretSt = ":
SyntaxError: unterminated string literal (detected at line 1)
secretSt = ""
for char in st:
    secretSt = chr(ord(char)+secret)

    
secretSt
'2'
for char in st:
    secretSt += chr(ord(char)+secret)

    
secretSt = ""
for char in st:
    secretSt += chr(ord(char)+secret)

    
secretSt
'Lm0$xieq2$[i$evi$jvsq$Irkperh-2'
\
st
'Hi, team. We are from England).'
secret
4
result = ""
for char in secretSt:
    secretSt += chr(ord(char)-secret)

    
secretSt = 'Lm0$xieq2$[i$evi$jvsq$Irkperh-2'
for char in secretSt:
    result += chr(ord(char)-secret)

    
result
'Hi, team. We are from England).'
for char in secretSt:
    result += chr(ord(char)-2)

    
result
'Hi, team. We are from England).Jk."vgco0"Yg"ctg"htqo"Gpincpf+0'
result = ""
for char in secretSt:
    result += chr(ord(char)-2)


result
'Jk."vgco0"Yg"ctg"htqo"Gpincpf+0'
st[::-1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
st[::-1]
'.)dnalgnE morf era eW .maet ,iH'
st
'Hi, team. We are from England).'
st = "[fig] asdegsdxzas"
st = "[bug] asdasgascvgbs"
st = "[fig] asdegsdxzas"
st1 = "[bug] asdasgascvgbs"
st3 = "[hlp] as45236dasgascvgbs"
st[1:4]
'fig'
st1[1:4]
'bug'
st3[1:4]
'hlp'
li = [st, st1, st3]
for s in li:
    resul = s[1:4]
    if resul == "bug"
    
SyntaxError: expected ':'
for s in li:
    resul = s[1:4]
    if resul == "bug":
        print("БАг!")
    elif resul == "fix":
        print("Фикс")
    else:
        print(123)

        
123
БАг!
123
for s in li:
    resul = s[1:4]
    if resul == "bug":
        print("БАг!")
    elif resul == "fig":
        print("Фикс")
    else:
        print(123)

        
Фикс
БАг!
123
st[2:]
'ig] asdegsdxzas'
st[::3]
'[gaeda'
st
'[fig] asdegsdxzas'
st.upper()
'[FIG] ASDEGSDXZAS'
st
'[fig] asdegsdxzas'
st.lower()
'[fig] asdegsdxzas'
st.upper().lower().upper()
'[FIG] ASDEGSDXZAS'
name = input("-> ".upper()








             
KeyboardInterrupt
name = input("-> ").upper()
             
-> afer
name
             
'AFER'
st
             
'[fig] asdegsdxzas'
st.index()
             
Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    st.index()
TypeError: index() takes at least 1 argument (0 given)
st.index("d")
             
8
st.index("[")
             
0
st.index("`")
             
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    st.index("`")
ValueError: substring not found
name
             
'AFER'
name = "Johan"
             
name[:name.index("h"]]+"L"+name[name.index("h"]+1:]
             
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
name[:name.index("h")]+"L"+name[name.index("h")+1:]
             
'JoLan'
name
             
'Johan'
name = "sdgyusirvhsidfgsdfgs"
             
name.count("s")
             
5
name.count("s")
             
5

asdf
             
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    asdf
NameError: name 'asdf' is not defined

============================ RESTART: Shell ============================
name = "asfsdgadfsgsrgsedgaserg"
             
name.isalpha()
             
True
name = "asfsdgadfsgsrgsedgaserg1"
             
name.isalpha()
             
False
numbers = "12315"
             
numbers.isdigit()
             
True
numbers = "12315f"
             
numbers.isdigit()
             
False
numbers = "12315"
             
numbers.isalpha
             
<built-in method isalpha of str object at 0x000002ADD231EB30>
\
numbers.isalpha()
             
False
name
             
'asfsdgadfsgsrgsedgaserg1'
name.islower()
             
True
name = "dsadgdafGsfgsdfg"
             
name.islower()
             
False
" ".isspace()
             
True
" dfg".isspace()
             
False
li
             
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    li
NameError: name 'li' is not defined
name
             
'dsadgdafGsfgsdfg'
name.replace("dsa", "lol
             
SyntaxError: unterminated string literal (detected at line 1)
name.replace("dsa", "lol")
             
'loldgdafGsfgsdfg'
name.swith(".")
             
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    name.swith(".")
AttributeError: 'str' object has no attribute 'swith'
name.endswith(".")
             
False
name.startswith("lol")
             
False
name
             
'dsadgdafGsfgsdfg'
name.isupper()
             
False
st
             
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    st
NameError: name 'st' is not defined. Did you mean: 'set'?
st = "      dfgsdfgsd    "
             
st.strip()
             
'dfgsdfgsd'
>>> st.title()
...              
'      Dfgsdfgsd    '
>>> st += st
...              
>>> st.title()
...              
'      Dfgsdfgsd          Dfgsdfgsd    '
>>> st.swapcase()
...              
'      DFGSDFGSD          DFGSDFGSD    '
>>> st.capitalize()
...              
'      dfgsdfgsd          dfgsdfgsd    '
>>> st = "sdfsdf*sdfs*sdfs*"
...              
>>> st.split(sep="*")
...              
['sdfsdf', 'sdfs', 'sdfs', '']
