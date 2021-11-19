class Node(object): 
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class AVL():
    def __init__(self) -> None:
        self.root = None
    
    def insert(self,node:Node,data):
        if node == None:
            return Node(data)
        elif data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node
    
    # def findRank(self,node:Node,li:list,position=0):
    #     if node.left == None and node.right == None:
    #         return li
    #     if node.left != None:
    #         li.insert(position,node.left.data)
    #         self.findRank(node.left,li,position-1)
    #     if node.right != None:
    #         li.insert(position,node.right.data)
    #         self.findRank(node.right,li,position+1)
    #     return li
    def findRank(self,node:Node,target):
        rank = 0
        if node == None:
            return rank
        rank += self.findRank(node.left,target)
        if target >= node.data:
            rank += 1
        rank += self.findRank(node.right,target)
        return rank

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

inp = input("Enter Input : ").split('/')
target = int(inp[1])
num = [int(i) for i in inp[0].split()]

T = AVL()
root = None
for i in num:
    root = T.insert(root,i)
printTree90(root)
print("--------------------------------------------------")
print("Rank of {} : {}".format(target,T.findRank(root,target)))


