
def findMax(inp,i,max):
    if i >= len(inp):
        return max
    else:
        if inp[i] > max:
            max = inp[i]
    return findMax(inp,i+1,max)





inp = [int(i) for i in input("Enter Input : ").split()]
print("Max : {}".format(findMax(inp,0,inp[0])))