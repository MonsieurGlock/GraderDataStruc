class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self) -> None:
        pass
    # Code Here
    pass

print(" ***** Fun with hashing *****")
inp = input("Enter Input : ").split('/')
tableSize , maxCol = int(inp[0].split()[0]),int(inp[0].split()[1])
arr = inp[1].split(',')
print(tableSize,maxCol,arr)
for i in arr:
    asc = 0
    for j in i:
        asc += ord(j)
    print(asc%tableSize)