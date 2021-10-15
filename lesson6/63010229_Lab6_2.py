
def toInt(arr:list,i):
    if i == len(arr):
        return arr
    else:
        arr[i] = int(arr[i])
        return toInt(arr,i+1)
    

def sort(arr:list,i,j):
    if i < len(arr):
        # print("i = ",i)
        if j < len(arr) - i-1:
            # print("j = ",j)
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
            return sort(arr,i,j)   
        else:
            j=0        
        i += 1
        return sort(arr,i,j)
    else:
        return arr



inp = input("Enter your List : ").split(",")
inp = toInt(inp,0)
print("List after Sorted :",sort(inp,0,0))
