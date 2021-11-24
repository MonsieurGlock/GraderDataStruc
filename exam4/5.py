def mergeSort(arr,count):
    if len(arr) > 1:

        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        count = mergeSort(L,count)
        count = mergeSort(R,count)
  
        i = j = k = 0

        while i < len(L) and j < len(R):
            count += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            # count += 1
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            # count += 1
            arr[k] = R[j]
            j += 1
            k += 1
    return count
  

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  

if __name__ == '__main__':
    count = 0
    print(" *** Merge sort ***")
    arr = [int(i) for i in input("Enter some numbers : ").split()]

    print()
    count = mergeSort(arr,count)
    print("Sorted -> ", end="")
    printList(arr)
    print("Data comparison = ",count)