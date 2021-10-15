
class Stack():
    def __init__(self ,) -> None:
        self.items = []
    
    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        
        return True if self.items.__len__() == 0 else False 

    def size(self):
        return self.items.__len__()





if __name__=="__main__":
    print(" *** Stack implement by Python list***")
    ls = [e for e in input("Enter data to stack : ").split()]
    s = Stack()

    for e in ls:
        s.push(e)

    print(s.size(),"Data in stack : ",s.items)

    while not s.isEmpty():

        s.pop()

    print(s.size(),"Data in stack : ",s.items)



