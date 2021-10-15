class Queue():
    def __init__(self) -> None:
        self.items = []

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

def active(a):
    active = {
        "0":"Eat",
        "1":"Game",
        "2":"Learn",
        "3":"Movie"
    }
    return active[a]

def location(l):
    loc = {
        "0":"Res.",
        "1":"ClassR.",
        "2":"SuperM.",
        "3":"Home"
    }
    return loc[l]

def result(score:int):
    if score >= 7:
        word = "Yes! You're my love!"
    elif 0 < score < 7:
        word = "Umm.. It's complicated relationship!"
    else:
        word = "No! We're just friends."
    print("{} : Score is {}.".format(word,score))


def calRelation(inp:list):
    myQ = Queue()
    hisQ = Queue()
    myWord = []
    hisWord = []
    score = 0
    for l in inp:#make queue
        # l.split()[0]
        myQ.enQueue(l.split()[0])
        hisQ.enQueue(l.split()[1])
    for i in range(len(myQ.items)):
        if int(myQ.items[i].split(":")[0]) == int(hisQ.items[i].split(":")[0]) and int(myQ.items[i].split(":")[1]) != int(hisQ.items[i].split(":")[1]):
            score += 1
        elif  int(myQ.items[i].split(":")[0]) != int(hisQ.items[i].split(":")[0]) and int(myQ.items[i].split(":")[1]) == int(hisQ.items[i].split(":")[1]):
            score += 2
        elif int(myQ.items[i].split(":")[0]) == int(hisQ.items[i].split(":")[0]) and int(myQ.items[i].split(":")[1]) == int(hisQ.items[i].split(":")[1]):
            score += 4
        else:
            score -= 5
        #Make string
        myWord.append(active(myQ.items[i].split(":")[0]) + ':' +location(myQ.items[i].split(":")[1]))
        hisWord.append(active(hisQ.items[i].split(":")[0]) + ':' +location(hisQ.items[i].split(":")[1]))
    
    print("My   Queue =",', '.join(myQ.items))
    print("Your Queue =",', '.join(hisQ.items))
    print("My   Activity:Location =",', '.join(myWord))
    print("Your Activity:Location =",', '.join(hisWord))
    result(score)

inp = input("Enter Input : ").split(",")
calRelation(inp)
# print(', '.join(myQ.items))



