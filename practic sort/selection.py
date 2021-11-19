
def select(li:list):
    for i in range(0,len(li)):
        max_index = i
        for j in range(i,len(li)):
            if li[j] < li[max_index]:
                max_index = j
        li[i],li[max_index] = li[max_index],li[i]
        print(":",li)
    return li




inp = [4,5,2,3,1]
print(inp)
print(select(inp))