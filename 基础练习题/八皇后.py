def check(board, row, col):
    """
    检查在 (row, col) 位置放置皇后是否安全（不被其他皇后攻击）

    Args:
    - board: 当前棋盘状态，一个一维数组，表示每一行皇后的列位置
    - row: 当前行
    - col: 当前列

    Returns:
    - True: 如果安全
    - False: 如果不安全
    """
    # 检查同一列是否有其他皇后
    for i in range(row):
        if board[i] == col:
            return False

    # 检查左上方对角线是否有其他皇后
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # 检查右上方对角线是否有其他皇后
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board), 1)):
        if board[i] == j:
            return False

    # 如果在同一列和对角线上都没有其他皇后，返回安全
    return True


def queens(n):
    """
    解决八皇后问题并返回所有解决方案

    Args:
    - n: 棋盘大小，即皇后的数量

    Returns:
    - result: 所有解决方案的列表，每个解决方案是一个一维数组，表示每一行皇后的列位置
    """
    def place_queen(board, row):
        """
        递归放置皇后，直到所有皇后都放置在棋盘上

        Args:
        - board: 当前棋盘状态，一个一维数组，表示每一行皇后的列位置
        - row: 当前行
        """
        if row == n:
            # 如果所有皇后都放置在棋盘上，将当前棋盘状态添加到结果中
            result.append(board[:])
            return

        for col in range(n):
            # 尝试在当前行的每一列放置皇后
            if check(board, row, col):
                # 如果当前位置安全，放置皇后并递归到下一行
                board[row] = col
                place_queen(board, row + 1)

    # 初始化结果列表和棋盘状态
    result = []
    board = [-1] * n

    # 从第0行开始递归放置皇后
    place_queen(board, 0)

    # 返回所有解决方案
    return result


# 解决八皇后问题（n=8）
n = 8
solutions = queens(n)

# 打印所有解决方案
for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    for row in solution:
        # 将皇后的位置用 Q 表示，未放置皇后的位置用 _ 表示
        print("".join(["Q" if j == row else "_" for j in range(n)]))
    print()
