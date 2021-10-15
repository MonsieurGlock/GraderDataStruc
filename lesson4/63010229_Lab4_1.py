


class Queue():
    def __init__(self) -> None:
        self.items = []

    def enQueue(self,data):
        self.items.append(data)
        print("Add {} index is {}".format(data,len(self.items) - 1))

    def deQueue(self):
        if self.isEmpty():
            print(-1)
        else:
            print("Pop {} size in queue is {}".format(self.items[0], len(self.items)-1))
            self.items.pop(0)

    def isEmpty(self):
        if len(self.items) > 0:
            return False
        else:
            return True


inp = [i.split() for i in input("Enter Input : ").split(",")]
q = Queue()

for l in inp:
    if l[0] == 'E':
        q.enQueue(l[1])
    if l[0] == 'D':
        q.deQueue()

if q.isEmpty():
    print("Empty")
else:
    print("Number in Queue is :  {}".format(q.items))


