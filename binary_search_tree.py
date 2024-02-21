class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None
    

class Tree:
    def __init__(self) -> None:
        self.root = None
    

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False
        if value == node.data:
            return node, parent, True
        
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
            
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)
        return node, parent, False
            
        


    def append(self, obj):
        if self.root is None:
            self.root = obj
            return
        
        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        return

    def inorderTraversal(self, node):
        if node is None:
            return

        self.inorderTraversal(node.left)
        print(node.data, end=' ')
        self.inorderTraversal(node.right)

    def preorderTraversal(self, node):
        if node is None:
            return
        
        print(node.data, end=' ')
        self.preorderTraversal(node.left)
        self.preorderTraversal(node.right)
    

    def postorderTraversal(self, node):
        if node is None:
            return

        self.postorderTraversal(node.left)
        self.postorderTraversal(node.right)
        print(node.data, end=' ')


    def nonrecursive_inorderTraversal(self, node):
        current = node
        stack = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            
            elif stack:
                current = stack.pop()
                print(current.data, end=' ')                
                current = current.right
            else:
                break
        print()


    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None
    
    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left
                 

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
        
        return node, parent


    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None
        
        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)
    

    def find(self, node, key):
        if node is None or key == node.data:
            return node
        if key < node.data:
            return self.find(node.left, key)
        else:
            return self.find(node.right, key)

    def ascending_sort(self, node):
        if node is None:
            return

        self.inorderTraversal(node.left)
        print(node.data, end=' ')
        self.inorderTraversal(node.right)

    def descending_sort(self, node):
        if node is None:
            return

        self.descending_sort(node.right)
        print(node.data, end=' ')
        self.descending_sort(node.left)

def simplify(s: str):        
   return s.replace('(', '').replace(')', '').replace(',', '').split()


string = '8 (3 (1, 6 (4, 7)), 10 (, 14 (13,)))'

lst = list(map(int, simplify(string)))
print(lst)
t = Tree()
for x in lst:
    t.append(Node(x))   

#t.nonrecursive_inorderTraversal(t.root)
#t.ascending_sort(t.root)
t.preorderTraversal(t.root)
#print()
#t.descending_sort(t.root)