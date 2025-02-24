from package import logic as l

prices_in_shop = {}

user_choose = int(input("""
    Выберете один из пунктов меню:
        1 - Создать товар для магазина.
        2 - Отредактировать цену магазина.
        3 - Удалить товар из магазина.
        4 - Просмотреть весь список товаров и цены.
       -1 - Выйти из приложения.\n"""))

while user_choose != -1:
    if user_choose == 1:
        print(l.create_product(prices_in_shop))
    elif user_choose == 2:
        l.edit_product(prices_in_shop)
    elif user_choose == 3:
        l.del_product(prices_in_shop)
    elif user_choose == 4:
        print("Каталог пуст.") if l.read_all_products(prices_in_shop) == None else print(l.read_all_products(prices_in_shop))
    user_choose = int(input("""
    Выберете один из пунктов меню:
        1 - Создать товар для магазина.
        2 - Отредактировать цену магазина.
        3 - Удалить товар из магазина.
        4 - Просмотреть весь список товаров и цены.
       -1 - Выйти из приложения.\n"""))
