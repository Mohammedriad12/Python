#Use a for loop to find the largest number in the list without using max().
def max_num(numbers):
    max_val = numbers[0]
    for i in range(1,len(numbers)):
        if (max_val < numbers[i]):
            max_val = numbers[i]
    return max_val

numbers = [13,2,3,4,69,10]
print(max_num(numbers))
