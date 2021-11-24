def bubble_sort(li):
    count = 0
    for i in range(len(li)):
        swap = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                swap = True
                li[j] , li[j+1] = li[j+1],li[j]
        if swap == False:
            break
    return [li,count] 

def shell_sort(li,count=0):
    se = [4,2,1]
    
    for i in se:
        temp = []
        j = 1
        while len(temp) <= len(li):
            temp.append(j)
            j += 1
            if j > i:
                j = 1
        print(temp)
        new = []
        j = 1
        while len(temp) <= len(li):
            temp.append(j)
            j += 1
            if j > i:
                j = 1
        # for m in range(i):
        #     for k in range(len(temp)):
        #         if temp[k] == m:
        #             new.append(li[k])
        print(new)
        output = bubble_sort(new)
        count += output[1]
        new = output[0]
        for k in range(len(li)):
            if temp[k] == i and len(new) != 0:
                li[k] = new.pop(0)
    print(li,count)
                


print(" *** Shell sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
shell_sort(A)

count = 0
print()
print(shell_sort(A))
print("Data comparison = ", count)