
tex = "Наибольшее число это: "  # Текст для вывода
first_number, second_number, third_number, four_number = input("Введите \
четыре целых числа через пробел: ").split()  # Получение 4 символьн. перемен.

first_number, second_number, third_number, four_number = int(first_number),\
 int(second_number), int(third_number), int(four_number)  # Преобразов. в int

# Основной цикл проверки максимального числа
if first_number > second_number:
	if third_number > four_number:
		print(f"{tex}{first_number}") if first_number > third_number else \
		 print(f"{tex}{third_number}")
	else:
		print(f"{tex}{first_number}") if first_number > four_number else \
		 print(f"{tex}{four_number}")
else:
	if third_number > four_number:
		print(f"{tex}{second_number}") if second_number > third_number else \
		 print(f"{tex}{third_number}")
	else:
		print(f"{tex}{second_number}") if second_number > four_number else \
		 print(f"{tex}{four_number}")

input("Нажмите ENTER чтобы закрыть...")  # Выход из программы
