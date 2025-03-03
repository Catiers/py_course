from mobile_phone_class import MobilePhone

phone1 = MobilePhone(input("Введите ваш номер телефона: "))


def main():

    inf_cycle = int(input("Выберите пункт:\n1 - Включить телефон.\n2 - Выключить телефон.\n3 - Позвонить на номер.\n-1 - Выйти из программы.\n"))

    while inf_cycle != -1:

        # Если inf_cycle == 1, то включаем телефон.
        if inf_cycle == 1:
            print(phone1.turn_on())

        # Если inf_cycle == 2, то выключаем телефон.
        elif inf_cycle == 2:
            print(phone1.turn_off())

        # Если inf_cycle == 3, то пытаемся дозвониться до другого абонента.
        elif inf_cycle == 3:
            print(phone1.call(input("Введите номер, на который желаете позвонить: ")))
            
        else:
            print("Данного пункта не существует.")

        inf_cycle = int(input("Выберите пункт:\n1 - Включить телефон.\n2 - Выключить телефон.\n3 - Позвонить на номер.\n-1 - Выйти из программы.\n"))
        

if __name__ == '__main__':
    main()
