#insertion sort แบบ recur
'''
Enter Input : 1 3 4 2
insert 3 at index 1 : [1, 3] [4, 2]
insert 4 at index 2 : [1, 3, 4] [2]
insert 2 at index 1 : [1, 2, 3, 4] 
sorted
[1, 2, 3, 4]
'''

def insert(result:list,li:list,n):
    if len(li) == 0:
        return result
    if len(result) == 0:
        result.append(li.pop(0))
        result = insert(result,li,n+1)
    else:
        # print(result)
        if li[0] < result[n-1] and n > 0:
            result = insert(result,li,n-1)
        else:
            temp = li[0]
            result.insert(n,li.pop(0))
            if len(li) == 0:
                print("insert {} at index {} : {}".format(temp,n,result))
            else:
                print("insert {} at index {} : {} {}".format(temp,n,result,li))
            result = insert(result,li,len(result))
    return result

# inp = [1,3,4,2]
# inp.insert(1,100)
inp = [int(i) for i in input("Enter Input : ").split()]
# print(inp)
s = insert([],inp,0)
print("sorted")
print(s)





