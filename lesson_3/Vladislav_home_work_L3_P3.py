# Create list.
spisok = []

lenght_spisok = int(input("Введите количество значение для списка: "))

for i in range(lenght_spisok):
	spisok.append(int(input("Введите число для добавления его в список: ")))

print(spisok)

# Bubble sort.
n=0

swapped = True

while swapped:
	swapped = False
	for i in range(lenght_spisok-1):
		if spisok[i] > spisok[i+1]:
			swapped = True
			spisok[i], spisok[i+1] = spisok[i+1], spisok[i]

print(spisok)
spisok.reverse()
print(spisok)