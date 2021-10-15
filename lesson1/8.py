def vote(inp:list):
    max = 0
    win = 0
    i = 0
    for i in inp:
        if inp.count(i) > max:
            max = inp.count(i)
            win = i
        inp.remove(i)
    print("Winner is {} :: Score {}".format(win,max))



inp = [int(i) for i in input("Enter : ").split()]
vote(inp)