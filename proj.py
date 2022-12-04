print('|=======================|\n'
      '|Добро пожаловать в игру|\n'
      '|----крестики нолики----|\n'
      '|=======================|')

field = [[" ", " ", " ",] for t in range(3)]
player1 = input("Игрок №1 введите ваше имя: ")
player2 = input("Игрок №2 введите ваше имя: ")
player = player1
def show(f):
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")
def examination(f):
    while True:
        cords = input('Введите координаты: ').split()
        if len(cords) != 2:
            print('Введите 2 числа')
            continue
        if not(cords[0].isdigit() and cords[1].isdigit()):
            print(f'Введите числа: ')
            continue
        x, y = map(int, cords)
        if not(x>= 0 and x<= 2  and y>= 0 and y<= 2):
            print('Числа находятся вне диапазона!')
            continue
        if f[x][y] != " ":
            print('Клетка уже занята!')
            continue
        break
    return x, y
def win_examination(f,user, player):
    coordinates = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                   ((0, 0), (1, 0), (2, 0)), ((1, 1), (2, 1), (0, 1)), ((0, 2), (1, 2), (2, 2)),
                   ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for win_cords in coordinates:
        win = []
        for a in win_cords:
            win.append(f[a[0]][a[1]])
        if win == [user, user, user]:
            print(f'Победил игрок "{player}"')
            return True
    return False

count = 0
while True:
    show(field)
    if count % 2 == 0:
        print(f'Ходит игрок "{player}"')
        user = "X"
        player = player2
    else:
        print(f'Ходит игрок "{player}"')
        user = "0"
        player = player1
    if count == 9:
        print('Победила дружба!!!')
        break
    x, y = examination(field)
    field[x][y] = user
    count += 1
    if win_examination(field, user, player):
        show(field)
        break

