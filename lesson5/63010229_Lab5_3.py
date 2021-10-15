class Node():
    def __init__(self,data,next=None) -> None:
        self.data = data
        self.next = next

class Link():
    def __init__(self, head = None) -> None:
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1

    
    def add(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            t = self.head
            while t.next != None: #Run to last
                t = t.next
            self.size += 1
            self.tail = t.next = newNode
    
    def getSize(self):
        t = self.head
        count = 0
        while t:
            t = t.next
            count += 1
        return count

    def pop(self,pos = -1):
        
        if self.getSize() > 0:
            if pos == -1:
                pos = self.getSize() - 1

            if pos == 0:
                result =  self.head.data
                temp = self.head.next
                del self.head
                self.head = temp
                return result
            elif pos < self.getSize() - 1:
                t = self.head
                for i in range(pos-1):
                    t = t.next
                result = t.next.data
                t.next = t.next.next
                return result
            elif pos == self.getSize() - 1:
                t = self.head
                while t.next.next != None:
                    t = t.next
                result = t.next.data
                del t.next
                t.next = None

                
                return result


    def getTail(self):
        t = self.head
        while t.next != None:

            t = t.next
        return t

    def show(self):
        txt = ''
        t = self.head
        while t:
            txt += str(t.data) + " "
            t = t.next
        return txt

    def reverse(self,head):
        if head is None or head.next is None:
            return head
 
        rest = self.reverse(head.next)
 
        head.next.next = head
        head.next = None

        return rest
    
def merge(L1:Link,L2:Link):
    L1.getTail().next = L2.head


inp = input("Enter Input (L1,L2) : ").split()
# print(inp[0].split("->"))
L1 = Link()
L2 = Link()
for i in inp[0].split("->"):
    L1.add(i)
for i in inp[1].split("->"):
    L2.add(i)
print("L1    :",L1.show())
print("L2    :",L2.show())
L2.head = L2.reverse(L2.head)
L1.getTail().next = L2.head
print("Merge :",L1.show())

