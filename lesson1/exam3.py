

print(" *** String count ***")
inp = input("Enter message : ")

low = []
cLow = 0
up = []
cUp = 0
for i in inp:
    if i != " ":
        if i.islower():
            cLow += 1
            if i not in low:
                low.append(i)
        if i.isupper():
            cUp += 1
            if i not in up:
                up.append(i)
low.sort()
up.sort()

print("No. of Upper case characters :",cUp)
print("Unique Upper case characters : {}".format('  '.join(up)))
print("No. of Lower case Characters :",cLow)
print("Unique Lower case characters : {}".format('  '.join(low)))



