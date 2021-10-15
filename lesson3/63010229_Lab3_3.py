class Stack:

    def __init__(self):
        self.items = []
    def push(self, value):
        self.items = value
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return True if len(self.items) == 0 else False
    def delete(self,value):
        self.items.remove(value)
    def show(self):
        if self.isEmpty():
            return 'Empty'
        else: 
            
            listToStr = ''.join([str(elem) for elem in self.items])
            txt = listToStr[::-1]
            return txt
            
        


def count(S:Stack):
    temp = ''
    count = 0
    combo = 0
    i=0
    while i < S.size():
        if S.items[i] != temp:
            count = 0
            temp = S.items[i]
        else:
            count += 1
        
        if count == 2:
            for r in range(3):
               S.items.remove(temp) 
            combo += 1
            i = 0
            count = 0
            continue
        # print(temp , count)
        i += 1
    print(S.size())
    
    print(S.show())
    if combo > 1:
        print("Combo : {} ! ! !".format(combo))


    


inp = input('Enter Input : ').split()
# print(inp)

S = Stack()
S.push(inp)

count(S)

# print(S.size())

### Enter Your Code Here ###