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
    return count

def shell_sort(li):
    count = 0
    gap = 8 // 2 # initialize the gap
    while gap > 0:
        i = 0
        j = gap
        while j < len(li):
            if li[i] >li[j]:
                li[i],li[j] = li[j],li[i]
            i += 1
            j += 1
            k = i
            while k - gap > -1:
                count += 1
                if li[k - gap] > li[k]:
                    li[k-gap],li[k] = li[k],li[k-gap]
                k -= 1
 
        gap //= 2
    return count

print(" *** Shell sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
count = shell_sort(A)

print()
print(A)

print("Data comparison = ", count)







