def sub(num ,r):
    '''for eat cat'''
    while r > 0:
        if num%10 == 0:
            num = num/10
        else:
            num -= 1
        r -= 1
    print(int(num))
        
num,r = input("Enter : ").split()
num,r = int(num),int(r)
sub(num,r)
