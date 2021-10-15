
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
        # t = self.head
        # while t.next != None:
        #     pre = t
        #     t = t.next
        # else:
        #     pre.next = None
        #     result = t.data
        #     del t
        #     self.size -= 1
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
                
                # if t.next.next == None:
                #     return t.next.data
                # if count == pos:
                #     return pre.data
                # pre = t
                # t = t.next
                # count += 1



    def getTail(self):
        t = self.head
        while t.next != None:

            t = t.next
        return t

    def show(self):
        txt = ''
        t = self.head
        while t:
            txt += str(t.data) + "->"
            t = t.next
        print(txt)

inp = [1,2,3,4,5]
li = Link()
for i in inp:
    li.add(i)

li.show()
# print(li.pop(1))
# print(li.pop(-1))
li.i
li.show()
