from random import randint


class Board:  # complex data type in global scope
    data = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    def draw(self):  # program is split into functions
        for a, row in enumerate(self.data):
            for i, element in enumerate(row):
                if i == 2:
                    print(element)
                else:
                    print(element, '│', end=' ')
            if a < 2:
                print('─────────')

    def move(self, row, column, cell):
        self.data[row][column] = cell

    def make_random_move(self):  # random data generation
        row = 0
        column = 0
        while True:
            row = randint(0, 2)
            column = randint(0, 2)
            if self.data[row][column] == "X" or self.data[row][column] == "0":
                continue
            break
        self.data[row][column] = "0"

    def check_win(self, symbol):
        for row in self.data:  # for loop
            if row[0] == symbol and row[1] == symbol and row[2] == symbol:
                return True
        for index, element in enumerate(self.data[0]):
            if element == symbol and self.data[1][index] == symbol and self.data[2][index] == symbol:
                return True
        if self.data[0][0] == symbol and self.data[1][1] == symbol and self.data[2][2] == symbol:
            return True
        if self.data[0][2] == symbol and self.data[1][1] == symbol and self.data[2][0] == symbol:
            return True
        return False


def read_input(board: Board):  # interaction with human
    while True:  # while loop
        u_input = -1
        while u_input not in range(0, 9):
            u_input = int(input("Pick your cell(1-9): "))
        row = 0
        column = 0

        if u_input <= 3:  # if elif else instructions
            row = 0
            column = u_input - 1
        elif u_input <= 6:
            row = 1
            column = u_input - 4
        else:
            row = 2
            column = u_input - 7

        if board.data[row][column] == "X" or board.data[row][column] == "0":
            continue

        return row, column


board = Board()

while True:
    row, column = read_input(board)
    board.move(row, column, 'X')
    board.make_random_move()
    if board.check_win('X'):
        print("User wins")
        break
    elif board.check_win('0'):
        print("Computer wins")
        break

    board.draw()

board.draw()
