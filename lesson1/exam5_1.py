class MyInt:
    
    def __init__(self,num) -> None:
        self.num = num
        
    def toRoman(self):
        roman = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        s = ''
        temp = self.num
        while temp != 0:
            for i in roman:
                if temp >= i:
                    s += roman[i]*int(temp/i)
                    temp -= i*int(temp/i)
                    break
        
        return "{} convert to Roman : {}".format(self.num,s)
    def __add__(self,cat):
        sum = self.num + cat.num
        sum += (sum/2)
        return "{} + {} = {}".format(self.num,cat.num,int(sum))

print(" *** class MyInt ***")
inp = input("Enter 2 number : ").split()
a = MyInt(int(inp[0]))
b = MyInt(int(inp[1]))
print(a.toRoman())
print(b.toRoman())
print(a+b)


