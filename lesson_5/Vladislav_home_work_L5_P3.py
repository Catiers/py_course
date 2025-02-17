print("""
#
#     Приложение для
#
#   расчёта факториала
#
#      любого числа
#
""")


# Function for factorial.
def factorial(n):
    """
    Input var:
    n - required, int

    Var:
    i - in cycle for

    Output var:
    res - int
    \n"""
    res = 1
    if n < 2 and n >= 0:
        return res
    elif n >= 2:
        for i in range(1,n+1):
            res *= i
        return res


print("Для примера факториал от -1 и до 9:\n")

# Test output.
for i in range(-1,9):
    print(factorial(i))