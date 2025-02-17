print("""
#
#   App for finding
#
#   Fibonacci number
#
\n""")


# Function for number of Fibonacci.
def fibo(n):
    """
    Input var:
    n - required, int.

    Var:
    i - in cycle for, int.
    f1 - previous number Fibonacci, int.

    Output var:
    f2 - number Fibonacci, int.\n
    """
    f1 = f2 = 1
    if n >= 2:
        for i in range(n-2):
            f1, f2 = f2, f1+f2
    elif n < 0:
        for i in range(0,n-1,-1):
            f1, f2 = f2, f1-f2
    elif n == 0:
        f2 = 0
    print(f"Ваше {n} - это число {f2}")
    

# Serial number from the user.
fibo(int(input("Какое число желаете найти?\n")))