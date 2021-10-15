class Node():
    def __init__(self,data,next=None,prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class Link():
    def __init__(self, head = None) -> None:
        txt = ''
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1

    
    def append(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            t = self.head
            while t.next != None: #Run to last
                # print("Append")
                t = t.next
            t.next = newNode
            newNode.prev = t
            
    
    def getSize(self):
        t = self.head
        count = 0
        while t:
            # print("Size")
            t = t.next
            count += 1
        return count
    
    def isEmpty(self):
        if self.getSize() == 0:
            return True
        else:
            return False



    def getTail(self):
        if self.getSize() > 0:
            t = self.head
            while t.next != None:
                t = t.next
            return t
        else:
            return None

    def lookBack(self):
        if self.getSize() != 0:
            t = self.getTail()
            maxHeight = 0
            count = 0
            while t:
                # print("Back")
                if t.data > maxHeight:
                    maxHeight = t.data
                    count += 1
                t = t.prev
            print(count)
        else:
            print("0")

    def eat(self):
        if self.getSize() != 0:
            t = self.head
            while t:
                # print("Eat")
                if t.data % 2 == 0:
                    if t.data > 1:
                        t.data -= 1
                else:
                    t.data += 2
                t = t.next

def run(inp:list):
    li = Link()
    for i in inp:
        if i[0] == 'A':
            li.append(int(i.split()[1]))
        elif i == 'B':
            li.lookBack()
        elif i == 'S':
            li.eat()


inp = input("Enter Input : ").split(",")
run(inp)



