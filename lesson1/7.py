def change(num):
    answer = [[]]
    for n in num:
        temp = []
        for m in answer:
            for i in range(len(m)+1):
                temp.append(m[:i] + [n] + m[i:])
                answer = temp
        
    return answer

# inp = input("Enter : ").split()
# print(change(inp))
print(type(0))