class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):  # 根节点
        self.root = TreeNode(root)

    def insert(self, val):
        if self.root is None:  # 如果根节点为空，插入
            self.root = TreeNode(val)
        else:  # 如果不为空 调用下面的方法，传入要插入的值和根节点
            self._insert(val, self.root)

    def _insert(self, val, curr_node):  # 传入参数：数值和当前节点
        if val < curr_node.val:  # 如果数值小于当前节点的值
            if curr_node.left is None:  # 如果当前节点的左子树为空
                curr_node.left = TreeNode(val)  # 当前节点的左子树添加值
            else:
                self._insert(val, curr_node.left)  # 否则在当前节点的左子树上添加左子树
        else:
            if curr_node.right is None:  # 同理添加右子树
                curr_node.right = TreeNode(val)
            else:
                self._insert(val, curr_node.right)

    def inorder_traversal(self, root):  # 遍历树，左中右
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=' ')
            self.inorder_traversal(root.right)

        # 使用示例


bt = BinaryTree(50)
bt.insert(30)
bt.insert(20)
bt.insert(40)
bt.insert(70)
bt.insert(60)
bt.insert(80)
bt.inorder_traversal(bt.root)  # 输出：20 30 40 50 60 70 80
