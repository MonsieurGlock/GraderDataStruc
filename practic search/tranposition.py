

def searchTran(li,key):
    for i in range(len(li)):
        if li[i] == key:
            if i > 0:
                li[i],li[i-1] = li[i-1],li[i]
                print("Found at :",i)
                break
            else:
                print("Found at :",i)
                break
    print(li)

inp = [11,12,20,5,80,8,20,2]
key = 11
searchTran(inp,key)











