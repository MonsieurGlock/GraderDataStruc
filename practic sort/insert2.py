
def insert(li):
    for i in range(1,len(li)):
        temp = li[i]
        for j in range(i,-1,-1):
            if li[j-1] > temp and j != 0:
                li[j] = li[j-1]
            else:
                li[j] = temp
                break
        print(li)




inp = [4,5,1,3,7,9]
insert(inp)






