class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,size,collision) -> None:
        self.size = size
        self.table = []
        self.collision = collision
        for i in range(size):
            self.table.append(None)

    def printTable(self):
        for i in range(self.size):
            print("#{}\t{}".format(i+1,self.table[i]))
        print('---------------------------')

    def encode(self,key):
        asc = 0
        for j in key:
            asc += ord(j)
        return asc%self.size

    def isFull(self):
        for i in range(self.size):
            if self.table[i] == None:
                return False
        return True

    def insert(self,data:list):
        insertKey = self.encode(data[0])
        if self.table[insertKey] == None:
            self.table[insertKey] = Data(insertKey,data[1])
        else:
            print("collision number {} at {}".format(self.table[insertKey],insertKey))
            i = 1
            colli = 1
            while colli < self.collision:
                insertKey = (insertKey + i**2)%self.size
                if self.table[insertKey] == None:
                    self.table[insertKey] = Data(insertKey,data[1])
                    break
                else:
                    print("collision number {} at {}".format(self.table[insertKey].key,insertKey))
                    i += 1
                    colli += 1
                    if colli >= self.collision:
                        print("Max of collisionChain")
                        break
        self.printTable()
                    


print(" ***** Fun with hashing *****")
inp = input("Enter Input : ").split('/')
tableSize , maxCol = int(inp[0].split()[0]),int(inp[0].split()[1])

arr = inp[1].split(',')
hashTable = hash(tableSize,maxCol)
for i in arr:
    temp = i.split()
    hashTable.insert(temp)
    if hashTable.isFull():
        print("This table is full !!!!!!")
        break
# print(tableSize,maxCol,arr)
# for i in arr:
#     asc = 0
#     for j in i:
#         asc += ord(j)
#     print(asc%tableSize)