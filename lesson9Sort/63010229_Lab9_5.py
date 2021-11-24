def combination(arr):
    com = []
    for i in range(1, len(arr) + 1):
        com.extend(combo_recur(arr, i))
    return com


def combo_recur(arr, n):
    if n == 0:
        return [[]]
    combo = []
    for i in range(len(arr)):
        strt = arr[i]
        rem = arr[i + 1:]
        for j in combo_recur(rem, n - 1):
            combo.append(sort([strt] + j))
    return sort(combo)


def sort(arr):
    for i in range(len(arr)):
        minindex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j
        arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr


inp = input("Enter Input : ").split("/")
ans = int(inp[0])
lstval = [int(x) for x in inp[1].split()]
sublst = combination(lstval)

out = []
for item in sublst:
    sumval = 0
    for i in range(len(item)):
        sumval += item[i]
    if sumval == ans:
        out.append(item)
if len(out) != 0:
    for i in out:
        print(i)
else:
    print("No Subset")