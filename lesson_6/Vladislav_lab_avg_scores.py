Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
school_class = {}
name = input("Name: ")
Name: Vasia Pupkin
name
'Vasia Pupkin'
#{name:grades, name:grades}
grage = int(input("grade: "))
grade: 8
school_class[name] = (grage, )
grage = int(input("grade: "))
grade: 6
school_class[name] += (grage, )
school_class
{'Vasia Pupkin': (8, 6)}
school_class[name]
(8, 6)
sum(school_class[name])/len(school_class[name])
7.0
menu = """
1 - добавить нового ученика
2 - добавить оценку ученику
3 - посчитать средний балд
-1 - выход"""
oper = int(input(menu))

1 - добавить нового ученика
2 - добавить оценку ученику
3 - посчитать средний балд
-1 - выход1
menu = """
1 - добавить нового ученика
2 - добавить оценку ученику
3 - посчитать средний балд
-1 - выход\n"""
oper = int(input(menu))

1 - добавить нового ученика
2 - добавить оценку ученику
3 - посчитать средний балд
-1 - выход
1
while oper != -1:
    if oper == 1:
        name = input("name: ")
        if name not in school_class:
            school_class[name] = ()
            print("Ученик успешно создан.")
        else:
            print("Ученик уже существует.")
    elif oper == 2:
        name = input("name: ")
        if name in school_class:
            grade = int(input("grade (1-10): ")
            school_class[name] += (grade, )
            print("Оценка успешно добавлена.")
        else:
            print("Такого ученика не существует.")
                        
SyntaxError: '(' was never closed


while oper != -1:
    if oper == 1:
        name = input("name: ")
        if name not in school_class:
            school_class[name] = ()
            print("Ученик успешно создан.")
        else:
            print("Ученик уже существует.")
    elif oper == 2:
        name = input("name: ")
        if name in school_class:
            grade = int(input("grade (1-10): "))
            school_class[name] += (grade, )
            print("Оценка успешно добавлена.")
        else:
            print("Такого ученика не существует.")
    elif oper == 3:
        if len(school_class) ==0:
            print("Оценок не содержится")
        elif len(school_class) > 0:
            for name in school_class.keys():
                grades = school_class[name]
                if len(grades) > 0:
                    print(name)
                        print(school_class[name])
                        
SyntaxError: unexpected indent
while oper != -1:
    if oper == 1:
        name = input("name: ")
        if name not in school_class:
            school_class[name] = ()
            print("Ученик успешно создан.")
        else:
            print("Ученик уже существует.")
    elif oper == 2:
        name = input("name: ")
        if name in school_class:
            grade = int(input("grade (1-10): "))
            school_class[name] += (grade, )
            print("Оценка успешно добавлена.")
        else:
            print("Такого ученика не существует.")
    elif oper == 3:
        if len(school_class) ==0:
            print("Оценок не содержится")
        elif len(school_class) > 0:
            for name in school_class.keys():
                grades = school_class[name]
                if len(grades) > 0:
                    print(name)
                    print(school_class[name])
                    print("avg: ")
                    print(sum(grades)/len(grades))
                else:
                    print("У", name, "нет оценок.")
    oper = int(input(menu))

                        
name: Kolya
Ученик успешно создан.

1 - добавить нового ученика
2 - добавить оценку ученику
3 - посчитать средний балд
-1 - выход
3
Vasia Pupkin
(8, 6)
avg: 
7.0
У Kolya нет оценок.

1 - добавить нового ученика
2 - добавить оценку ученику
3 - посчитать средний балд
-1 - выход
2
name: Kolya
grade (1-10): 10
Оценка успешно добавлена.

1 - добавить нового ученика
2 - добавить оценку ученику
3 - посчитать средний балд
-1 - выход
3
Vasia Pupkin
(8, 6)
avg: 
7.0
Kolya
(10,)
avg: 
10.0

1 - добавить нового ученика
2 - добавить оценку ученику
3 - посчитать средний балд
-1 - выход
2
name: "Vova"
Такого ученика не существует.

1 - добавить нового ученика
2 - добавить оценку ученику
3 - посчитать средний балд
-1 - выход
-1
