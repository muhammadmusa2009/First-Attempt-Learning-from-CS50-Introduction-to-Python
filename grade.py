print("Welcome to marks to grade converter.")

x = float(input("What are the total marks of the test?"))
y = float(input("What were the marks obtained?"))

z = round((y/x), 4) * 100

print ("Percentage is:", z, "%")

if (100 >= z >= 95):
    print("Your Grade is A+")
elif(95 > z >= 90):
    print("Your Grade is A")
elif(90 > z >= 85):
    print("Your Grade is B+")
elif(85 > z >= 80):
    print("Your Grade is B")
elif(80 > z >= 75):
    print("Your Grade is C+")
elif(75 > z >= 70):
    print("Your Grade is C")
elif(70 > z >= 65):
    print("Your Grade is D")
elif(65 > z >= 60):
    print("Your Grade is D-")
else:
    print("You're fail. :(")
print("-----------------------")
