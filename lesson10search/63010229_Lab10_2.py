



inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), list(map(int,inp[1].split()))
# print(arr,k)
for i in k:
    foundMax = False
    max = i
    for j in arr:
        if foundMax == False and j > max:
            max = j
            foundMax = True
        if j > i and j < max:
            max = j 
    if foundMax:
        print(max)
    else:
        print("No First Greater Value")
    



