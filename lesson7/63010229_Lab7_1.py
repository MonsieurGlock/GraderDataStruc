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

    def insert(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
        else:
            # print(self.root.data)
            temp = self.root
            while temp != None:
                if data < temp.data:
                    if temp.left == None:
                        temp.left = newNode
                        break
                    else:
                        temp = temp.left
                elif data >= temp.data:
                    if temp.right == None:
                        temp.right = newNode
                        break
                    else:
                        temp = temp.right
        return self.root
            
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)