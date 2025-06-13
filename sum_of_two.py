# # # 1. Sum of Two Numbers
# # # Write a program that takes two numbers and prints their sum.
# # again = True

while again:
    num1 = float(input("Enter first number: "))
    num2 = float(input("enter second number: "))
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "is", sum)
    again = input("Do you want to add two more numbers? (Y/N): ")
    if again.lower() != 'y':
        again = False
        print("Thank you for using the program!")
