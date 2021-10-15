
class Queue():
    def __init__(self,time:int = None,ls:list = None) -> None:
        if ls == None:
            self.items = []
        else:
            self.items = [ls]
        if time != None:
            self.time = time
        self.counter = 0
        self.isStart = False

    def enQueue(self,data):
        self.items.append(data)

    def deQueue(self):
        if self.isEmpty() == False:
            return self.items.pop(0)

    def isEmpty(self):
        if len(self.items) > 0:
            return False
        else:
            return True
    def isFull(self):
        if len(self.items) < 5:
            return False
        else:
            return True

    def count(self):
        if self.counter >= self.time:
            self.counter = 0
            self.deQueue()
        if len(self.items) != 0:
            self.counter += 1
        



def line(inp:list):
    i = 1
    aLine = Queue(0)
    aLine.items = inp
    c1 = Queue(3)
    c2 = Queue(2)
    # print(aLine.items)
    while aLine.isEmpty() == False:
        # c1.count()
        # c2.count()
        if c1.isStart == True:
            c1.count()
            if c1.isEmpty() == True:
                c1.isStart = False
        if c2.isStart == True:
            c2.count()
            if c2.isEmpty() == True:
                c2.isStart = False

        if c1.isFull() == False:
            c1.enQueue(aLine.deQueue())
            if c1.isStart == False:
                c1.isStart = True
                c1.count()
        elif c2.isFull() == False:
            c2.enQueue(aLine.deQueue())
            if c2.isStart == False:
                c2.isStart = True
                c2.count()
        
        
        print(i,aLine.items,c1.items,c2.items)
        
        i += 1


inp = [i for i in input("Enter people : ")]
line(inp)
# print(inp)

