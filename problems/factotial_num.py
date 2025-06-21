# #3.Factorial of a Number using a function 
# # Write a program that calculates the factorial of a given number using a loop.

def factorial(n):
    i = 1
    for start in range(1,n+1):
        i *= start
    return i

fun =int(input("Enter the number for the function: "))
print(factorial(fun))
