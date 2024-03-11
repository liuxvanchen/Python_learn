import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15  # 边框宽度
BOARD_ROWS, BOARD_COLS = 3, 3  # 有三行三列
SQUARE_SIZE = WIDTH // BOARD_COLS  # 设置每个格子的大小
CIRCLE_RADIUS = SQUARE_SIZE // 3  # 画的圈的半径
CIRCLE_WIDTH = 15  # 圆的线条宽度
CROSS_WIDTH = 25  # 叉的线条宽度
SPACE = SQUARE_SIZE // 4  # 画叉时边界宽度

# 颜色定义
BG_COLOR = (225, 158, 45)  # 底色
LINE_COLOR = (48, 34, 29)  # 交叉线颜色
CIRCLE_COLOR = (97, 178, 221)  # 圆的颜色
CROSS_COLOR = (87, 155, 46)  # 叉的颜色

# 设置屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("井字棋游戏")
screen.fill(BG_COLOR)

# 棋盘数据
board = [[None] * 3 for _ in range(3)]  # 每个格子初始为空
player = 0  # 0代表圆圈，1代表叉


# 绘制网格线
def draw_lines():
    # 水平线
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)#参数解释：要绘画的区域，颜色，起始点，终止点，线宽（默认为一）
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # 垂直线
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


# 绘制棋子
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                pygame.draw.circle(screen, CIRCLE_COLOR, (
                    int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 1:
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)


# 检查胜利
def check_win(player):
    # 检查行
    for row in range(BOARD_ROWS):
        if all([board[row][col] == player for col in range(BOARD_COLS)]):
            return True
    # 检查列
    for col in range(BOARD_COLS):
        if all([board[row][col] == player for row in range(BOARD_ROWS)]):#选择一列（外循环），然后看这一列里面所有的行（内循环）
            return True
    # 检查对角线
    if all([board[i][i] == player for i in range(BOARD_ROWS)]) or all(
            [board[i][BOARD_ROWS - i - 1] == player for i in range(BOARD_ROWS)]):#正对角和反对角
        return True
    return False


# 检查平局
def check_draw():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True


# 游戏循环
draw_lines()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not check_win(0) and not check_win(1):
            mouseX = event.pos[0]  # 获得鼠标按下的x坐标
            mouseY = event.pos[1]  # 获得y坐标

            clicked_row = mouseY // SQUARE_SIZE#求鼠标落在哪个格子
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = player
                if check_win(player):
                    print(f"Player {player + 1} wins!")
                    running = False
                player = (player + 1) % 2

                if check_draw():#检查平局
                    print("Draw!")
                    running = False

            draw_figures()
            pygame.display.update()
