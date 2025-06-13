# # # 1. Sum of Two Numbers
# # # Write a program that takes two numbers and prints their sum.
# # again = True

# while again:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("enter second number: "))
#     sum = num1 + num2
#     print("The sum of", num1, "and", num2, "is", sum)
#     again = input("Do you want to add two more numbers? (Y/N): ")
#     if again.lower() != 'y':
#         again = False
#         print("Thank you for using the program!")

# # # 2.Area of a Rectangle
# # # Write a program that calculates the area of a rectangle. Take length and width as inputs.

# again = True
# while again:
#     length = int(input("Enter length: "))
#     width = int(input("Enter width: "))
#     area =  2*(length * width) 
#     print("the area is: ",area)
#     again = input("Do you want to add two more numbers? (Y/N): ")
#     if again.lower() != 'y':
#         again = False
#         print("Thank you for using the program!")

# #3.Factorial of a Number using a function 
# # Write a program that calculates the factorial of a given number using a loop.

# def factorial(n):
#     i = 1
#     for start in range(1,n+1):
#         i *= start
#     return i

# fun =int(input("Enter the number for the function: "))
# print(factorial(fun))

# #4. Palindrome Checker
# # Write a function is_palindrome(word) that checks if a string is a palindrome (same forward and backward).

# def palindrome(args):
#     rev = args[::-1]
#     if args == rev:
#         return True
#     else:
#         return False

# print(palindrome("madam"))  # True
# print(palindrome("hello"))  # False