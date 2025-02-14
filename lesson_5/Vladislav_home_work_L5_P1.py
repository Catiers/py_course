print("""
#
#
#   Finding a leap year
#
#
""")

# Function for checking is a leap year.
def is_leap_year(year):
    """
    Входные переменные:
        year - int, обязательно.

    Функция проверяет, является ли введённый пользователем год високосным.
    
    Выходные переменные:
        True or None.
    """
    if (year%4 == 0 and year%100 != 0) or\
        (year%4 == 0 and year%100 == 0 and year%400 == 0):
        return True

# Test varible for comparing.
test_data = [1500, 1900, 2000, 2016, 1987]
test_result = [None, None, True, True, True]

# Checking for a match.
for user_year, result in zip(test_data,test_result):
    if is_leap_year(user_year) == result:
        print(user_year, 'is a leap year? --> ', result)
    else:
        print(user_year, 'from your func --> ', is_leap_year(user_year),\
              '\nbut expected --> ', result)
