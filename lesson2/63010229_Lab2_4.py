
def hbd(age):

    ### Enter Your Code Here ###
    
    if age % 2 == 0:
        x = 20
        base = age / 2
    else: 
        x = 21
        base = age / 2

    return "saimai is just {}, in base {}!".format(x,int(base))

year = input("Enter year : ")

print(hbd(int(year)))


