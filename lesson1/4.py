def num_grid(lst):
    temp = []
    for i in lst:
        for j in range(len(i)):
            if i[j] != '#':
                i[j] = 0
            else:
                i[j] = 20
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] >= 20:
                
                # lst[i-1][j] ,lst[i+1][j] ,lst[i][j+1] ,lst[i][j-1] , lst[i+1][j+1], lst[i+1][j-1], lst[i-1][j+1], lst[i-1][j-1] += 1
                
                if i != 0:
                    lst[i-1][j] += 1
                if i != 4:
                    lst[i+1][j] += 1
                if j != 0:
                    lst[i][j-1] += 1
                if j != 4:
                    lst[i][j+1] += 1
                if i != 4 and j != 4:
                    lst[i+1][j+1] += 1
                if i != 4 and j != 0:
                    lst[i+1][j-1] += 1
                if i != 0 and j != 4:
                    lst[i-1][j+1] += 1
                if i != 0 and j != 0:
                    lst[i-1][j-1] += 1
    
    for i in lst:
        for j in range(len(i)):
            if i[j] >= 20:
                i[j] = '#'
            else:
                i[j] = str(i[j])


    return lst



# lst_input = [

#     ["-","-","-","-","-"],

#     ["-","-","-","-","-"],

#     ["-","-","#","-","-"],

#     ["-","-","-","-","-"],

#     ["-","-","-","-","-"]

# ]

lst_input = []
print("*** Minesweeper ***")
input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:

  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")