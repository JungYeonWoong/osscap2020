from matrix import *
from random import *

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()

### 미구현 기능 1 -> 7가지 모양을 함수안에 리스트의 형태로 선언 후 random숫자를 받아 
def random_arrayBlk():

    arrayBlk_list = list()
    arrayBlk_list = [ [ [ 1, 1 ],[ 1, 1 ] ], [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ], [ [ 1, 0, 0 ], [ 1, 1, 1 ],[ 0, 0, 1] ], [ [ 1, 0, 0 ], [ 1, 1, 1 ],[ 0, 0, 0] ], [ [ 0, 0, 1 ], [ 1, 1, 1 ],[ 0, 0, 0 ] ], [ [ 0, 1, 0 ], [ 1, 1, 1 ],[ 0, 0, 0] ], [ [ 0, 0, 1 ], [ 1, 1, 1 ],[ 1, 0, 0] ] ]


    random_num = randint(0, 6)
    if random_num == 0:
        return arrayBlk_list[0]
    elif random_num == 1:
        return arrayBlk_list[1]
    elif random_num == 2:
        return arrayBlk_list[2]
    elif random_num == 3:
        return arrayBlk_list[3]
    elif random_num == 4:
        return arrayBlk_list[4]
    elif random_num == 5:
        return arrayBlk_list[5]
    elif random_num == 6:
        return arrayBlk_list[6]
    else:
        print("오류가 났습니다.")

arrayBlk = random_arrayBlk()

###미구현 기능 2  , case_num이 1 이면 시계방향으로 회전, 2이면 반시계방향으로 회전
def transpose(arrayBlk, case_num):
    currBlk = Matrix(arrayBlk)

    if currBlk.get_dy() == 2:
        a1, a2, a3, a4 = arrayBlk[0][0], arrayBlk[0][1], arrayBlk[1][1], arrayBlk[1][0]

        if case_num == 1:
            arrayBlk[0][1], arrayBlk[1][1], arrayBlk[1][0], arrayBlk[0][0] = a1, a2, a4, a4
        elif case_num == 2:
            arrayBlk[0][0], arrayBlk[0][1], arrayBlk[1][1], arrayBlk[1][0] = a2, a3, a4, a1

    elif currBlk.get_dy() == 3:
        a, b, c, d = arrayBlk[0][0], arrayBlk[0][2], arrayBlk[2][2], arrayBlk[2][0]
        aa, bb, cc, dd = arrayBlk[0][1], arrayBlk[1][2], arrayBlk[2][1], arrayBlk[1][0]
        
        if case_num == 1:
            arrayBlk[0][2], arrayBlk[2][2], arrayBlk[2][0], arrayBlk[0][0] = a, b, c, d
            arrayBlk[1][2], arrayBlk[2][1], arrayBlk[1][0], arrayBlk[0][1] = aa, bb, cc, dd
        elif case_num == 2:
            arrayBlk[0][0], arrayBlk[0][2], arrayBlk[2][2], arrayBlk[2][0] = b, c, d, a
            arrayBlk[0][1], arrayBlk[1][2], arrayBlk[2][1], arrayBlk[1][0] = bb, cc, dd, aa

    elif currBlk.get_dy() == 4:
        a1, a2, a3, a4 = arrayBlk[0][0], arrayBlk[0][3], arrayBlk[3][3], arrayBlk[3][0]
        b1, b2, b3, b4 = arrayBlk[0][1], arrayBlk[1][3], arrayBlk[3][2], arrayBlk[2][0]
        c1, c2, c3, c4 = arrayBlk[0][2], arrayBlk[2][3], arrayBlk[3][1], arrayBlk[1][0]
        d1, d2, d3, d4 = arrayBlk[1][1], arrayBlk[1][2], arrayBlk[2][2], arrayBlk[2][1]
        
        if case_num == 1:
            arrayBlk[0][3], arrayBlk[3][3], arrayBlk[3][0], arrayBlk[0][0] = a1, a2, a3, a4
            arrayBlk[1][3], arrayBlk[3][2], arrayBlk[2][0], arrayBlk[0][1] = b1, b2, b3, b4
            arrayBlk[2][3], arrayBlk[3][1], arrayBlk[1][0], arrayBlk[0][2] = c1, c2, c3, c4
            arrayBlk[1][2], arrayBlk[2][2], arrayBlk[2][1], arrayBlk[1][1] = d1, d2, d3, d4
        elif case_num == 2:
            arrayBlk[0][0], arrayBlk[0][3], arrayBlk[3][3], arrayBlk[3][0] = a2, a3, a4, a1
            arrayBlk[0][1], arrayBlk[1][3], arrayBlk[3][2], arrayBlk[2][0] = b2, b3, b4, b1
            arrayBlk[0][2], arrayBlk[2][3], arrayBlk[3][1], arrayBlk[1][0] = c2, c3, c4, c1
            arrayBlk[1][1], arrayBlk[1][2], arrayBlk[2][2], arrayBlk[2][1] = d2, d3, d4, d1

    return arrayBlk


###
### initialize variables
###     


### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2

newBlockNeeded = False

arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

###
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
currBlk = Matrix(arrayBlk)
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

###
### execute the loop
###

while True:
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left
        left -= 1
    elif key == 'd': # move right
        left += 1
    elif key == 's': # move down
        top += 1
    elif key == 'w':# rotate the block clockwise
        arrayBlk = transpose(arrayBlk, 1)
        currBlk = Matrix(arrayBlk)

    elif key == ' ': # drop the block    미구현 기능 3
        while 1:
            top += 1
            tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
            tempBlk = tempBlk + currBlk
            
            if tempBlk.anyGreaterThan(1):
                break
    else:
        print('Wrong key!!!')
        continue

    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(1):
        if key == 'a': # undo: move right
            left += 1
        elif key == 'd': # undo: move left
            left -= 1
        elif key == 's': # undo: move up
            top -= 1
            newBlockNeeded = True
        elif key == 'w': # undo: rotate the block counter-clockwise
            arrayBlk = transpose(arrayBlk, 2)
            currBlk = Matrix(arrayBlk)
#미구현 기능 3
        elif key == ' ': # undo: move up
            top -= 1
            newBlockNeeded = True

        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()

    if newBlockNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False
        arrayBlk = random_arrayBlk() #랜덤으로 테트리스 모양 선택
        
        currBlk = Matrix(arrayBlk)
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
        
###
### end of the loop
###
