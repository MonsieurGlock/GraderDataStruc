def top(x):
    for i in range(1+x):
        print(".",end="")
    print("#",end="")
    for i in range(2+x):
        print("+",end="")
    print("")

def up(x):
    for row in range(x):
        for i in range(x-row):
            print(".",end="")
        for i in range(row+2):
            print("#",end="")
        print("+",end="")
        for i in range(x):
            print("#",end="")
        print("+")
          
def middle(x):
    for row in range(2):
        for i in range(x+2):
            print("#",end="")
        for i in range(x+2):
            print("+",end="")
                 
        print("")

def down(x):
    for row in range(x):
        print("#",end="")
        for i in range(x):
            print("+",end="")
        
        print("#",end="")
        for i in range(x-row+1):
            print("+",end="")
        for i in range(row+1):
            print(".",end="")   
        
        print("")

def bottom(x):
    for i in range(x+2):
        print("#",end="")
    print("+",end="")
    for i in range(1+x):
        print(".",end="")
    print("")

x = int(input("Enter Input : "))

num = 6+(x*2)
top(x)
up(x)
middle(x)
down(x)
bottom(x)
