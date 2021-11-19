
def harmonic_sum(n,i,sum):
    if i == n+1:
        return sum
    if i == 1:
        print("1",end='')
    else:
        print(" + 1/{}".format(i),end='')
    sum += 1/i 
    return harmonic_sum(n,i+1,sum)

print(" *** Harmonic sum ***")
num = int(input("Enter number of terms : ")) 
print(" = %.8f" %(harmonic_sum(num,1,0)))

