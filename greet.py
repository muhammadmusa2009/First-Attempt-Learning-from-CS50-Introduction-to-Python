#Greet the brother
print("Hello, Brutha.")
#Ask their name
name = input("What's your name? ")
#Strip the user's name and capitalize it
name = name.strip().title()
#Split
first, last = name.split(" ")
#Greet them with name
print(f"Hello, {first}")
