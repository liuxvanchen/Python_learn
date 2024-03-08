from collections import deque


def bfs(graph, root):
    visited = set()
    queue = deque([root])

    while queue:
        vertex = queue.popleft()  # 出队：移除并返回队列的第一个元素
        print(vertex, end=" ")  # 访问节点

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)  # 入队：将邻居节点添加到队列的尾部


# 定义图的邻接列表表示
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

# 执行广度优先搜索
bfs(graph, 'A')  # 输出: A B C D E F