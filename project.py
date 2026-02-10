#Define Score
def score(X, answer):
    if answer == True:
        X = X + 5
    else:
        X = X + 0
    return X
#Greet the user with their name
print("Hello Contestant. Welcome to THE MATH TEST.")
name = input("What is your name? ")
print("Welcome", name + "!")
#Introduce the Questions
print("You will be given a question with 3 options out of which one is correct. There are 5 questions in total and each question carries 5 marks.")
X = 0
#First Question
print("---Your first question is")
print("Question - What is the product of '2Y' with '4'")
print("a = 5Y")
print("b = 8Y")
print("c = 4Y")

user_answer = input("What is the correct option 'a', 'b', 'c'? ")

if user_answer == "b":
    answer = True
else:
    answer = False
#Define Score
X = score(X, answer)
print("Your score is", X)
#Question 2
print("---Your next question is")
print("Question - What is the square root of '4 multiplied by 2 to the power 0'")
print("a = 0")
print("b = 8")
print("c = 4")
user_answer = input("What is the correct option 'a', 'b', 'c'? ")
if user_answer == "c":
    answer = True
else:
    answer = False
X = score(X, answer)
print("Your score is", X)
#Question 3
print("---Your next question is")
print("Question - What is the quotient of a dividend '4' by a divisor '0'")
print("a = undefined")
print("b = a fractional value")
print("c = very small value")
user_answer = input("What is the correct option 'a', 'b', 'c'? ")
if user_answer == "a":
    answer = True
else:
    answer = False
X = score(X, answer)
print("Your score is", X)
#Question 4
print("---Your next question is")
print("Question - Using which rule or law can you find the area of a triangle?")
print("a = Hero's Law")
print("b = Pythagoras Theorem")
print("c = Theorem of proportionality")
user_answer = input("What is the correct option 'a', 'b', 'c'? ")
if user_answer == "a":
    answer = True
else:
    answer = False
X = score(X, answer)
print("Your score is", X)
#Question 5
print("---Your next question is:")
print("Question - What is the value of 0 to the power 100")
print("a = undefined")
print("b = a fractional value")
print("c = 0")
user_answer = input("What is the correct option 'a', 'b', 'c'? ")
if user_answer == "c":
    answer = True
else:
    answer = False
X = score(X, answer)
print("Your score is", X)
#Show final score
print("\nYour total score is:", X)
#Condition
if 10 < X <= 25:
    print("You passed the test.YAY!")
else:
    print("You failed. Try Again.")
