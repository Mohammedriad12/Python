# 1. Sum of Two Numbers
# Write a program that takes two numbers and prints their sum.
again = True

while again:
    num1 = float(input("Enter first number: "))
    num2 = float(input("enter second number: "))
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "is", sum)
    again = input("Do you want to add two more numbers? (Y/N): ")
    if again.lower() != 'y':
        again = False
        print("Thank you for using the program!")

# 2.Area of a Rectangle
# Write a program that calculates the area of a rectangle. Take length and width as inputs.

again = True
while again:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area =  2*(length * width) 
    print("the area is: ",area)
    again = input("Do you want to add two more numbers? (Y/N): ")
    if again.lower() != 'y':
        again = False
        print("Thank you for using the program!")

