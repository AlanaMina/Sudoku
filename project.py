"""
File: project.py
"""


def main():
    puzzle = 9  # int(input("What kind of puzzle do you want to play? "))
    print("Welcome to Sudoku Solver")
    print("Original grid")
    """
    print("Please enter the values corresponding to the coordinates. Row by row:")
    sudoku = []
    for i in range(puzzle):
        sudoku.append([])
        for j in range(puzzle):
            nro = input(str(i) + str(j) + ": ")
            if nro == "" or 0:
                sudoku[i].append(0)
            else:
                sudoku[i].append(int(nro))

    """
    """
    sudoku = [[0, 3, 0, 0, 0, 0, 9, 0, 0], [0, 6, 9, 0, 8, 0, 2, 1, 7], [0, 1, 0, 4, 9, 2, 0, 0, 0],
              [9, 7, 3, 5, 6, 0, 0, 2, 0], [0, 5, 0, 0, 0, 0, 8, 3, 0], [1, 0, 0, 9, 0, 0, 5, 0, 0],
              [0, 2, 4, 0, 0, 0, 3, 6, 1], [0, 0, 6, 0, 3, 7, 4, 0, 2], [0, 8, 0, 0, 0, 6, 0, 0, 0]]

    """
    sudoku = [[0, 3, 0, 0, 0, 0, 9, 0, 0], [0, 6, 9, 0, 8, 0, 2, 1, 7], [0, 1, 0, 4, 9, 2, 0, 0, 0],
              [9, 7, 3, 5, 6, 0, 0, 2, 0], [0, 5, 0, 0, 0, 0, 8, 3, 0], [1, 0, 0, 9, 0, 0, 5, 0, 0],
              [0, 2, 4, 0, 0, 0, 3, 6, 1], [0, 0, 6, 0, 3, 7, 4, 0, 2], [0, 8, 0, 0, 0, 6, 0, 0, 0]]

    """
    sudoku = [[0, 3, 0, 0, 0, 0, 9, 0, 0], [0, 6, 9, 0, 8, 0, 2, 1, 7], [0, 1, 0, 4, 9, 2, 0, 0, 0],
              [9, 7, 3, 5, 6, 0, 0, 2, 0], [0, 5, 0, 0, 0, 0, 8, 3, 0], [1, 0, 0, 9, 0, 0, 5, 0, 0],
              [0, 2, 4, 0, 0, 0, 3, 6, 1], [0, 0, 6, 0, 3, 7, 4, 0, 2], [0, 8, 0, 0, 0, 6, 0, 0, 0]]
    
    sudoku = [[0, 3, 0, 0, 0, 0, 9, 0, 0], [0, 6, 9, 0, 8, 0, 2, 1, 7], [0, 1, 0, 4, 9, 2, 0, 0, 0],
              [9, 7, 3, 5, 6, 0, 0, 2, 0], [0, 5, 0, 0, 0, 0, 8, 3, 0], [1, 0, 0, 9, 0, 0, 5, 0, 0],
              [0, 2, 4, 0, 0, 0, 3, 6, 1], [0, 0, 6, 0, 3, 7, 4, 0, 2], [0, 8, 0, 0, 0, 6, 0, 0, 0]]
    """

    print_board(sudoku, puzzle)

    numbers = []
    for i in range(puzzle):
        numbers.append(i+1)

    solved(puzzle, sudoku, numbers)
    print("")
    print("+++++++++++++++++++++++++")
    print("")
    print("Solved grid")
    print_board(sudoku, puzzle)


def solved(puzzle, sudoku, numbers):
    blank = find_empty_places(puzzle, sudoku)
    if blank:
        row, column = find_empty_places(puzzle, sudoku)
    else:
        return True

    for number in range(1, len(numbers) + 1):
        if is_possible(puzzle, sudoku, row, column, number):
            sudoku[row][column] = number
            if solved(puzzle, sudoku, numbers):
                return True
            sudoku[row][column] = 0
    return False


def find_empty_places(puzzle, sudoku):
    for i in range(puzzle):
        for j in range(puzzle):
            if sudoku[i][j] == 0:
                return i, j
    return None


def print_board(sudoku, puzzle):
    for i in range(puzzle):
        if i % 3 == 0:
            print("-------------------------")
        for j in range(puzzle):
            if j % 3 == 0 and j != 0 and j != 8:
                print(" | " + str(sudoku[i][j]), end="")
            elif j == 0:
                print("| " + str(sudoku[i][j]), end="")
            elif j == 8:
                print(" " + str(sudoku[i][j]) + " |")
            else:
                print(" " + str(sudoku[i][j]) + "", end="")
    print("-------------------------")


def is_possible(puzzle, sudoku, row, column, number):
    rectangle = 3  # 3x3
    for i in range(puzzle):
        if sudoku[row][i] == number:
            return False
    for j in range(puzzle):
        if sudoku[j][column] == number:
            return False
    initial_row = (row // 3) * 3
    initial_column = (column // 3) * 3
    for i in range(rectangle):
        for j in range(rectangle):
            if sudoku[initial_row + i][initial_column + j] == number:
                return False
    return True


if __name__ == '__main__':
    main()
