
print("*** String Rotation ***")
x,y = input("Enter 2 strings : ").split()
s1,s2 = x,y
i = 1
s1 = s1[-1] + s1[:len(s1) -1]
s2 = s2[1:len(s2)] + s2[0]
print("{} {} {}".format(i,s1,s2))
while (s1 != x or s2 != y):
    i += 1
    s1 = s1[-1] + s1[:len(s1) -1]
    s2 = s2[1:len(s2)] + s2[0]
    if i <= 5:
        print("{} {} {}".format(i,s1,s2))
else:
    if i == 6:
        print("{} {} {}".format(i,s1,s2))
    elif i >= 5:
        print(" . . . . . ")
        print("{} {} {}".format(i,s1,s2))
print("Total of  {} rounds.".format(i))


# s2 = "456"
# s2 = s2[1:len(s2)] + s2[0]
# print(s2)
# s2 = s2[1:len(s2)] + s2[0]
# print(s2)
# s2 = s2[1:len(s2)] + s2[0]
# print(s2)
# s = "ABCDE"
# s = s[-1] + s[:len(s) -1]
# s = s[-1] + s[:len(s) -1]
# print(s)
# w = 'AB'
# if w == x:
#     print("yes")