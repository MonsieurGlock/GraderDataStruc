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
                t = t.next
            t.next = newNode
            newNode.prev = t
            
    
    def getSize(self):
        t = self.head
        count = 0
        while t:
            t = t.next
            count += 1
        return count
    
    def isEmpty(self):
        if self.getSize() == 0:
            return True
        else:
            return False

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
        if self.getSize() > 0:
            t = self.head
            while t.next != None:
                t = t.next
            return t
        else:
            return None

    def __str__(self):
        txt = ''
        t = self.head
        isStart = False
        while t:
            if isStart == True:
                txt += "->"
            txt += str(t.data)
            isStart = True
            
            t = t.next
        return txt

    def run(self,arg:str):
        inp = arg.split()
        for i in inp:
            if i == '+':
                x = int(self.pop())
                y = int(self.pop())
                self.append(x+y)
            elif i == '-':
                x = int(self.pop())
                y = int(self.pop())
                self.append(x-y)
            elif i == '*':
                x = int(self.pop())
                y = int(self.pop())
                self.append(x*y)
            elif i == '/':
                x = int(self.pop())
                y = int(self.pop())
                self.append(x/y)
            elif i == 'DUP':
                self.append(self.getTail().data)
            elif i == 'POP':
                self.pop()
            elif i == 'PSH':
                pass
            else:
                if i.isnumeric():
                    self.append(i)
                else:
                    self.txt = "Invalid instruction: {}".format(i)
                    return
        if self.getSize() == 0:
            self.txt = 0
        else:
            self.txt = int(self.getTail().data)

    def getValue(self):
        return self.txt
    
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = Link()
machine.run(arg)
print(machine.getValue())
            