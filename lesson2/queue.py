from collections import deque

class Queue():
    def __init__(self , list = None ) -> None:
        # if list == None:
        #     self.item = []
        # else:
        #     self.item = list
        if list == None:
            self.item = deque()
        else:
            self.item = deque(list)
        

    def enQueue(self,i):
        self.item.append(i)
        
    def deQueue(self):
        return self.item.popleft()




if __name__ == "__main__":
    s = [i.split(" ") for i in input("Enter : ").split(",")]
    print(s)



