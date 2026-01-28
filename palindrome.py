# WAP to print the input is a palindrome or not

word = input("Enter a word: ")
if word == word[::-1]:
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")