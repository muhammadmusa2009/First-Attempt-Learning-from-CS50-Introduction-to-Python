#Creat a default greeting
def Default(pop = "Welcome"):
    print(pop)
#Create a function
def Greet(to):
    print("Hello,", to)
#Welcome the user
Default()
#Ask the user for their name
name = input("What is your name? ")
#Strip it of free spaces and capitalize
name = name.strip().title()
#Print the name
Greet(name)
