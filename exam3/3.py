
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

inp = [int(i) for i in input("Enter Input : ").split()]

if inp[0] < inp[1]:
    inp[0],inp[1] = inp[1],inp[0]
if inp[0] < 0 and inp[1] < 0:
    inp[0],inp[1] = inp[1],inp[0]

ans = gcd(inp[0],inp[1])
if ans < 0:
    ans *= -1
if inp[0] != 0 or inp[1] != 0:
    print("The gcd of {} and {} is : {}".format(inp[0],inp[1],ans))
else:
    print("Error! must be not all zero.")
