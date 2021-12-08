def welcome():    # Функция вступительного приветствия
    print('--------------------------')
    print('|    Приветствуем Вас    |')
    print('|        в игре          |')
    print('|    Крестики-нолики!    |')
    print('|   Формат ввода: x, y   |')
    print('|    x-номер строки      |')
    print('|    y-номер столбца     |')
    print('--------------------------')

# field = [[""] * 3 for i in range(3)]      # Определение размера игрового поля

def type_of_field():    # Функция визуализации поля
     print()                                            # Выводим пустую строку
     print("    | 0 | 1 | 2 | ")                        # Выводим название столбцов
     print("  --------------- ")                        # Выводим разделитель

     for i, row in enumerate(field):                    # Запускаем цикл For, используя функцию
                                                        # enumerate которая берет список field
                                                        # и пронумеровывает каждый его элемент.
                                                        # При этом получается индекс списка и его элемент.

         row_str = f"  {i} | {' | '.join(row)} | "      # Заводим переменную row_str для определения строки поля
                                                        # при помощи объединения спичков в строку методом .join

         print(row_str)                                 # Выводим строку поля
         print("  --------------- ")                    # Выводим разделитель
     print()



def request():  # Запрос координат у пользователей
    while True:                                             # Запускаем цикл while
        cords = input('    Ваш ход:    ').split()           # Получение пользовательского ввода с разделением
                                                            # его методом .split()

        if len(cords) != 2:                                 # Подсчет и проверка количества элементов
            print(' Введите 2 координаты через пробел ')
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):            # Проверка на int
            print('Введите числа!!!')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:                # Проверка диапазона ввода чисел
            print('Координаты вне диапазона')
            continue

        if field[x][y] != "":                               # Проверка свободной клетки
            print('Клетка занята')
            continue
        return x, y


def you_won_if():    # Проверка победных комбинаций
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ['X', 'X', 'X']:
            print('Выйграл X!!!')
            return True
        if symbols == ['0', '0', '0']:
            print('Выйграл 0!!!')
            return True
    return False


# Игровой цикл
welcome()
field = [[""] * 3 for i in range(3)]  # Определение размера игрового поля
num = 0
while True:
    num += 1

    type_of_field()

    if num % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')

    x, y = request()  # Распаковка двух переменых из функции request

    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if you_won_if():
        break

    if num == 9:
        print('Ничья!!!')
        break