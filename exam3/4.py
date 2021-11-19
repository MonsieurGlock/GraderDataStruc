class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def list_to_bst(list_nums,i,j):
    # root = None
    # for i in list_nums:
    #     if root == None:
    #         root = TreeNode(i)
    #     else:
    #         temp = root
    #         while temp != None:
    #             if i < temp.val:
    #                 if temp.left == None:
    #                     temp.left = TreeNode(i)
    #                     break
    #                 else:
    #                     temp = temp.left
    #             else:
    #                 if temp.right == None:
    #                     temp.right = TreeNode(i)
    #                     break
    #                 else:
    #                     temp = temp.right
    if i > j:
        return None
    
    mid = (i+j+1)//2
    root = TreeNode(list_nums[mid])
    root.left = list_to_bst(list_nums,i,mid-1)
    root.right = list_to_bst(list_nums,mid+1,j)
    return root


def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)   


def printBST(node,level = 0):
    if node != None:
        printBST(node.right, level + 1)
        print('     ' * level, node.val)
        printBST(node.left, level + 1)


list_nums = sorted([int(item) for item in input("Enter list : ").split()])

result = list_to_bst(list_nums,0,len(list_nums)-1)

print("\nList to a height balanced BST : ")
print(preOrder(result))
print("\nBST model : ")
printBST(result)