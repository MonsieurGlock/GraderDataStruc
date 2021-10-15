print(" *** Wind classification ***")
n = float(input("Enter wind speed (km/h) : "))

if n >= 0:
    if n >= 209:
        w = "Super Typhoon"
    elif n >= 102:
        w = "Typhoon"
    elif n >= 56:
        w = "Tropical Storm"
    elif n >= 52:
        w = "Depression"
    elif n >= 0:
        w = "Breeze"
    print("Wind classification is {}.".format(w))
else:
    print("!!!Wrong value can't classify.")




