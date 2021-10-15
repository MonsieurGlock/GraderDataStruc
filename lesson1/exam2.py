
print(" *** Divisible number ***")
inp = int(input("Enter a positive number : "))
total = 0
temp = []
if inp > 0:
    for i in range(1,inp+1):
        if inp%i == 0:
            total += 1
            temp.append(str(i))
    word = ' '.join(temp)
    print("Output ==> {}".format(word))
    print("Total ==> {}".format(total))

else:
    print("{} is OUT of range !!!".format(inp))


