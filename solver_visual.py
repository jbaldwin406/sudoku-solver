import pygame

pygame.font.init()
board_text = pygame.font.SysFont("couriernew", 40)
info_text = pygame.font.SysFont("couriernew", 20)

screen = pygame.display.set_mode((720, 720))

pygame.display.set_caption("SUDOKU")

x = 0
y = 0
dif = 600 / 9
val = 0

# Default Board
# TODO: add functionality to import boards from other sources
grid = [
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


# use this to get position of user click on board
def get_cords(pos):
    global x, y
    x, y = pos[0] // dif, pos[1] // dif


def highlight_cell():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)
                         * dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif,
                         y * dif), ((x + i) * dif, y * dif + dif), 7)


def draw_lines():
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                pygame.draw.rect(screen, (0, 153, 153),
                                 (i * dif, j * dif, dif + 1, dif + 1))
                nums1 = board_text.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(nums1, (i * dif + 5, j * dif + 5))

    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif),
                         (600, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0),
                         (i * dif, 600), thick)


def fill_val(val):
    nums1 = board_text.render(str(val), 1, (0, 0, 0))
    screen.blit(nums1, (x * dif + 5, y * dif + 5))


def raise_error():
    err = info_text.render("Incorrect", 1, (0, 0, 0))
    screen.blit(err, (20, 700))


def is_valid(board, i, j, val):
    for num in range(9):
        
        # check if value is already in column
        if board[i][num] == val:
            return False 

        # check if value is already in row
        if board[num][j] == val:
            return False 

    # check if value we are trying to insert is already in the 'box'
    # first we set the following values to determine which 'box' we are in
    # i.e. we think of the top left 'box' as being at position[0][0] and
    # next box in that row is position[0][1] etc
    box_x = i // 3
    box_y = j // 3

    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if board[i][j] == val:
                return False
    return True


def solve(grid, i, j):
    while grid[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for num in range(1, 10):
        if is_valid(grid, i, j, num) == True:
            grid[i][j] = num
            global x, y
            x = i
            y = j

            screen.fill((255, 255, 255))
            draw_lines()
            highlight_cell()
            pygame.display.update()
            pygame.time.delay(20)

            if solve(grid, i, j) == 1:
                return True
            else:
                grid[i][j] = 0

            screen.fill((255, 255, 255))
            draw_lines()
            highlight_cell()
            pygame.display.update()
            pygame.time.delay(50)
    return False


def instructions():
    ins_1 = info_text.render("PRESS D TO RESET TO DEFAULT / R TO CLEAR", 1, (0, 0, 0))
    ins_2 = info_text.render("ENTER VALUES AND PRESS ENTER TO SEE ALGO WORK", 1, (0, 0, 0))
    screen.blit(ins_1, (20, 610))
    screen.blit(ins_2, (20, 650))


def result():
    res_1 = info_text.render("ALGO DONE", 1, (0, 0, 0))
    screen.blit(res_1, (20, 680))




run = True
flag1 = 0
flag2 = 0 
rs = 0
error = 0

while run:

    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cords(pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                grid = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                grid = [ 
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
        if flag2 == 1:
            if solve(grid, 0, 0) == False:
                error = 1
            else:
                rs = 1
            flag2 = 0
        if val != 0:
            fill_val(val)
            if is_valid(grid, int(x), int(y), val) == True:
                grid[int(x)][int(y)] = val 
            else:
                grid[int(x)][int(y)] = 0
            val = 0
        if error == 1:
            raise_error()
        if rs == 1:
            result()
        draw_lines()
        if flag1 == 1:
            highlight_cell()
        instructions()

        pygame.display.update()

pygame.quit()
            