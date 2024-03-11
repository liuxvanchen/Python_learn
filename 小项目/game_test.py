import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("pygame-test")

# 文本显示加上换行功能

screen.fill((228, 226, 151))  # 屏幕颜色
fonts = pygame.font.Font('C:\Windows\Fonts\FZSTK.TTF', 36)
input_text = "Good morning dear miss LiMu :)123456789/97aduyuaygsduygfeiwuhduygyujhaiudsgfbuyjghirkdgfgyuyijknfdgxvgyuyi;yauiuidshfbuytiyuherfd"

lines = []
current_line = ""

for char in input_text:  # 循环输入的字符
    current_line += char
    if fonts.size(current_line)[0] > screen_width - 100:  # 设置最长的字符长度
        lines.append(current_line)
        current_line = ""  # 重置当前行
        if char in (" ", ".", ",", ";", "!", "?"):  # 判断是不是标点符号或空格
            lines.append(char)
        else:
            current_line = char
    elif char == '\n':
        lines.append(current_line)
        current_line = ""

if current_line:
    lines.append(current_line)

y_position = 100  # 第一行起始的y位置
for line in lines:  # 循环打印每一行
    text_surface = fonts.render(line, False, (0, 0, 0))  # 这里的fonts就是上面设置的字体格式,.render方法：要显示的文本，是否抗锯齿，颜色
    screen.blit(text_surface, (screen_width // 2 - text_surface.get_width() // 2, y_position))  # 渲染文本，blit：文本，位置，
    y_position += text_surface.get_height() + 10  # 设置了行间距，每次增加5
# input_surface = font.render(input_text,True, (0, 0, 0))

pygame.display.flip()

# 运行游戏循环（这里只是简单显示文本并等待用户关闭窗口）
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
