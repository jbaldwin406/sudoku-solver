'''
Sudoku Solver
Uses backtracking algorithm to solve Sudoku board with given starting numbers
prints to terminal
'''
rows = 9
cols = 9


def solve(grid):
    position = find_empty_position(grid)

    # base case
    if not position:
        return True
    else:
        row, col = position

    for i in range(1, 10):
        if valid_position(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):
                return True

            # if value tried is not valid, reset position value to 0
            grid[row][col] = 0

    return False


def valid_position(grid, num, pos):
    # check if value we are trying to insert is already in row
    for i in range(rows):
        if grid[pos[0]][i] == num and pos[0] != i:
            return False

    # check if value we are trying to insert is already in col
    for i in range(cols):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # check if value we are trying to insert is already in the 'box'
    # first we set the following values to determine which 'box' we are in
    # i.e. we think of the top left 'box' as being at position[0][0] and 
    # next box in that row is position[0][1] etc
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # now that we have positions of the boxes in our grid, we need to multiply the values 
    # found above by 3, in order to get the indexes of each cell inside the box.
    # For example, the middle box on the top row (position[0][1]) the indexes of the cells:
    # [0][3] [0][4] [0][5]
    # [1][3] [1][4] [1][5]
    # [2][3] [2][4] [2][5]
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True 

# method to display the Sudoku grid
def display_grid(grid):
    for i in range(rows):
        if i % 3 == 0 and i != 0:
            print('- - - + - - - - + - - -')

        for j in range(cols):
            if j % 3 == 0 and j != 0:
                print(' | ', end = "")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end = "")


def find_empty_position(grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 0:
                return i, j # returning this as row, col
    # if there are no empty positions found, return None
    # serves as a trigger for solve method to be done
    return None 


if __name__ == '__main__':
    sudoku = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    print('Starting Sudoku Grid')
    display_grid(sudoku)
    solve(sudoku)
    print("_______________________")
    print('Solved Sudoku Grid')
    display_grid(sudoku)