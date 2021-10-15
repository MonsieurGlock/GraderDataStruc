h,w = input("Enter your High and Weight : ").split()
h = float(h)
w = float(w)

bmi = w/(h*h)

if bmi >= 30:
    text = "Fat"
elif bmi >= 25:
    text = "Getting Fat"
elif bmi >= 23:
    text = "More than Normal Weight"
elif bmi >= 18.50:
    text = "Normal Weight"
else:
    text = "Less Weight"
print(text)