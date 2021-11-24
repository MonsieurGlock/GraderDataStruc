inp = [int(x) for x in input("Enter Input : ").split()]
check = False
picker = []
for i in range(len(inp)):
    check = False
    for j in range(0, len(inp)-i-1):
        if inp[j] > inp[j+1]:
            check = True
            picker.append(inp[j])
            inp[j], inp[j+1] = inp[j+1], inp[j]

    if check == True and len(inp)-2 == i:
        print(f"last step : {inp[:]}", end=" ")
        print(f"move[{picker[-1]}]")
    elif check == False and len(inp)-2 == i:
        print(f"last step : {inp[:]}", end=" ")
        print(f"move[None]")
    elif check == True:
        print(f"{i+1} step : {inp[:]}", end=" ")
        print(f"move[{picker[-1]}]")
    picker.clear()