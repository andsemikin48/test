from collections import deque

class BinaryTree:
    def __init__(self, value, key):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def in_order(self):
        """in order"""
        if self.left:
            self.left.in_order()
        print(self.key, end=" ")
        if self.right:
            self.right.in_order()
        return

    def pre_order(self):
        print(self.key, end=" ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.key, end=" ")

    def insert(self, key):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = BinaryTree(True,key)
                else:
                    self.left.insert(key)
            else:
                if self.right is None:
                    self.right = BinaryTree(False,key)
                else:
                    self.right.insert(key)

    def bfs(self):
        if not self.key:
            return []
        queue = deque([self])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


    def search(self, key):
        if self.key == key:
            return f"Содержимое узла: {self.value}"
        elif key < self.key:
            if self.left:
                return self.left.search(key)
            else:
                return None
        else:
            if self.right:
                return self.right.search(key)
            else:
                return None

class AVLTree(BinaryTree):
    def __init__(self, key):
        super().__init__(True, key)
        self.height = 1

    def get_height(self,node):
        return node.height if node else 0

    def update_height(self):
        self.height = max(self.get_height(self.left), self.get_height(self.right)) + 1

    def check_balance(self):
        return self.get_height(self.left) - self.get_height(self.right)

    def insert(self, key):
        if key < self.key:
            if self.left:
                self.left = self.left.insert(key)
            else:
                self.left = AVLTree(key)
        else:
            if self.right:
                self.right = self.right.insert(key)
            else:
                self.right = AVLTree(key)

        self.update_height()
        bf = self.check_balance()

        # Левое
        if bf > 1 and self.left.check_balance() >= 0:
            return self.rotate_right()

        # Лево правое
        if bf > 1 and self.left.check_balance() < 0:
            self.left = self.left.rotate_left()
            return self.rotate_right()

        # правое
        if bf < -1 and self.right.check_balance() <= 0:
            return self.rotate_left()

        # право левое
        if bf < -1 and self.right.check_balance() > 0:
            self.right = self.right.rotate_right()
            return self.rotate_left()

        return self

    def rotate_left(self):
        new_root = self.right
        self.right = new_root.left
        new_root.left = self
        self.update_height()
        new_root.update_height()
        return new_root


    def rotate_right(self):
        new_root = self.left
        self.left = new_root.right
        new_root.right = self
        self.update_height()
        new_root.update_height()
        return new_root

tree = BinaryTree(True, 2)
tree.insert(1)
tree.insert(5)
tree.insert(10)
tree.insert(15)
print("BinaryTree:")
print("in order:")
tree.in_order()
print("\npre order:")
tree.pre_order()
print("\npost order:")
tree.post_order()
print('\nПоиск: ')
print(tree.search(10))
print('Обход в ширину: ', tree.bfs(), '\n')
#AVLTree
avl = AVLTree(10)

avl = avl.insert(20)
avl = avl.insert(30)
avl = avl.insert(5)
avl = avl.insert(15)

print("AVLTree:")
print("in order:")
avl.in_order()
print("\npre order:")
avl.pre_order()
print("\npost order:")
avl.post_order()