import numpy as np
import time


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    else:
        return step2_no_umbrella()


def step2_umbrella():
    rain = bool(np.random.randint(2))
    if rain:
        print(
            "Ух....идет дождик.....но у уточки же есть зонтик!"
            "Поэтому уточка открывает зонтик и идет до бара спокойно."
        )
        step3("no rain")
    else:
        print(
            "А дождика то нет!"
            "Поэтому зонтик утке не понадобился и она счастливая идет до бара."
        )
        step3("no rain")


def step2_no_umbrella():
    rain = bool(np.random.randint(2))
    if rain:
        print("Дождик капает, а зонтика нет."
              "Что делать уточке?"
              "Вернуться домой и устроить ламповый марофон фильмов про Гарри Поттера или дотопать до бара?"
              )
        option = ''
        options = {'остаться': True, 'рискнуть': False}
        while option not in options:
            print('Выберите: {}/{}'.format(*options))
            option = input()
        time.sleep(1)
        if options[option]:
            print("Уточка вернулась домой, легла в теплую кроватку и наслаждается жизнью^^")
        else:
            print("Смелая уточка потопала под дождиком в бар.")
            step3('rain')
    else:
        print("Дождика нет, а значит счастливая утка идет до бара.")
        step3("no rain")


def step3(x):
    walk()
    if x == "rain":
        print("Уточка дошла до бара вся мокрая и с плохим настроением, а значит надо выпить что-то крепкое.")
    else:
        print("Уточка дошла до бара весело и счастливо, а значит надо выпить что-то крепкое.")
    step4()




def step4():
    print("Что уточка будет пить?")
    drink = ''
    drinks = ["водка", "виски", "коньяк", "абсент"]
    while drink not in drinks:
        print('Выберите: {}/{}/{}/{}'.format(*drinks))
        drink = input()
    if drink == "абсент":
        print("Уточке стало плохо...ей заказали такси и проснулась она уже в своей кроватке")
    else:
        print("Уточка напилась и немного побуянила"
              "...ничего нового....."
              "позже она заказала такси и поехала спокойно домой."
        )


def walk():
    for i in range(0, 10):
        time.sleep(1)
        print("топ топ топ")


if __name__ == '__main__':
    step1()
