def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)



someting = input("Enter text: ")

if is_palindrome(someting):
    print("Yes,it is a palindrome")
else:
    print("No, it is not a palindrome")
