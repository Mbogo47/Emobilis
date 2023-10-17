# IF STATEMENTS
# A program that checks whether if a number is 0 even or negative
number = int(input("Enter a number? \n"))

if number == 0 :
    print(f"{number} is zero")
elif number < 0 :
    print(f"{number} is negative")
else:
    print(f"{number} is positive")