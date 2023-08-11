# -*- coding: UTF-8 -*-

import os, copy, msvcrt, colorama
colorama.init(autoreset=True)

blocks = [[*'1' * 9] for _ in range(9)]

def printBlocks():
    os.system('cls')
    blocks_ = copy.deepcopy(blocks)
    blocks_[y][x] = colorama.Fore.LIGHTYELLOW_EX + blocks_[y][x] + colorama.Fore.RESET
    string = '\n'.join([' '.join(block) for block in blocks_])
    return print(string)

x, y = 0, 0
selected = False

while 1:
    printBlocks()

    key = msvcrt.getche()
    if selected:
        value = int(blocks[y][x])

        if key in (b'w', b'W'):
            if not value >= 9:
                value += 1
            else:
                value = 1
        elif key in (b's', b'S'):
            if value > 1:
                value -= 1
            else:
                value = 9
        elif key in (b'\n', b'\r'):
            selected = False
            continue
        else:
            pass

        blocks[y][x] = str(value)
    else:
        if key in (b'w', b'W'):
            if y > 1:
                y -= 1
            else:
                y = 8
        elif key in (b's', b'S'):
            if y < 8:
                y += 1
            else:
                y = 0
        elif key in (b'a', b'A'):
            if x > 1:
                x -= 1
            else:
                x = 8
        elif key in (b'd', 'D'):
            if x < 8:
                x += 1
            else:
                x = 0
        elif key in (b'\n', b'\r'):
            selected = True
            continue
        else:
            pass

    if key == b' ':
        break
blocks[y][x] = blocks[y][x].strip(colorama.Fore.LIGHTYELLOW_EX)
printBlocks()

correct = True
for x in range(9):
    blocks[x] = [*map(int, blocks[x])]
    blocks_x = set(blocks[x])
    blocks_y = set([int(blocks[y][x]) for y in range(9)])

    if len(blocks_x) < 9 or len(blocks_y) < 9:
        correct = False
        break
    else:
        continue

if correct:
    print('맞았습니다!')
else:
    print('틀렸습니다!')

print('아무 키나 눌러 프로그램을 종료하세요')
msvcrt.getch()
