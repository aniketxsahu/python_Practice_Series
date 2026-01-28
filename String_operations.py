# WAP to reverse a string
str1 = input("Enter a string:")
reversed_str = str1[::-1]
print("Reversed string is:", reversed_str)

# WAP to check if a string is a palindrome
if str1 == reversed_str:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
# WAP to count the number of vowels in a string
vowels = "aeiouAEIOU"
count = 0
for char in str1:
    if char in vowels:
        count += 1  
        print("Number of vowels in the string is:", count)
        
# WAP to count the number of words in a string
words = str1.split()
print("Number of words in the string is:", len(words))

# WAP to convert a string to uppercase
upper_str = str1.upper()  
print("String in uppercase is:", upper_str)

# WAP to convert a string to lowercase
lower_str = str1.lower()  
print("String in lowercase is:", lower_str)

# WAP to replace a substring in a string
substr = input("Enter the substring to be replaced: ")
new_substr = input("Enter the new substring: ")
replaced_str = str1.replace(substr, new_substr)
print("String after replacement is:", replaced_str) 

# WAP to find the length of a string
length = len(str1)
print("Length of the string is:", length)

# WAP to count the occurrence of a character in a string
char_to_count = input("Enter the character to count: ")
count_char = str1.count(char_to_count)
print("The character", char_to_count, "occurs", count_char, "times in the string.")

# WAP to check if a string contains only alphabets
if str1.isalpha():
    print("The string contains only alphabets.")
else:
    print("The string does not contain only alphabets.")
    
# WAP to check if a string contains only digits
if str1.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
    
