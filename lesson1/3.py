def change(num):
    answer = [[]]
    for n in num:
        temp = []
        for m in answer:
            # print(m)
            for i in range(len(m)+1):
                temp.append(m[:i] + [n] + m[i:])
                answer = temp
        
    return answer

print("*** Fun with permute ***")
num = input("input : ").split(',')
for i in range(len(num)):
    num[i] = int(num[i])
print("Original Cofllection: ",num)
print("Collection of distinct numbers:\n",change(num))