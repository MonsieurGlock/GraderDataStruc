class Stack :

    def __init__(self) :
        self.items = []
        
    def isEmpty(self) :
        if len(self.items) <= 0:
            return True
        else:
            return False
    def push(self,data) :
        self.items.append(data)
    def pop(self) :
        return self.items.pop()
    def size(self) :
        return len(self.items)
    def peek(self)->str:
        return self.items[-1]

def doing(str:list):
    s = Stack()
    for l in str:
        if l[0] == 'A':
            # print(l.split())
            if int(l.split()[1]) >= 1:
                s.push(int(l.split()[1]))
            else:
                s.push(1)
        if l[0] == 'B':
            i = s.size() - 1
            count = 0
            if i < 0:
                print(count)
            else:
                mostHi = 0
                for n in range(s.size() - 1,-1,-1):
                    # print("n",n)
                    if s.items[n] > mostHi:
                        count += 1
                        mostHi = s.items[n]
                print(count)
            # print(s.items)
            
        if l[0] == 'S':
            # print(s.items)
            for i in range(s.size()):
                if s.items[i] % 2 == 0:
                    if s.items[i] > 1:
                        s.items[i] -= 1
                else:
                    s.items[i] += 2
        # print(s.items)
        



x = input("Enter Input : ").split(",")
doing(x)
