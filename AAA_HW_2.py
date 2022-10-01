def show_menu():
    """базовая функция"""

    print(
        'Добро пожаловать!\n'
        'Выберите один из трёх варинтов:\n'
        'Если вы хотите вывести иерархию команд, нажмите 1\n'
        'Если вы хотите вывести сводный отчёт по департаментам, нажмите 2\n'
        'Если вы хотите сохранить сводный отчёт, нажмите 3\n'
    )

    option = input()
    while option not in ['1', '2', '3']:
        option = input()

    if option == '1':
        show_hierarchy()  # функция выводит департаменты и команды этих департаментов в виде словаря
    elif option == '2':
        show_statistics()  # функция выводит данные по каждому департаменту в виде словаря
    else:
        save_statistics()  # функция сохраняет данные по каждому департаменту в таблицу CSV


def show_hierarchy():
    """функция выводит департаменты и команды этих департаментов в виде словаря"""

    dict_commands = collections.defaultdict(list)  # ключами данного словаря будут департаменты,а его значениями-команды
    for row in csv_f:  # csv_f - исходная таблица, которую мы считываем построчно
        if row[2] not in dict_commands[row[1]]:
            dict_commands[row[1]].append(row[2])
    print(dict_commands)


def show_statistics() -> dict:
    """функция создает словарь, где ключ - департамент, а значение - снова словарь, в котором 0ой элемент отвечает
    за количество сотрудников, 1ый элемент - за макс ЗП, 2ой элемент - за мин ЗП, 3ий элемент - за среднюю ЗП"""

    dict_of_departs = {}
    for row in csv_f:
        if row[1] not in dict_of_departs.keys():
            dict_of_departs[row[1]] = {'Колич': 0, 'МаксЗП': 0, 'МинЗП': 10000000000, 'СредЗП': 0}
        else:
            dict_of_departs[row[1]]['Колич'] += 1
            dict_of_departs[row[1]]['МаксЗП'] = int(row[5]) if int(row[5]) > dict_of_departs[row[1]]['МаксЗП'] else \
                dict_of_departs[row[1]]['МаксЗП']
            dict_of_departs[row[1]]['МинЗП'] = int(row[5]) if int(row[5]) < dict_of_departs[row[1]]['МинЗП'] else \
                dict_of_departs[row[1]]['МинЗП']
            dict_of_departs[row[1]]['СредЗП'] += int(row[5])

    # мы посчитали не среднюю ЗП, а суммарную, для средней нужно суммарную разделить на количество работников
    for deparment in dict_of_departs:
        dict_of_departs[deparment]['СредЗП'] = int(
            dict_of_departs[deparment]['СредЗП'] / dict_of_departs[deparment]['Колич'])

    print(dict_of_departs)
    return dict_of_departs


def save_statistics():
    """функция сохраняет данные по каждому департаменту в таблицу CSV"""

    dict_of_departs = show_statistics()  # у нас есть словарь из 2 пунтка, нужно перевести его в табличный вид
    file1 = open(r"C:\Users\User\Desktop\ААА\Домашки\Python\CSV_HW_2_WRITE.csv", 'w')
    columns = ['Департамент', 'Число сотрудников', 'Максимальная ЗП', 'Минимальная ЗП', 'Средняя ЗП']
    writer = csv.DictWriter(file1, fieldnames=columns, delimiter=';')
    writer.writeheader()
    for dep in dict_of_departs.keys():
        writer.writerow({'Департамент': dep,
                         'Число сотрудников': dict_of_departs[dep]['Колич'],
                         'Максимальная ЗП': dict_of_departs[dep]['МаксЗП'],
                         'Минимальная ЗП': dict_of_departs[dep]['МинЗП'],
                         'Средняя ЗП': dict_of_departs[dep]['СредЗП']})


if __name__ == "__main__":
    # выгружаем данные для чтения и приводим их в нормальный вид
    import csv
    import collections

    csv_file = open(r"C:\Users\User\Desktop\ААА\Домашки\Python\CSV_HW_2.csv", 'r')
    headers = next(csv_file)  # делаем эту штуку, чтобы не считывать название столбцов в виде отдельной строчки
    csv_f = csv.reader(csv_file, delimiter=';')
    # переходим к работе нашей программы
    show_menu()
