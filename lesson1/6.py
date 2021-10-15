inp = input("Input : ").split()
x,y = int(inp[0]) , int(inp[1])
sum = x * y
if sum > 1000:
    print("Sum is {}".format(sum))
else:
    print("{} * {} = {}".format(x,y,sum))


