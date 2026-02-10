def is_even(n):
    return True if n%2 == 0 else False
x = int(input("What is your number? "))
if is_even(x):
    print("The number is even.")
else:
    print("The number is odd.")
