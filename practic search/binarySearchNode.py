
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
class BST:
    def __init__(self):
        self.root = None

    def insert(self,data,node:Node):
        if node == None:
            if self.root == None:
                self.root = Node(data)
            else:
                node = Node(data)
        else:
            if data < node.data:
                if node.left != None:
                    self.insert(data,node.left)
                else:
                    node.left = Node(data)
            else:
                if node.right != None:
                    self.insert(data,node.right)
                else:
                    node.right = Node(data)

    def search(self,key,node):
        if node == None:
            return False
        elif node.data == key:
            return True
        if key < node.data:
            return self.search(key,node.left)
        else:
            return self.search(key,node.right)


    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i,T.root)
T.printTree(T.root)
key = 13
print(T.search(key,T.root))





