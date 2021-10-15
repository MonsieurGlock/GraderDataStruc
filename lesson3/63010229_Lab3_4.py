class Stack :

    def __init__(self) :
        self.items = []
        
    def isEmpty(self) :
        if len(self.items) <= 0:
            return True
        else:
            return False
    def push(self,data) :
        self.items.append(data)
    def pop(self) :
        return self.items.pop()
    def size(self) :
        return len(self.items)
    def peek(self)->str:
        return self.items[-1]

# def operatorValue(ope:str):
#     if ope == '+' or ope =='-':
#         print("Value work")
#         return 1
#     elif ope == '*' or ope =='/':
#         return 2
#     elif ope == '^':
#         return 3

operatorValue ={'+':1, '-':1, '*':2, '/':2, '^':3, '(':0}

def isWord(x:str)->bool:
    if x == '+'or x == '-'or x == '*'or x == '/'or x == '^':
        # print("isWord false")
        return False
    else:
        # print("isWord true")
        return True



def infix2postfix(exp:str) :

    s = Stack() #Answer
    operator = Stack()
    for i in exp:
        if isWord(i):
            if i ==')':
                pass
                while len(operator.items) != 0 and operator.peek() != '(':
                    s.push(operator.pop())
                else:
                    # pass
                    operator.pop()
            elif i == '(':
                operator.push(i)
            else:
                s.push(i)
        else:
            
            if operator.isEmpty() == True:
                
                operator.push(i)
                
            elif len(operator.items) != 0 and operatorValue[i] > operatorValue[operator.peek()]:
                
                operator.push(i)
            else:

                while len(operator.items) != 0 and operatorValue[i] <= operatorValue[operator.peek()]:
                    
                    s.push(operator.pop())
                else:
                    operator.push(i)
        # print(i)
        # print(s.items)
        # print(operator.items)
    while not operator.isEmpty():
        s.push(operator.pop())
    answer = ''.join(s.items)
    return answer


print(" ***Infix to Postfix***")

token = input("Enter Infix expression : ")

print("PostFix : ")

print(infix2postfix(token))
# print('+' == '+' or)