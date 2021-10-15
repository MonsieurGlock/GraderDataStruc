

# x = Enter number and shiftcount : 3888 4

# x,bit = input("Enter number and shiftcount : ").split()


def Rshift(num,shift):

    num >>= shift
    return num
    

n,s = input("Enter number and shiftcount : ").split()

print(Rshift(int(n),int(s)))



# print("{} {}".format(x,bit))








