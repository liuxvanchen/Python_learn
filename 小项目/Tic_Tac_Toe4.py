import pygame
import sys

pygame.init()

width, height = 400, 400
line_width = 20
rows, cols = 4, 4
square = width // cols
circle_d = square // 1.5
cross_line = 25
circle_line = 10
space = square // 4

# color
circle_color = (97, 178, 221)
cross_color = (87, 155, 46)
down_color = (225, 158, 45)
cross_line_color = (48, 34, 29)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("井字棋游戏4*4版")
screen.fill(down_color)

board = [[None] * 4 for _ in range(4)]
player = 0


def draw_lines():
    pygame.draw.line(screen, cross_line_color, (0, square), (width, square), line_width)
    pygame.draw.line(screen, cross_line_color, (0, 2 * square), (width, 2 * square), line_width)
    pygame.draw.line(screen, cross_line_color, (0, 3 * square), (width, 3 * square), line_width)

    pygame.draw.line(screen, cross_line_color, (square, 0), (square, height), line_width)
    pygame.draw.line(screen, cross_line_color, (square * 2, 0), (square * 2, height), line_width)
    pygame.draw.line(screen, cross_line_color, (square * 3, 0), (square * 3, height), line_width)


def draw_figures():
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                pygame.draw.circle(screen, circle_color,
                                   (int(col * square + square // 2), int(row * square + square // 2)), circle_d // 2,
                                   circle_line)
            elif board[row][col] == 1:
                start_x = col * square + space
                start_y = row * square + space
                end_x = col * square + square - space
                end_y = row * square + square - space
                pygame.draw.line(screen, cross_color, (start_x, start_y), (end_x, end_y), cross_line)
                pygame.draw.line(screen, cross_color, (start_x, end_y), (end_x, start_y), cross_line)


def check_win(player):
    for row in range(rows):
        if all([board[row][col] == player for col in range(cols)]):
            return True

    for col in range(cols):
        if all([board[row][col] == player for row in range(rows)]):
            return True

    if all([board[i][i] == player for i in range(rows)]) or all(
            [board[i][rows - i - 1] == player for i in range(rows)]):
        return True
    return False


def check_draw():
    for row in range(rows):
        for col in range(cols):
            if board[row][col] is None:
                return False
    return True


draw_lines()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not check_win(0) and not check_win(1):
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // square  # 求鼠标落在哪个格子
            clicked_col = mouseX // square

            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = player
                if check_win(player):
                    print(f"Player {player + 1} wins!")
                    running = False

                player = (player + 1) % 2  # 切换玩家

                if check_draw():  # 检查平局
                    print("Draw!")
                    running = False

            draw_figures()
            pygame.display.update()
