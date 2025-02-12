operation = input("Введите какую операцию хотите провести (+, -, /, *): ")

while operation not in ["exit","выход","стоп"]:
	first_number, second_number = input("Введите два \
целых числа через пробел: ").split()  # Получение 2 символьн. перемен.
	first_number, second_number = int(first_number), int(second_number)
	if operation == "+":
		print(f"Результат сложения двух \
чисел равен {first_number + second_number}")  # Сложение
	elif operation == "-":
		print(f"Результат вычитания двух \
чисел равен {first_number - second_number}")  # Вычитание
	elif operation == "*":
		print(f"Результат умножения двух \
чисел равен {first_number * second_number}")  # Умножение
	elif operation == "/":
		print(f"Результат деления двух \
чисел равен {first_number / second_number}")  # Деление
	operation = input("Напишите 'exit' или введите мат. операцию: ")
