
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



print(" *** Bubble sort ***")    
input_string = input("Enter some numbers : ")
A=[]
for n in input_string.split():
	A.append(int(n))
# bubble_sort(A)
count = 0
for i in range(len(A)):
    swap = False
    for j in range(len(A)-i-1):
        count += 1
        if A[j] > A[j+1]:
            swap = True
            A[j] , A[j+1] = A[j+1],A[j]
    if swap == False:
        break 
print()
print(A)
print("Data comparison =", count)


