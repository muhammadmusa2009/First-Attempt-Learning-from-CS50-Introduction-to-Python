#Greet
greeting = input("Greeting:").strip().lower()
if greeting.startswith("hello" or "hello!" or "hello !"):
    print("The bank gives you nothing.")
elif greeting.startswith("h"):
    print("You're given $20 by the bank.")
else:
    print("You're given $100 by the bank.")
