class Queue():
    def __init__(self) -> None:
        self.items = []

    def enQueue(self,data):
        self.items.append(data)
        print(self.items)

    def deQueue(self):
        if self.isEmpty() == False:
            return self.items.pop(0)

    def isEmpty(self):
        if len(self.items) > 0:
            return False
        else:
            return True

inp = input("Enter code,hint : ").split(",")
key = ord(inp[1][0]) - ord(inp[0][0])
q = Queue()
for txt in inp[0]:
    q.enQueue(chr(ord(txt) + key))

