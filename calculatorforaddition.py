#Ask for X
x = float(input("What is the first number? "))
#Ask for Y
y = float(input("What is your second number? "))
#Ask for how many places they want to round it off up to
b = int(input("How many digits would you want it to round off up to? Write in numbers."))
#Find Z
z = round((x + y),b)
#Print the function
print("Your number is", (f"{z:,}"))
