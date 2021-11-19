class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)

class BTS:
    def insert(self,root:Node,data):
        if root == None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left,data)
        else:
            root.right = self.insert(root.right,data)
        return root

def toList(node:Node):
    result = []
    temp = []
    while node != None:
        if node.left != None:
            temp.append(node.left)
        if node.right != None:
            temp.append(node.right)
        result.append(node.data)
        if len(temp) > 0:
            node = temp.pop(0)
        else:
            node = None
    return result
            
            


def printTree(node, level = 0):
        if node != None:
            printTree(node.right, level + 1)
            print('     ' * level, node)
            printTree(node.left, level + 1)

def run(x,y,li:list):
    # x = li[(x*2)+1] + li[(x*2)+2]
    if (x*2)+2 < len(li):
        a = li[x] + li[(x*2)+1] + li[(x*2)+2]
    elif (x*2)+1 < len(li):
        a = li[x] + li[(x*2)+1]
    else:
        a = li[x]
    # x = li[(x*2)+1 if (x*2)+1 < len(li) else x] + li[(x*2)+2 if (x*2)+2 < len(li) else x]
    if (y*2)+2 < len(li):
        b = li[y] + li[(y*2)+1] + li[(y*2)+2]
    elif (y*2)+1 < len(li):
        b = li[y] + li[(y*2)+1]
    else:
        b = li[y]
    
    if a > b:
        print("{}>{}".format(x,y))
    elif a < b:
        print("{}<{}".format(x,y))
    else:
        print("{}={}".format(x,y))
    
    # print(x,y)
    # y = li[(y*2)+1] + li[(y*2)+2]

    


T = BTS()
inp = input("Enter Input : ").split('/')
num = [int(i) for i in inp[0].split()]
compar = [j.split() for j in [i for i in inp[1].split(',')]]
# print(compar)
root = None
for i in num:
    root = T.insert(root, i)
# printTree(root)

cat = toList(root)
sum = 0
for i in cat:
    sum += i
print(sum)
for i in compar:
    x = int(i[0])
    y = int(i[1])
    run(x,y,cat)