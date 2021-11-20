#รับ input เป็น list แล้วแสดงขั้นตอนของ bubble sort ตามตัวอย่า
def bubble(li):
    for i in range(len(li)):
        swapped = False
        c=0
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                c+=1
                swapped = True
                li[j],li[j+1] = li[j+1],li[j]
        
        min = li[0]
        sort = True
        for k in li:
            if min > k:
                sort = False
            else:
                min = k
        
        
        if swapped == True:
            print("{} step : {} move[{}]".format(i+1,li,c+1))
        elif sort == True:
            if c==0:
                print("last step : {} move[None]".format(li))
            else:
                if len(li) == 4:
                    print("last step : {} move[{}]".format(li,c+1))
                    break
                else:
                    print("last step : {} move[{}]".format(li,c+1))
            break
        

        
        # else:
        #     print("last step : {} move[None]".format(li))
    # print(li)

# inp = [int(i) for i in input("Enter Input : ").split()]
inp = [int(i) for i in input("Enter Input : ").split()]
bubble(inp)


