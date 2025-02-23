import random

inf_game = True
user_win = 0
comp_win = 0

# Вводное меню по программе.
choose_user = int(input("""
Введите:
      1 - Хочу сыграть в русскую рулетку...
      2 - Хочу увидеть счёт
      -1 - Выйти из игры...\n"""))


# Основной цикл программы.
while choose_user != -1:

    # Условие, что вызывает игру.
    if choose_user == 1:
        while inf_game:
            user_result = int(input('Введи одну цифру от 1 до 3 --> '))
            comp_result = random.randint(1, 4)

            if user_result == comp_result:
                user_win += 1
                win_or_die = 'Ты выиграл. Молодец.'
            else:
                comp_win += 1
                win_or_die = 'Ты проиграл. Пора умирать....'

            print(win_or_die)

            if input('Желаешь ещё сыграть?) \n + --> да \t - --> нет\n').strip() == '-':
                inf_game = False
                print("Прощай и заходи к нам ещё.")

    # Условие, которое выводит счёт.
    elif choose_user == 2:
        if user_win > comp_win:
            print(f"Тебе пока везёт. Ты выигрываешь со счётом {user_win}:{comp_win}")
        elif user_win < comp_win:
            print(f"Тебе пока не везёт. Ты проигрываешь со счётом {user_win}:{comp_win}")
        else:
            print(f"У вас ничью. Продолжай играть.\n {user_win}:{comp_win}")

    choose_user = int(input("""
    Введите:
      1 - Хочу сыграть в русскую рулетку...
      2 - Хочу увидеть счёт
     -1 - Выйти из игры...\n"""))