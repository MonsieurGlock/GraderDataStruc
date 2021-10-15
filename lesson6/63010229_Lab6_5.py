

def staircase(n,i):
    if n == 0 and i == 0:
        return "Not Draw!"
    if n != 0:
        if n > 0:
            s=''
            s += ('_'*(n-1)) + ('#'*(i+1)) + '\n' + staircase(n-1,i+1)
            return s
        elif n < 0:
            s=''
            s += ('_'*(i)) + ('#'*(n*-1)) + '\n' + staircase(n+1,i+1)
            
            return s
    return ''
    
print(staircase(int(input("Enter Input : ")),0))




