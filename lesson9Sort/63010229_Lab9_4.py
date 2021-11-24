#หาค่า median (มัธยฐาน)

def insertion(li):
    for i in range(1,len(li)):
        temp = li[i]
        for j in range(i,-1,-1):
            if temp < li[j-1] and j != 0:
                li[j] = li[j-1]
            else:
                li[j] = temp
                break
    return li

def findMedian(li):
    li = insertion(li)
    n = len(li)
    if n%2 == 1:
        pos = int(((n+1)/2)-1)
        med = li[pos]
    else:
        pos = int(((n+1)/2)-1)
        med = (li[pos] + li[pos+1])/2
    return med


l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    cat = []
    for i in l:
        cat.append(i)
        med = findMedian([i for i in cat])
        # med = 0
        print("list = {} : median = {:.1f}".format(cat,med))
        
    