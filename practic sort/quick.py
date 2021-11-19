
def pivot(li,i,j):



def quick(li,i,j):
        



inp = [4,5,2,3,1]
print(inp,0,len(inp)-1)













def partition(start, end, array):
    pivot_index = start 
    pivot = array[pivot_index]
      
    while start < end:
          
        while start < len(array) and array[start] <= pivot:
            start += 1
              
        while array[end] > pivot:
            end -= 1
          
        if(start < end):
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]
     
    return end
def quick_sort(start, end, array):
      
    if (start < end):
          
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
    return array
          
# Driver code
array = [ 10, 7, 8, 9, 1, 5 ]

  
print(quick_sort(0, len(array) - 1, array))