class tree_node:
    def __init__(self, value: int, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def preorder(node=None) -> list:
        if node is None:
            return []
        res = [node.value]
        if node.left is not None:
            res += tree_node.preorder(node.left)
        if node.right is not None:
            res += tree_node.preorder(node.right)
        return res

    @staticmethod
    def inorder(node=None) -> list:
        if node is None:
            return []
        res = []
        if node.left is not None:
            res += tree_node.inorder(node.left)
        res.append(node.value)
        if node.right is not None:
            res += tree_node.inorder(node.right)
        return res
    
    @staticmethod
    def postorder(node=None) -> list:
        if node is None:
            return []
        res = []
        if node.left is not None:
            res += tree_node.postorder(node.left)
        if node.right is not None:
            res += tree_node.postorder(node.right)
        res.append(node.value)
        return res


left_node = tree_node(2)
right_node = tree_node(3)
root = tree_node(1, left_node, right_node)
print(tree_node.preorder(root))
print(tree_node.inorder(root))
print(tree_node.postorder(root))
