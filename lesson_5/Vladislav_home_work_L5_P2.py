print("""
#   
#   Скрипт для рассчитывания
#   
#       ИМТ пользователя
#
#    введя вес(кг) и рост(м)
#
""")
a = 0
# Function for find BMI user.
def BMI(w, h):
    """
    Входные переменные:
        w - float (можно int), обязательно, не меньше 0.
        h - float (можно int), обязательно, не меньше 0.
    Выходные переменные:
        None или значение ИМТ.
    """
    global a
    if w <= 0 or h <= 0:
        return "Введите верные значения"
    b = result = w / h ** 2
    if result > 18.4:
        a += 5


# Input user characteristics.
user_characteristics = input("Введите свой вес(кг) и рост(в метрах) через пробел: ")

# Output BMI user.
print(BMI(float(user_characteristics.split()[0]),float(user_characteristics.split()[1])))
