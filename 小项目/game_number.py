import pygame
import random
import sys

pygame.init()

# 页面初始化
screen_width = 600
screen_height = 400

# 加上title
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("猜数字游戏")

# 字体设置
font = pygame.font.Font(None, 36)

# 随机生成一个目标数字
target_number = random.randint(1, 100)

# 输入框
input_text = ""

# 设置循环
running = True
hint_text = ""  # 初始化提示信息变量
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                try:
                    guess = int(input_text)
                    if guess < target_number:
                        hint_text = "The number is low!"
                    elif guess > target_number:
                        hint_text = "The number is high!"
                    else:
                        hint_text = "Yes you are right!"
                        running = False
                except ValueError:
                    hint_text = "Please enter a right number!"
                input_text = ""  # 清空输入框
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    screen.fill((255, 255, 255))

    # 显示输入框中的文字
    input_surface = font.render(input_text, True, (0, 0, 0))
    screen.blit(input_surface, (screen_width // 2 - input_surface.get_width() // 2, 150))

    # 显示提示信息
    hint_surface = font.render(hint_text, True, (0, 0, 0))
    screen.blit(hint_surface, (screen_width // 2 - hint_surface.get_width() // 2, 200))

    # 显示猜数字的提示
    text = font.render("Guess a number between 1 and 100: ", True, (0, 0, 0))
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, 100))

    pygame.display.flip()

pygame.quit()
sys.exit()