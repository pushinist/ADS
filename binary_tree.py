class binary_tree:
    def __init__(self, lst: list = None) -> None:
        if lst is None:
            self.head = None
            return
        self.head = binary_tree.construct_head(lst)

    def preorder(self) -> list:
        return tree_node.preorder(self.head)

    def inorder(self) -> list:
        return tree_node.inorder(self.head)

    def postorder(self) -> list:
        return tree_node.postorder(self.head)

    @staticmethod
    def construct_head(lst: list, i=0):
        head = tree_node(lst[i])
        if (2 * i + 1) < len(lst):
            head.left = binary_tree.construct_head(lst, 2 * i + 1)
        if (2 * i + 2) < len(lst):
            head.right = binary_tree.construct_head(lst, 2 * i + 2)
        return head

    @staticmethod
    def from_list(lst: list, i=0):
        res = binary_tree()
        head = tree_node(lst[i])
        if (2 * i + 1) < len(lst):
            head.left = binary_tree.construct_head(lst, 2 * i + 1)
        if (2 * i + 2) < len(lst):
            head.right = binary_tree.construct_head(lst, 2 * i + 2)
        res.head = head
        return res

    @staticmethod
    def from_string(str: str):
        res = binary_tree()
        res.head = binary_tree.treeFromString(str)
        return res

    @staticmethod
    def findIndex(Str, start, end):
        if start > end:
            return -1
        stack = []
        for i in range(start, end + 1):
            if Str[i] == "(":
                stack.append(Str[i])
            elif Str[i] == ")":
                if stack[-1] == "(":
                    stack.pop(-1)
                    if len(stack) == 0:
                        return i
        return -1

    @staticmethod
    def treeFromString(Str: str, start=0, end=None):
        if end is None:
            end = len(Str) - 1
        if start > end:
            return None
        root = tree_node(ord(Str[start]) - ord("0"))
        index = -1
        if start + 1 <= end and Str[start + 1] == "(":
            index = binary_tree.findIndex(Str, start + 1, end)
        if index != -1:
            root.left = binary_tree.treeFromString(Str, start + 2, index - 1)
            root.right = binary_tree.treeFromString(Str, index + 2, end - 1)
        return root


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


def simplify(str):
    return str.replace(" ", "").replace(",", ")(").replace("()", "")



pig = simplify("8 (3 (1, 6 (4,7)), 10 (, 14(13,)))")
print(pig)
print(binary_tree.from_string(pig).inorder())
