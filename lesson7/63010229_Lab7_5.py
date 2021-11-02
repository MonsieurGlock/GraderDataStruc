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
        operand = ('+','-','*','/')
        stack = []
        for i in data:
            if i in operand:
                newNode = Node(i)
                newNode.right = stack.pop(-1)
                newNode.left = stack.pop(-1)
                stack.append(newNode)
            else:
                newNode = Node(i)
                stack.append(newNode)
        self.root = stack[0]
        return self.root

    def infix(self,temp:Node):
        s = ''
        if temp.left != None:
            s += '(' + self.infix(temp.left)
        s += temp.data
        if temp.right != None:
            s += self.infix(temp.right) + ')'
        return s

    def prefix(self,temp):
        s = ''
        
        s += temp.data
        if temp.left != None:
            s += self.prefix(temp.left)
        if temp.right != None:
            s += self.prefix(temp.right)
        return s

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = input("Enter Postfix : ")
root = T.insert(inp)
print("Tree :")
T.printTree(root)
print("--------------------------------------------------")
print("Infix :",T.infix(root))
print("Prefix :",T.prefix(root))