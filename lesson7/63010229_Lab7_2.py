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

    def below(self,temp:Node,check)->str:
        s = ''
        if temp.left != None:
            s += str(self.below(temp.left,check))
        
        if int(temp.data) < check:
            s += str(temp.data) + " "

        if temp.right != None:
            s += str(self.below(temp.right,check))
        
        return s
            
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ').split('|')
num = [int(i) for i in inp[0].split()]
for i in num:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
s = T.below(root,int(inp[1]))
if len(s) == 0:
    s = "Not have"
print("Below {} : {}".format(inp[1],s))
