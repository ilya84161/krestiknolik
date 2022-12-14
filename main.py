
pole = [['-' for j in range (3)] for i in range(3)]
#поле функций

def print_pole ():           #отрисовка поля
    print ('    0   1   2')
    print ('--------------')
    for i in range(3):
        print(i,'|', pole[i][0], '|', pole[i][1], '|', pole[i][2])

def hod (s): #заполнение ячейки символом игрока
    proverka_hoda = False
    while not (proverka_hoda):
        print(f'ход игрока {s}')
        try:
            koordinata =[int (k) for k in (input ('введите координаты хода через пробел, в формате: А В, где А - число по вертикали, В - число по горизонтали\n')).split()]
        except:
            print('проверьте правильность введенных вами координат хода и попробуйте еще раз')
            continue
        try:
            if any ( [koordinata [0]<0, koordinata [0]>2, koordinata [1]<0, koordinata [1]>2 ]):
                print('проверьте правильность введенных вами координат хода, координаты хода, вне диапазона игрового поля, попробуйте еще раз')
                continue
        except IndexError:
            print('проверьте правильность введенных вами координат хода и попробуйте еще раз')
            continue
        if pole[koordinata[0]][koordinata[1]] == '-':
            pole[koordinata[0]][koordinata[1]] = s
            print_pole()
            proverka_hoda = True
        elif pole[koordinata[0]][koordinata[1]] =='x' or pole[koordinata[0]][koordinata[1]] =='o':
            print('данная клетка занята, попробуйте еще раз')

def proverka_rezultata ():           #функция проверки выигрыша одним из игроков
    vjigr_komb = [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]], [[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]], [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]
    for prk in vjigr_komb:
        #print(prk)
        if pole [prk [0][0]][prk[0][1]] == pole [prk [1][0]][prk[1][1]] == pole [prk [2][0]][prk[2][1]] != '-':
            return pole [prk [0][0]][prk[0][1]]
    return False



#ход игры, играем пока не выигрываем, проверку начинаем после третьего хода, если количество ходов 9 - ничья

print('поле для игры 3*3, начали!')
print_pole()
win = False
hodi = 1
while not win:
    igrok = 'x' if hodi %2 ==0 else 'o'
    hod (igrok)
    if hodi > 3:
        win = proverka_rezultata()
        if win:
            print(f'Победу одержал игрок {win}')
    if hodi == 9:
        print('ходов не осталось, ничья')
        break
    hodi += 1

