
def run(inp,n, l):
    if n == 0:
        if len(l) == 0:
            print(0)
        else:
            a=[]
            res = ""
            if len(bin(n)[2:])<inp:
                res=("0"*(inp-len(bin(n)[2:])))+bin(n)[2:]
            else:
                res=bin(n)[2:]
            a.append(res)          
            print('\n'.join((a+l)))
    else:
        if len(l) == 0:
            return run(inp,n - 1, [bin(n)[2:]])
        else:
            a=[]
            res = ""
            if len(bin(n)[2:])<inp:
                res=("0"*(inp-len(bin(n)[2:])))+bin(n)[2:]
            else:
                res=bin(n)[2:]
            a.append(res)
            return run(inp,n - 1, a+l)


inp = int(input('Enter Number : '))
if inp < 0:
    print('Only Positive & Zero Number ! ! !')
else:
    run(inp,(2**inp) -1, [])