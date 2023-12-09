import random

MAX_BLOCK_NUM = 2048
BLOCK_WEIGHT = len(str(MAX_BLOCK_NUM)) + 1

board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def run():
    global board

    while True:
        render()

        if isAllFilled() and not has_adjacent_numbers():
            print("You fucked it up!")
            quit()

        inputKey = input("> ")

        if inputKey == "w":
            goUp()
            newBlock()
        elif inputKey == "s":
            goDown()
            newBlock()
        elif inputKey == "a":
            goLeft()
            newBlock()
        elif inputKey == "d":
            goRight()
            newBlock()

        else:
            print("Error input")


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
    empty_cells = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                empty_cells.append((i, j))
    if empty_cells:
        row, column = random.choice(empty_cells)
        board[row][column] = random.choice([2, 4])


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


def isAllFilled():
    global board
    for row in board:
        for num in row:
            if num == 0:
                return False
    return True


def has_adjacent_numbers():
    global board
    array = board
    rows = len(array)
    cols = len(array[0])

    for i in range(rows):
        for j in range(cols):
            current_number = array[i][j]
            # 检查右边的元素
            if j + 1 < cols and array[i][j + 1] == current_number:
                return True
            # 检查下面的元素
            if i + 1 < rows and array[i + 1][j] == current_number:
                return True
    return False

if __name__ == "__main__":
    newBlock()
    newBlock()
    run()
