#input = 6 3 -2 5 -8 2 -2
#output = 2 3 -2 5 -8 6 -2

#-99 5 -8 60 -77 49
#-99 5 -8 49 -77 60
def insertSort(li)->list:
    for i in range(1,len(li)):
        temp= li[i]
        if temp < 0:
            continue
        for j in range(i,-1,-1):
            if li[j] >= 0:
                n = 1
                while li[j-n] < 0 and j-n >= 0:
                    n += 1
                if temp < li[j-n] and j-n >= 0:
                    li[j] = li[j-n]
                else:
                    li[j] = temp
                    break

    return li

inp = [int(i) for i in input("Enter Input : ").split()]
print(' '.join(map(str,insertSort(inp))))

