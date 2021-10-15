
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


'''
size
search
index
insert
pop(position)
append
add
'''
open = {'(':1 , '[':2}
close = {')':1 , ']':2}
def para(str):
    stack = Link()
    for i in str:
        if i in open:
            stack.add(i)
            
        else:
            if stack.getSize() > 0 and close[i] == open[stack.getTail().data]:
                stack.pop()
            else:
                return "Unmatched ! ! !"
    if stack.getSize() == 0:
        return "Matched ! ! !"
    else:
        return "Unmatched ! ! !"
                
        

    
inp = input("Enter Input : ")
print("Parentheses :",para(inp))
# # l.show()
# a = l.head
# temp = a.data
# isPara = True
# while a:
#     a = a.next
#     if (temp == '(' and a.data == ')') or (temp == '[' and a.data == ']'):
#         # print("===",a.data)
#         a = a.next
#         if a != None:
#             temp = a.data
#     else:
#         isPara = False
#         print("Parentheses : Unmatched ! ! !")
#         break
# if isPara == True:
#     print("Parentheses : Matched ! ! !")







