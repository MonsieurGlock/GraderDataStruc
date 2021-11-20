class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,size) -> None:
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append(None)

    def printTable(self):
        for i in range(self.size):
            print("#{}\t{}".format(i+1,self.table[i]))
            print('---------------------------')

    def insert()


print(" ***** Fun with hashing *****")
inp = input("Enter Input : ").split('/')
tableSize , maxCol = int(inp[0].split()[0]),int(inp[0].split()[1])
arr = inp[1].split(',')
hashTable = hash(tableSize)
hashTable.printTable()
# print(tableSize,maxCol,arr)
# for i in arr:
#     asc = 0
#     for j in i:
#         asc += ord(j)
#     print(asc%tableSize)