

def heap(li):
    for i in range(1,len(li)):
        temp = li[i]
        pos = (i-1)//2
        while i > 0 and temp < li[pos]:
            li[i] = li[pos]
            i = pos
            pos = (i-1)//2
        li[i] = temp
    print(li)


inp = [4,5,2,3,1]
heap(inp)




