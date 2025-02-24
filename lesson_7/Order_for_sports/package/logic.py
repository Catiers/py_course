# Функция создания товара в магазин.
def create_product(prices_in_shop):
    """
    Args
    ------
    prices_in_shop - dict, Каталог товаров.
    product - str, Наименование товара.
    price - float, Цена товара.

    Returns
    ------
    Либо "Товар создан", либо "Товар существует".
    """

    product, price = input("Введите название товара - "), float(input("Введите цену товара (в $) - "))
    if product not in prices_in_shop:
        prices_in_shop[product] = (f"{price} $")
        return f"Товар '{product}' создан."
    return "Такой товар уже существует."


# Функция редактирования цены товара в магазине.
def edit_product(prices_in_shop):
    """
    Args
    ------
    prices_in_shop - dict, Каталог товаров.
    product - str, Наименование товара.
    price - float, Цена товара.

    Returns
    ------
    Либо "Товар создан", либо "Товар существует".
    """
    
    product, price = input("Введите название товара - "), float(input("Введите новую цену товара (в $) - "))
    if product in prices_in_shop:
        prices_in_shop[product] = (f"{price} $")
        return f"Цена товара '{product}' изменена на {price}."
    return "Такого товара не существует."


# Функция удаления товара из магазина.
def del_product(prices_in_shop):
    """
    Args
    ------
    prices_in_shop - dict, Каталог товаров.
    product - str, Наименование товара.
    price - float, Цена товара.

    Returns
    ------
    Либо "Товар создан", либо "Товар существует".
    """
    
    product = input("Введите название товара - ")
    if product in prices_in_shop:
        prices_in_shop.pop(product)
        print(f"Товар '{product}' удалён.")
    else:
        print("Такого товара не существует.")


# Функция просмотра товара в магазине.
def read_all_products(prices_in_shop):
    """
    Args
    ------
    prices_in_shop - dict, Каталог товаров.
    product - str, Наименование товара.
    price - float, Цена товара.

    Returns
    ------
    Либо "Товар создан", либо "Товар существует".
    """
    
    if prices_in_shop != {}:
        return prices_in_shop

