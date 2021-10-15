class MyInt:
    def __init__(self, value):
        self.value = value

    def toRoman(self):
        roman = {1000: "M",900: "CM", 500: "D",400: "CD",100: "C",90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        temp = self.value
        out = ""
        listvalues = find_value(temp)
        # print(listvalues)
        for i in listvalues:
            out += roman[i]
        return out

    def __add__(self, other):
        ans = self.value+other.value
        ans = ans+(ans/2)
        return int(ans)


def find_value(value):
    s = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    listout = []
    index = 0
    while value != 0:
        if s[index] > value:
            index += 1
        elif s[index] <= value:
            value = value-s[index]
            listout.append(s[index])
    return listout


print(" *** class MyInt ***")
a, b = input("Enter 2 number : ").split()

a = MyInt(int(a))
b = MyInt(int(b))
print(f"{a.value} convert to Roman : ", end="")
print(a.toRoman())
print(f"{b.value} convert to Roman : ", end="")
print(b.toRoman())
# print(find_value(5320))
print(f"{a.value} + {b.value} = ", end="")
print(a+b)