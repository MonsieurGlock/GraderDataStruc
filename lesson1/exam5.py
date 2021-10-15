class MyInt:
    def __init__(self,num) -> None:
        self.num = num
        
    def toRoman(self):
        s = ''
        temp = self.num
        while self.num != 0:
            if self.num >= 1000:
                s += "M"
                self.num -= 1000
            elif self.num >= 900:
                s += "CM"
                self.num -= 900
            elif self.num >= 500:
                s += "D"
                self.num -= 500
            elif self.num >= 400:
                s += "CD"
                self.num -= 400
            elif self.num >= 100:
                s += "C"
                self.num -= 100
            elif self.num >= 90:
                s += "XC"
                self.num -= 90
            elif self.num >= 50:
                s += "L"
                self.num -= 50
            elif self.num >= 40:
                s += "XL"
                self.num -= 40
            elif self.num >= 10:
                s += "X"
                self.num -= 10
            elif self.num >= 9:
                s += "IX"
                self.num -= 9
            elif self.num >= 5:
                s += "V"
                self.num -= 5
            elif self.num >= 4:
                s += "IV"
                self.num -= 4
            elif self.num >= 1:
                s += "I"
                self.num -= 1
        self.num = temp
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
# print(a.toRoman())
# print(b.toRoman())
# print(a+b)
# "M" = 1000
# "CM" = 900
# "D" = 500
# "CD" = 400
# "C" = 100
# "XC" = 90
# "L" = 50
# "XL" = 40
# "X" = 10
# "IX" = 9
# "V" = 5
# "IV" = 4
# "I" = 1

