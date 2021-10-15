
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

    def operation(self,ls):
        # print(ls)
        for i in ls:
            if i[0] == 'A':
                self.push(int(i[2:]))
                print("Add =",int(i[2:]))
                
            elif i == 'P':
                if self.isEmpty() == False:
                    
                    print("Pop =",self.pop())
                else:
                    print("-1")

            elif i[0] == 'D':
                if len(self.items) == 0:
                    print("-1")
                temp = []
                for ls in self.items: # Add to list temp
                    if ls == int(i[2:]):
                        temp.append(ls)
                # if len(temp) == 0: For no
                #     print("-1")
                for j in temp:
                    self.items.remove(j)
                    print("Delete =",j) 

            elif i[0:2] == 'LD':
                if len(self.items) == 0:
                    print("-1")
                temp = []
                for ls in self.items: # Add to list temp
                    if ls < int(i[3:]):
                        temp.append(ls)
                temp.reverse()
                for j in temp:
                    self.items.remove(j)
                    print("Delete = {} Because {} is less than {}".format(j,j,int(i[3:])))
                
                
            elif i[0:2] == 'MD':
                if len(self.items) == 0:
                    print("-1")
                temp = []
                for ls in self.items: # Add to list temp
                    if ls > int(i[3:]):
                        temp.append(ls)
                # if len(temp) == 0: For no
                #     print("-1")
                for j in temp:
                    self.items.remove(j)
                    print("Delete = {} Because {} is more than {}".format(j,j,int(i[3:])))
                
                
        print("Value in Stack =",self.items)






if __name__=="__main__":
    ls = input("Enter Input : ").split(",")
    s = Stack()
    s.operation(ls)




