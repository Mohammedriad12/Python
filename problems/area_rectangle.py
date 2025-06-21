# # # 2.Area of a Rectangle
# # # Write a program that calculates the area of a rectangle. Take length and width as inputs.

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
