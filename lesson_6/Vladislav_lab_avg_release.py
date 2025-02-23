menu = """
1 - Добавить нового ученика
2 - Добавить оценку ученику
3 - Посчитать средний балл
4 - Вывести список учеников
5 - Удаление ученика
-1 - выход\n"""

oper = int(input(menu))
school_class = {}


# Функция для добавления ученика.
def add_new_student():
    '''
    Args
    ------
    name_student - str, ФИО ученика.
    school_class - dict, Классный журнал.

    Returns
    ------
    Результат условия: или создан, или уже существует.
    '''
    name_student = input("Введите имя нового ученика: ")
    if name_student not in school_class:
        school_class[name_student] = ()
        print("Ученик успешно создан.")
    else:
        print("Ученик уже существует.")


# Функция для добавления оценок ученикам.
def add_new_grade():
    '''
    Args
    ------
    name_student - str, ФИО ученика.
    school_class - dict, Классный журнал.
    grade - int, Оценка ученика.

    Returns
    ------
    Результат условия: или добавляет оценки, или выводит, что ученик отсутсвует.
    '''
    additing_grade = True
    name_student = input("Введите имя ученика: ")
    if name_student in school_class:
        while additing_grade:
            grade = int(input("Оценка (1-10): "))
            school_class[name_student] += (grade, )
            print("Оценка успешно добавлена.")
            if input("+ - ещё добавить оценку; stop - прекратить добавлять\n").strip() == "stop":
                additing_grade = False

    else:
        print("Такого ученика не существует.")


# Функция для рассчитывания среднего балла.
def avg_score():
    '''
    Args
    ------
    name_student - str, ФИО ученика.
    school_class - dict, Классный журнал.
    grades - int, Оценки ученика.

    Returns
    ------
    Результат условия: или средний балл ученика, или отсутствие оценок.
    '''
    if len(school_class) == 0:
        print("Оценок не содержится.")
    elif len(school_class) > 0:
        for name_student in school_class.keys():
            grades = school_class[name_student]
            if len(grades) > 0:
                print(f"У {name_student} такие оценки {school_class[name_student]}")
                print(f"Средний балл: {sum(grades)/len(grades)}")
            else:
                print("У", name_student, "нет оценок.")
    

# Функция для вывода списка всех учеников.
def list_student():
    '''
    Args
    ------
    name_student - str, ФИО ученика.
    school_class - dict, Классный журнал.

    Returns
    ------
    Результат: выводит список всех учеников в журнале.
    '''
    for name_student in school_class.keys():
        print(name_student)


# Функция для удаления ученика.
def del_student():
    '''
    Args
    ------
    name_student - str, ФИО ученика.
    school_class - dict, Классный журнал.

    Returns
    ------
    Результат условия: или удалён, или не существует.
    '''
    name_student = input("Введите имя ученика: ")
    if name_student in school_class:
        print(f"{school_class.pop(name_student)} удалён.")
    else:
        print("Такого ученика не существует.")


# Главный цикл обработки.
while oper != -1:
    print()
    if oper == 1:
        add_new_student()
    elif oper == 2:
        add_new_grade()
    elif oper == 3:
        avg_score()
    elif oper == 4:
        list_student()
    elif oper == 5:
        del_student()
    oper = int(input(menu))
