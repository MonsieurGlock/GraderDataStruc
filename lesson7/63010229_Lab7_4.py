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

    def preorder(self,temp:Node)->str:
        s = ''
        s += str(temp.data) + ' '
        if temp.left != None:
            s += str(self.preorder(temp.left))
        if temp.right != None:
            s += str(self.preorder(temp.right))
        return s
    
    def inorder(self,temp:Node)->str:
        s = ''
        if temp.left != None:
            s += str(self.inorder(temp.left))
        s += str(temp.data) + ' '
        if temp.right != None:
            s += str(self.inorder(temp.right))
        return s

    def postorder(self,temp:Node)->str:
        s = ''
        if temp.left != None:
            s += str(self.postorder(temp.left))
        if temp.right != None:
            s += str(self.postorder(temp.right))
        s += str(temp.data) + ' '
        return s

    def breadth(self,temp:Node):
        q = []
        s=''
        while temp != None:
            s += str(temp.data) + " "
            if temp.left != None:
                q.append(temp.left)
            if temp.right != None:
                q.append(temp.right)
            
            temp = q.pop(0) if len(q) > 0 else None
        return s

        

 
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input("Enter Input : ").split()]
for i in inp:
    root = T.insert(i)
# print(T.printTree(root))
print("Preorder :",T.preorder(root))
print("Inorder :",T.inorder(root))
print("Postorder :",T.postorder(root))
print("Breadth :",T.breadth(root))
