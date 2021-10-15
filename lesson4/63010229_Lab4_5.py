class Queue():
    def __init__(self,inp) -> None:
        self.items = inp
        self.exp = 0

    def enQueue(self,data):
        self.items.append(data)

    def deQueue(self):
        if self.isEmpty() == False:
            return self.items.pop(0)

    def isEmpty(self):
        if len(self.items) > 0:
            return False
        else:
            return True
def count(S:list):
    temp = ''
    count = 0
    combo = 0
    fail = 0
    result = []
    i=0
    while i < len(S):
        if S[i][0] != temp:
            count = 0
            temp = S[i][0]
        else:
            count += 1
        
        if count == 2:
            result.append(S[i])
            for r in range(3):
                # print("r =",r)
                if len(S[i-2]) > 1:
                    fail += 1
                S.pop(i-2)
            combo += 1
            i = 0
            count = 0
            continue
        i += 1
    
    return [result,S,fail]

def cat(c:list,normal:list):
    temp = ''
    count = 0
    i=0
    num = 0
    while i < len(normal):
        if normal[i] != temp:
            count = 0
            temp = normal[i]
        else:
            count += 1
        
        if count == 2:
            if num < len(c):
                normal.insert(i,c[num]+ '-')
                num += 1
                temp = ''
            count = 0
            continue
        i += 1
    return normal



def main(inp:list):
    normalQ = Queue([i for i in inp[0]])
    # print(normalQ.items)
    mirrorQ = Queue([i for i in inp[1]])
    # print(mirrorQ.items)
    mirrorQ.items.reverse()
    mirResult = count(mirrorQ.items)
    # mirResult[0].reverse()
    # print(mirResult[0])
    
    # normalQ.items.reverse()
    x = cat(mirResult[0] , normalQ.items)
    normalResult = count(x)
    normalResult[1].reverse()
    for i in range(len(normalResult[1])):
        if len(normalResult[1][i]) > 1:
            normalResult[1][i] = normalResult[1][i][0]
    
    # normalResult[1].reverse()

    #display
    print("NORMAL :")
    print(len(normalResult[1]))
    if len(normalResult[1]) == 0:
        print("Empty")
    else:
        print(''.join(normalResult[1]))
    if normalResult[2] == 0:
        print("{} Explosive(s) ! ! ! (NORMAL)".format(len(normalResult[0])))
    else: 
        print("{} Explosive(s) ! ! ! (NORMAL)".format(len(normalResult[0]) - normalResult[2]))
        print("Failed Interrupted {} Bomb(s)".format(normalResult[2]))
    print("------------MIRROR------------")
    print(": RORRIM")
    print(len(mirResult[1]))
    mirResult[1].reverse()
    if len(mirResult[1]) == 0:
        print("ytpmE")
    else:
       print(''.join(mirResult[1]))
    print("(RORRIM) ! ! ! (s)evisolpxE {}".format(len(mirResult[0])))



inp = input("Enter Input (Normal, Mirror) : ").split()
main(inp)

