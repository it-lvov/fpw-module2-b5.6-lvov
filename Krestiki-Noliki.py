# Игра Крестики-Нолики, используются английские X и O (маленькие)

# формирование матрицы
def show_m(m):
    for i in range(4):
        for j in range(4):
            print(m[i][j], end=" ")
        print()
    print(".......")


# ход
def move():
    steps = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
    s = input(who)

    # проверка корректности инпута
    if s not in steps:
        print("Некорректный ввод, попробуйте еще раз...")
        move()
    elif m[int(s[0])][int(s[1])] != '-':
        print("Поле уже занято, попробуйте еще раз...")
        move()
    else:
        m[int(s[0])][int(s[1])] = sym  # запись хода в матрицу


# проверка победы
def check_victory(m):
    # кто выиграл
    def who_won(check):
        global end
        if check == 'x' or check == 'o':
            end = True
            return print('Победил: ', check, ' !!!')

    # rows
    for i in range(1, 4):
        check = ''.join(set(m[i][1:]))
        who_won(check)

    # columns
    check = []
    for j in range(1, 4):
        for i in range(1, 4):
            check.append((m[i][j]))
        check = ''.join(set(check))
        who_won(check)
        check = []

    # dia1
    check = []
    for i in range(1, 4):
        check.append(m[i][i])
    check = ''.join(set(check))
    who_won(check)

    # dia2
    check = []
    j = 3
    for i in range(1, 4):
        check.append(m[i][j])
        j -= 1
    check = ''.join(set(check))
    who_won(check)

    # friendship
    if step == 9:
        return print('Победила дружба !!!')


# начальная матрица
m = [
    [' ', 1, 2, 3],
    [1, '-', '-', '-'],
    [2, '-', '-', '-'],
    [3, '-', '-', '-'],
]

# инструкция:
print("Игра Крестики-Нолики")
print("Ход указывается сочетанием строки и столбца без пробела. Например: 22")
print("---")

# вывод начальной матрицы
show_m(m)

# для завершения при победе
end = False

# ходы от 1 до 9
for step in range(1, 10):
    if not end:
        if step % 2 == 0:
            who = "Ход НОЛИКА (строка и столбец без пробела):"
            sym = 'o'
        else:
            who = "Ход КРЕСТИКА (строка и столбец без пробела):"
            sym = 'x'

        move()
        show_m(m)

        if step > 4:  # раньше 5-го хода нет смысла проверять пробеду
            check_victory(m)
    else:
        print('-- конец игры --')
        break