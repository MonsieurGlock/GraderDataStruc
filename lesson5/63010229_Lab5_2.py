class Node():
    def __init__(self,data,next=None,prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class Link():
    def __init__(self, head = None) -> None:
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
    
    def insert(self,isAb,data,index = 0):
        """No index means addBefore"""
    
        if index == 0: #add before
            newNode = Node(data)
            if self.head == None:
                self.head = newNode
            else:
                self.head.prev = newNode #Make old head.prev point to newNode
                newNode.next = self.head #Make newNode.next point to old head
                self.head = newNode #Make new head
            if isAb == False:
                print("index = {} and data = {}".format(index,data))
        elif 0 < index < self.getSize():
            t = self.head
            for i in range(index - 1):
                if t.next != None:
                    t = t.next
            newNode = Node(data)
            newNode.next = t.next
            t.next.prev = newNode
            newNode.prev = t
            t.next = newNode
            print("index = {} and data = {}".format(index,data))
        elif index == self.getSize():
            newNode = Node(data)
            newNode.prev = self.getTail()
            self.getTail().next = newNode
            print("index = {} and data = {}".format(index,data))
        else:
            print("Data cannot be added")
    
    def remove(self,data):
        #No item
        countIndex = 0
        if self.getSize() != 0:
            t = self.head
            while t != None:
                if t.data == data:
                    
                    if t.prev != None:
                        t.prev.next = t.next
                    else:
                        self.head = t.next
                    if t.next != None:
                        t.next.prev = t.prev
                    del t
                    return "removed : {} from index : {}".format(data,countIndex)
                countIndex += 1
                t = t.next
            else:
                return "Not Found!"
        else:
            return "Not Found!"
            
                
            

    def str_reverse(self):
        t = self.getTail()
        txt = ''
        isStart = False
        while t:
            if isStart == True:
                txt += "->"
            txt += str(t.data)
            isStart = True
            
            t = t.prev
        return txt

inp = input("Enter Input : ").split(",")
li = Link()

for i in inp:
    if i.split()[0] == 'A':
        li.append(i.split()[1])
        print("linked list :",li.__str__())
        print("reverse :",li.str_reverse())
    elif i.split()[0] == 'Ab':
        li.insert(True,i.split()[1])
        print("linked list :",li.__str__())
        print("reverse :",li.str_reverse())
    elif i.split()[0] == 'I':
        li.insert(False,i.split()[1].split(":")[1], int(i.split()[1].split(":")[0]))
        print("linked list :",li.__str__())
        print("reverse :",li.str_reverse())
    elif i.split()[0] == 'R':
        print(li.remove(i.split()[1]))
        print("linked list :",li.__str__())
        print("reverse :",li.str_reverse())
