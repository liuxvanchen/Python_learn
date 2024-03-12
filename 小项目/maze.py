# import pygame
# import sys
# import numpy as np
#
#
# def generate_random_maze(width, height):
#     # 使用NumPy的random.randint函数生成一个width x height的二维数组
#     # 其中每个元素都是0或1，概率相等
#     maze = np.random.randint(2, size=(height, width))
#     for i in range(width):
#         for j in range(height):
#             if i == 0 or i == width - 1 or j == 0 or j == height - 1:
#                 maze[i][j] = 1  # 周围设置墙
#
#     maze[1][1] = 0  # 起始位置设为可走
#     maze[width - 2][height - 2] = -1  # 标记终点
#     return maze
#
#
# def stack(maze, stacks):
#     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#     start = maze[1][1]
#     stacks = [(1, 1)]
#     x_now = stacks[-1][1]  # 这里注意，x坐标是列号，如（1，2）入栈，那么这个格子的亨佐标是2
#     y_now = stacks[-1][0]
#     for x_add, y_add in directions:
#         x_next = x_now + x_add
#         y_next = y_now + y_add
#         type = maze[x_next][y_next]
#         if type <= 0:
#             stacks.append([x_next, y_next])
#             maze[x_next][y_next] = 1
#             if type == -1:
#                 return False
#             return True
#     stacks.pop(-1)
#     return True
#
#
# # 使用示例
# width = 11
# height = 11
# maze = generate_random_maze(width, height)
# # print(maze)
# stacks = []

# while stack(maze, stacks):
#     pass
# print(stacks)

import numpy as np


def generate_random_maze(width, height):
    maze = np.random.randint(2, size=(height, width))
    return maze


def find_path(maze, start, end):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    stack = [(start[0], start[1])]  # 初始栈，存储路径上的点
    visited = set([(start[0], start[1])])  # 记录已经访问过的点

    while stack:
        x, y = stack.pop()

        if (x, y) == end:
            return True  # 找到终点，返回True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 检查新坐标是否在迷宫内且未被访问过，且不是墙
            if 0 <= nx < maze.shape[0] and 0 <= ny < maze.shape[1] and (nx, ny) not in visited and maze[nx][ny] == 1:
                stack.append((nx, ny))
                visited.add((nx, ny))

    return False  # 没有找到路径，返回False


# 使用示例
width = 11
height = 11
maze = generate_random_maze(width, height)
for i in range(width):
    for j in range(height):
        if i == 0 or i == width - 1 or j == 0 or j == height - 1:
            maze[i][j] = 1  # 周围设置墙
maze[1][1] = 0  # 起始位置设为可走
maze[9][9] = 0  # 终点也设置为可走，不需要特殊标记

if find_path(maze, (1, 1), (9, 9)):
    print("找到路径！")
    print(maze)
else:
    print("未找到路径。")
    print(maze)