class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)


class AVL_Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return TreeNode(data)
        else:
            if data < root.data:
                root.left = self.insert(root.left, data)
            elif data >= root.data:
                root.right = self.insert(root.right, data)

        root.height = 1 + max(self.getheight(root.left),
                              self.getheight(root.right))
        root = self.balance(root, data)
        return root

    def balance(self, root, data):
        balanceFactor = self.getheight(root.left) - self.getheight(root.right)
        if balanceFactor > 1:
            if root.left.data <= data:  # <# inside
                root.left = self.leftRotation(root.left)
            root = self.rightRotation(root)
        elif balanceFactor < -1:
            if root.right.data > data:  # ># inside
                root.right = self.rightRotation(root.right)
            root = self.leftRotation(root)

        return root

    def rightRotation(self, root):
        handRight = root.right

        handLeft = root.left
        temp = handLeft.right

        handLeft.right = root
        root.left = temp

        root.height = 1+max(self.getheight(root.left),
                            self.getheight(root.right))
        handLeft.height = 1 + \
            max(self.getheight(handLeft.left), self.getheight(handLeft.right))

        return handLeft

    def leftRotation(self, root):
        handRight = root.right
        handLeft = root.left

        temp = handRight.left
        handRight.left = root
        root.right = temp

        root.height = 1+max(self.getheight(root.left),
                            self.getheight(root.right))
        handRight.height = 1 + \
            max(self.getheight(handRight.left), self.getheight(handRight.right))
        return handRight

    def getheight(self, root):
        if root is None:
            return 0
        return root.height

    def preorder(self, node):
        ans = ""
        ans += str(node.data) + " "
        if node.left != None:
            ans += str(self.preorder(node.left))
        if node.right != None:
            ans += str(self.preorder(node.right))
        return ans

    def inorder(self, node):
        ans = ""
        if node.left != None:
            ans += str(self.inorder(node.left))
        ans += str(node.data) + " "
        if node.right != None:
            ans += str(self.inorder(node.right))
        return ans

    def postorder(self, node):
        ans = ""
        if node.left != None:
            ans += str(self.postorder(node.left))
        if node.right != None:
            ans += str(self.postorder(node.right))
        ans += str(node.data) + " "
        return ans


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


myTree = AVL_Tree()
root = None
print(" *** AVL Tree ***")
data = input("Enter some numbers : ").split()
for e in data:
    root = myTree.insert(root, int(e))
print("in_order  -->", myTree.inorder(root))
print("preorder  -->", myTree.preorder(root))
print("postorder -->", myTree.postorder(root))
