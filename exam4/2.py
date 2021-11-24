class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
    def __str__(self):
            return str(self.val)


class AVLTree:
    def __init__(self) -> None:
        self.root = None

    def getHeight(self, root):
        if not root:
            return 0
        else:
            return root.height

    def getBalance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right)

    def insert(self,val,root=None,isStart=False):
        if root == None:
            if self.root == None:
                self.root = Node(val)
                return
            else:
                if isStart == False:
                    root = self.root
                else:
                    return Node(val)
        print("H....")
        if val >= root.val:
            root.right = self.insert(val,root.right,True)
        else:
            root.left = self.insert(val,root.left,True)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and root.left.val >= val:
            return self.rotateRight(root)
        if balance < -1 and root.right.val < val:
            return self.rotateLeft(root)
        if balance > 1 and root.left.val <= val:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
        if balance < -1 and root.right.val > val:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        

        self.root = root


    def rotateRight(self, z):
        y = z.left
        T3 = y.right
        z.left = T3
        y.right = z
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rotateLeft(self, z):
        y = z.right
        T2 = y.left
        z.right = T2
        y.left = z
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

print(" *** AVL Tree ***")    
input_string = input("Enter some numbers : ")
bst = AVLTree()
for n in input_string.split():
	bst.insert(int(n))
printTree90(bst.root)
# bst.print_inorder()
# bst.print_preorder()
# bst.print_postorder()