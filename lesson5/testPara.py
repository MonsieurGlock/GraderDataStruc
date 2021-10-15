
open = {'(':1 , '[':2}
close = {')':1 , ']':2}
def myCheck(li):
    stack = []
    for i in li:
        if i == '(' or i == '[':
            stack.append(i)
            # print(stack)
        else:
            if close[i] == open[stack[-1]]:
                stack.pop()
            else:
                print("No")
                break
    if len(stack) == 0:
        print("Yes")
    else:
        print("No")

# open_list = ["[","{","("]
# close_list = ["]","}",")"]
# def check(myStr):
#     stack = []
#     for i in myStr:
#         if i in open_list:
#             stack.append(i)
#         elif i in close_list:
#             pos = close_list.index(i)
#             if ((len(stack) > 0) and
#                 (open_list[pos] == stack[len(stack)-1])):
#                 stack.pop()
#             else:
#                 return "Unbalanced"
#     if len(stack) == 0:
#         return "Balanced"
#     else:
#         return "Unbalanced"

inp = input("Enter : ")

# print(check(inp))
# myCheck(inp)
li = [1,2]
print(li.pop())




