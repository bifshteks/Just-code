'''Игра в крестики-нолики'''


import sys


OR = 0

def print_bcg(arr):
    '''Выводит поле на экран'''
    for _ in  arr:
        for __ in _:
            print(__, end=' ')
        print()

def chet():
    '''Возвращает очередность хода'''
    global OR
    c = OR*1
    OR += 1
    return True if c % 2 == 0 else False

def place(num):
    '''Переносит ввод с правой цифровой клаватуры в индексы'''
    if num >= 7:
        return 0, num - 7
    elif num >= 4:
        return 1, num - 4
    else:
        return 2, num - 1
    
def find_win(arr):
    '''Проверяет, есть ли победитель'''
    if arr[0][0] == arr[0][1] == arr[0][2] != '.':
        return arr[0][0]
    elif arr[1][0] == arr[1][1] == arr[1][2] != '.':
        return arr[1][1]
    elif arr[2][0] == arr[2][1] == arr[2][2] != '.':
        return arr[2][2]
    elif arr[0][0] == arr[1][0] == arr[2][0] != '.':
        return arr[0][0]
    elif arr[0][1] == arr[1][1] == arr[2][1] != '.':
        return arr[1][1]
    elif arr[0][2] == arr[1][2] == arr[2][2] != '.':
        return arr[2][2]
    elif arr[0][0] == arr[1][1] == arr[2][2] != '.':
        return arr[0][0]
    elif arr[2][0] == arr[1][1] == arr[0][2] != '.':
        return arr[1][1]

def main():
    print('\n' * 50)
    bcg = [['.' for _ in range(3)] for _ in range(3)]
    print_bcg(bcg)
    while True:
        print()
        way = int(input())
        p = place(way)
        bcg[p[0]][p[1]] = 'X' if chet() else 'O'
        print('\n' * 50)
        print_bcg(bcg)
        if find_win(bcg):
            print('\n"' + find_win(bcg) + '" IS WIN!!!')
            print('Do you want to continue? "y" or "n"')
            answer = input()
            if answer == 'y':
                bcg = [['.' for _ in range(3)] for _ in range(3)]
                main()
            else:
                print('\nThanks for gaming. I hope you enjoy')
                break
        elif ('.' not in bcg[0] and
              '.' not in bcg[1] and
              '.' not in bcg[2]) and not find_win(bcg):
            print('Dead heat!')
            print('Do you want to continue? "y" or "n"')
            answer = input()
            if answer == 'y':
                bcg = [['.' for _ in range(3)] for _ in range(3)]
                main()
            else:
                print('\nThanks for gaming. I hope you enjoy')
                break
            
        
if __name__ == '__main__':
    main()
