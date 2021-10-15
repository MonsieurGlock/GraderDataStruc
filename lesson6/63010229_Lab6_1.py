
def factor(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factor(num-1)

inp = int(input("Enter Number : "))
print("{}! = {}".format(inp,factor(inp)))