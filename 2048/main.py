import random

MAX_BLOCK_NUM = 2048
BLOCK_WEIGHT = len(str(MAX_BLOCK_NUM)) + 1

board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def run():
    global board

    while True:
        render()

        if isLose() != False:
            print("You fucked it up!")
            quit()

        newBlock()
        inputKey = input("> ")

        if inputKey == "w":
            goUp()
        elif inputKey == "s":
            goDown()
        elif inputKey == "a":
            goLeft()
        elif inputKey == "d":
            goRight()
        else:
            print("Error input")

        run()


def render():
    global board
    for array in board:
        for each in array:
            if each == 2:
                print(
                    "\033[31m" + str(each).rjust(BLOCK_WEIGHT, " ") + "\033[0m", end=""
                )
            elif each == 4:
                print(
                    "\033[32m" + str(each).rjust(BLOCK_WEIGHT, " ") + "\033[0m", end=""
                )
            elif each == 8:
                print(
                    "\033[33m" + str(each).rjust(BLOCK_WEIGHT, " ") + "\033[0m", end=""
                )
            elif each == 16:
                print(
                    "\033[34m" + str(each).rjust(BLOCK_WEIGHT, " ") + "\033[0m", end=""
                )
            elif each == 32:
                print(
                    "\033[35m" + str(each).rjust(BLOCK_WEIGHT, " ") + "\033[0m", end=""
                )
            elif each == 64:
                print(
                    "\033[36m" + str(each).rjust(BLOCK_WEIGHT, " ") + "\033[0m", end=""
                )
            elif each == 128:
                print(
                    "\033[37m" + str(each).rjust(BLOCK_WEIGHT, " ") + "\033[0m", end=""
                )
            else:
                print(str(each).rjust(BLOCK_WEIGHT, " "), end="")

        print("\n")


def newBlock():
    global board
    row = random.randint(0, 3)
    colume = random.randint(0, 3)
    if board[row][colume] == 0:
        board[row][colume] = random.choice([2, 4])  # 新块是2或4
    else:
        newBlock()


def goUp():
    global board

    rotateBoard("l")
    goLeft()
    rotateBoard("r")


def goDown():
    global board

    rotateBoard("r")
    goLeft()
    rotateBoard("l")


def goLeft():  # 如果左边是0，就左移；如果左边是自己相同的，就相加
    global board

    for row in range(0, 4):  # 0,1,2,3
        # 向左靠拢
        zeros = [x for x in board[row] if x == 0]
        non_zeros = [x for x in board[row] if x != 0]

        board[row] = non_zeros + zeros

        for colume in range(1, 4):  # 1,2,3
            if board[row][colume] == board[row][colume - 1]:
                board[row][colume] = board[row][colume - 1] + board[row][colume]
                board[row][colume - 1] = 0
                zeros = [x for x in board[row] if x == 0]
                non_zeros = [x for x in board[row] if x != 0]

                board[row] = non_zeros + zeros


def goRight():
    global board

    rotateBoard("l")
    rotateBoard("l")

    goLeft()
    rotateBoard("r")
    rotateBoard("r")


def rotateBoard(direction):
    global board
    rows = len(board)
    cols = len(board[0])

    # 创建一个新的二维数组来存储旋转后的结果
    rotated = [[0] * rows for _ in range(cols)]

    if direction == "l":
        for i in range(rows):
            for j in range(cols):
                rotated[cols - 1 - j][i] = board[i][j]
    elif direction == "r":
        for i in range(rows):
            for j in range(cols):
                rotated[j][rows - 1 - i] = board[i][j]

    board = rotated


def isLose():
    global board
    for row in board:
        for num in row:
            if num == 0:
                return False


newBlock()
newBlock()
run()
