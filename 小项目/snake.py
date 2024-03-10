import pygame
import sys
import random

pygame.init()

# 设置窗口大小
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 设置窗口页面

# 设置标题
pygame.display.set_caption("贪吃蛇游戏")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BLOCK_SIZE = 20
SNAKE_SPEED = 6


class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]  # 起始位置，长宽的二分之一处
        # 双斜杠 // 是一个整数除法运算符。当你使用 // 来进行除法时，结果会被向下取整为最接近的整数。这与你使用单斜杠 / 进行除法时得到的结果不同，后者会返回一个浮点数。
        self.direction = "RIGHT"

    def move(self):
        head = self.body[0]
        if self.direction == "RIGHT":
            head = (head[0] + BLOCK_SIZE, head[1])
        elif self.direction == "LEFT":
            head = (head[0] - BLOCK_SIZE, head[1])
        elif self.direction == "UP":
            head = (head[0], head[1] - BLOCK_SIZE)
        elif self.direction == "DOWN":
            head = (head[0], head[1] + BLOCK_SIZE)

        self.body.insert(0, head)

        if head in self.body[1:]:  # 头碰上身体
            self.body.clear()  # 清除并重置游戏
            self.body.append((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        n = SCREEN_HEIGHT / BLOCK_SIZE
        m = SCREEN_WIDTH / BLOCK_SIZE
        if head[0] in [0, n] or head[1] in [0, m] or head[0] == m * BLOCK_SIZE or head[1] == SCREEN_HEIGHT:
            self.body.clear()  # 清除并重置游戏
            self.body.append((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE,
                                                        BLOCK_SIZE))  # 窗口页面，颜色，坐标设置（x，y和每个单位的大小，block_size是每个方格的大小


class Food:
    def __init__(self):
        self.x = random.randint(0, (SCREEN_WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE
        self.y = random.randint(0, (SCREEN_HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE

    def draw(self):
        pygame.draw.rect(screen, RED, pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))


snake = Snake()
food = Food()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # 运动的方向
            if event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"

    snake.move()

    if snake.body[0] == (food.x, food.y):  # 吃到食物
        food = Food()
    else:
        if snake.body[0] in snake.body[1:]:
            running = False

    screen.fill(WHITE)
    snake.draw()
    food.draw()
    pygame.display.flip()

    clock.tick(SNAKE_SPEED)

pygame.quit()
sys.exit()
