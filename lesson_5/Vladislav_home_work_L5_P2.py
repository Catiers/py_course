print("""
#   
#   Скрипт для рассчитывания
#   
#       ИМТ пользователя
#
#    введя вес(кг) и рост(м)
#
""")

# Function for find BMI user.
def BMI(w, h):
    """
    Входные переменные:
        w - float (можно int), обязательно, не меньше 0.
        h - float (можно int), обязательно, не меньше 0.
    Выходные переменные:
        None или значение ИМТ.
    """
    if w <= 0 or h <= 0:
        print("Введите верные значения")
    result = w / h ** 2
    if result < 18.5:
        print(f"{result}\nУ вас дефицит массы тела. Попробуйте проследить за калориями.")
    elif result < 25.1:
        print(f"{result}\nУ вас норма массы тела. Продолжайте в том же духе.")
    elif result < 30.1:
        print(f"{result}\nУ вас предожирение массы тела. Попробуйте проследить за калориями.")
    elif result < 35.1:
        print(f"{result}\nУ вас ожирение | степени. Попробуйте проследить за калориями.")
    elif result < 40.1:
        print(f"{result}\nУ вас ожирение || степени. Попробуйте проследить за калориями.")
    elif result < 45.1:
        print(f"{result}\nУ вас ожирение ||| степени. Попробуйте обратиться к врачу.")


# Input user characteristics.
user_characteristics = input("Введите свой вес(кг) и рост(в метрах) через пробел: ")

# Output BMI user.
BMI(float(user_characteristics.split()[0]),float(user_characteristics.split()[1]))
