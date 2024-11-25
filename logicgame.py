STATUS_CONTINUE = 'Игра продолжается!'
row1 = '1'
row2 = '2'
row3 = '3'
cola = 'a'
colb = 'b'
colc = 'c'
empty = '_ '
data = {
    row1: {
        cola: empty,
        colb: empty,
        colc: empty,
    },
    row2: {
        cola: empty,
        colb: empty,
        colc: empty,
    },
    row3: {
        cola: empty,
        colb: empty,
        colc: empty,
    },
}
allowed_symbols = ['X','O']
allowed_rows = [row1,row2,row3]
allowed_cols = [cola,colb,colc]


def check_is_game_end():
    winner = STATUS_CONTINUE

    empty_symbols = 0
    for dat in data.values():
        for d in dat.values():
            if d == empty:
                empty_symbols += 1

    # Условие победы по строчкам
    if (data[row1][cola] == data[row1][colb]) and\
            (data[row1][cola] == data[row1][colc]) and\
            (data[row1][cola] != empty):
        winner = data[row1][cola]
    elif (data[row2][cola] == data[row2][colb]) and\
            (data[row2][cola] == data[row2][colc]) and\
            (data[row2][cola] != empty):
        winner = data[row2][cola]
    elif (data[row3][cola] == data[row3][colb]) and\
            (data[row3][cola] == data[row3][colc]) and\
            (data[row3][cola] != empty):
        winner = data[row3][cola]
    # Условие победы по колонкам
    elif (data[row1][cola] == data[row2][cola]) and\
            (data[row1][cola] == data[row3][cola]) and\
            (data[row1][cola] != empty):
        winner = data[row1][cola]
    elif (data[row1][colb] == data[row2][colb]) and\
            (data[row1][colb] == data[row3][colb]) and\
            (data[row1][colb] != empty):
        winner = data[row1][colb]
    elif (data[row1][colc] == data[row2][colc]) and\
            (data[row1][colc] == data[row3][colc]) and\
            (data[row1][colc] != empty):
        winner = data[row1][colc]
    # Условие победы по диагоналям
    elif (data[row1][cola] == data[row2][colb]) and\
            (data[row1][cola] == data[row3][colc]) and\
            (data[row1][cola] != empty):
        winner = data[row1][cola]
    elif (data[row3][cola] == data[row2][colb]) and\
            (data[row3][cola] == data[row1][colc]) and\
            (data[row3][cola] != empty):
        winner = data[row3][cola]
    # Условия ничьи
    elif empty_symbols == 0:
        winner = "Ничья"

    # все ячейки заполн

    return winner


def input_value(input_value,value):
    column = input_value[1].lower()
    if column not in allowed_cols:
        return f'Вы пропустили ход из-за неправильной колонки: {column} разрешенные колонки." {allowed_cols}'

    row = input_value[0]
    if row not in allowed_rows:
        return f'Вы пропустили ход из-за неправильной строки: {row} разрешенные строки." {allowed_rows}'

    if (value in allowed_symbols) and (data[row][column] == empty):
        data[row][column] = value
        return 'Ход принят'
    else:
        return f'Вы пропустили ход из-за неправильного символа: {value}, разрешённые символы: {allowed_symbols} ' \
                  f'или ячейка уже заполнена.'


def print_game_field():
    str_result = 'Данные вводятся в формате: 1a\n'
    str_result += f"\t\t\t\ta\t\t\tb\t\tc\t\t\n"
    str_result += f"1\t\t{data[row1][cola]}\t\t{data[row1][colb]}\t\t{data[row1][colc]}\n"
    str_result += f"2\t\t{data[row2][cola]}\t\t{data[row2][colb]}\t\t{data[row2][colc]}\n"
    str_result += f"3\t\t{data[row3][cola]}\t\t{data[row3][colb]}\t\t{data[row3][colc]}\n"
    return str_result


def clear_data():
    data[row1] = {
        cola: empty,
        colb: empty,
        colc: empty,
    }
    data[row2] = {
        cola: empty,
        colb: empty,
        colc: empty,
    }
    data[row3] = {
        cola: empty,
        colb: empty,
        colc: empty,
    }