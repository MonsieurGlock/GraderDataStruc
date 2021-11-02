from typing import _get_type_hints_obj_allowed_types


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:

    def insert(self,node:Node,data):
        if node == None:
            return Node(data)
        elif data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        
        return node

    def findRank(self,node:Node,data,c=0):
        c = self.goLeft(node)

    def goLeft(self,node:Node):
        c = 0
        if node.left != None:
            c = self.goLeft(node.left)
        if node.right != None:
            c = self.goLeft(node.right)
        return c+1

    def goRight(self,node:Node):
        c = 0
        if node.right != None:
            c = self.goRight(node.right)
        if node.left != None:
            c = self.goRight(node.left)
        return c+1
        


    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = input("Enter Input : ")
s1 = [int(i) for i in inp.split('/')[0].split()]
s2 = int(inp.split('/')[1])
root = None
for i in s1:
    root = T.insert(root,i)
T.printTree(root)
print("--------------------------------------------------")
print("Rank of {} : {}".format(s2,T.goLeft(root)))
# print(T.findRank(root,s2))