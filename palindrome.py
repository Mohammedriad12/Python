# #4. Palindrome Checker
# # Write a function is_palindrome(word) that checks if a string is a palindrome (same forward and backward).

def palindrome(args):
    rev = args[::-1]
    if args == rev:
        return True
    else:
        return False

print(palindrome("madam"))  # True
print(palindrome("hello"))  # False

