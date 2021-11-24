
def insert(li):#น้อยไปมาก
    for i in range(1,len(li)):
        temp = li[i]
        for j in range(i,-1,-1):
            # print(i,j)
            if li[j-1] < temp  and j != 0:
                li[j] = li[j-1]
            else:
                li[j] = temp
                break
            print(i,j,li)

    return li


inp = [4,5,2,3,1]
print(inp)
print(insert(inp))


