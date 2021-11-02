class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class AVL:

    def insert(self,node:Node,data):
        if node == None:
            return Node(data)
        elif data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)

        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))

        temp = self.balace(node)

        if temp > 1 and data < node.left.data:
            return self.rightRotate(node)
        if temp < -1 and data > node.right.data:
            return self.leftRotate(node)
        
        if temp > 1 and data > node.left.data:
            root.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if temp > 1 and data < node.left.data:
            root.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def leftRotate(self,z:Node):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def rightRotate(self,z:Node):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def getHeight(self, node:Node):
        if not node:
            return 0
        return node.height

    def balace(self,node:Node):
        if node == None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right) 
    
    def printTree(self, node:Node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = AVL()
inp = [int(i) for i in input("Enter Input : ").split()]
root = None
for i in inp:
    print("Insert : ( {} )".format(i))
    root = T.insert(root,i)
    T.printTree(root)
    print("--------------------------------------------------")
# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.height = 1
 
# AVL tree class which supports the
# Insert operation
# class AVL_Tree(object):
 
#     # Recursive function to insert key in
#     # subtree rooted with node and returns
#     # new root of subtree.
#     def insert(self, root, key):
 
#         if not root:
#             return TreeNode(key)
#         elif key < root.val:
#             root.left = self.insert(root.left, key)
#         else:
#             root.right = self.insert(root.right, key)
 
#         root.height = 1 + max(self.getHeight(root.left),
#                            self.getHeight(root.right))
 
#         balance = self.getBalance(root)
 
        
#         if balance > 1 and key < root.left.val:
#             return self.rightRotate(root)
 
#         if balance < -1 and key > root.right.val:
#             return self.leftRotate(root)
 
#         if balance > 1 and key > root.left.val:
#             root.left = self.leftRotate(root.left)
#             return self.rightRotate(root)
 
#         if balance < -1 and key < root.right.val:
#             root.right = self.rightRotate(root.right)
#             return self.leftRotate(root)
 
#         return root
 
#     def leftRotate(self, z):
 
#         y = z.right
#         T2 = y.left
 
#         # Perform rotation
#         y.left = z
#         z.right = T2
 
#         # Update heights
#         z.height = 1 + max(self.getHeight(z.left),
#                          self.getHeight(z.right))
#         y.height = 1 + max(self.getHeight(y.left),
#                          self.getHeight(y.right))
 
#         # Return the new root
#         return y
 
#     def rightRotate(self, z):
 
#         y = z.left
#         T3 = y.right
 
#         # Perform rotation
#         y.right = z
#         z.left = T3
 
#         # Update heights
#         z.height = 1 + max(self.getHeight(z.left),
#                         self.getHeight(z.right))
#         y.height = 1 + max(self.getHeight(y.left),
#                         self.getHeight(y.right))
 
#         # Return the new root
#         return y
 
#     def getHeight(self, root):
#         if not root:
#             return 0
 
#         return root.height
 
#     def getBalance(self, root):
#         if not root:
#             return 0
 
#         return self.getHeight(root.left) - self.getHeight(root.right)
 
#     def preOrder(self, root):
 
#         if not root:
#             return
 
#         print("{0} ".format(root.val), end="")
#         self.preOrder(root.left)
#         self.preOrder(root.right)