# WAP to demonstrate various string operations in Python

str1="Aniket"
str2="Sahu"

print(str1+str2) # concatenation of str1 and str2
print(str1+" "+str2) # adds a space between str1 and str2
print(str1*3) # prints str1 three times

print(len(str1)) # prints the length of str1
print(str1[0]) # prints the first character of str1
print(str1[-1]) # prints the last character of str1
print(str1[1:4]) # prints characters from index 1 to 3 of str1
print(str1[1:5:2]) # prints every second character of str1
print(str1[::-1]) # reverses str1
print(str1[::2]) # prints every second character of str1

print(str1.lower()) # converts str1 to lowercase
print(str1.upper()) # converts str1 to uppercase
print(str1.capitalize()) # capitalizes the first character of str1
print(str1.count("a")) # counts occurrences of 'a' in str1
print(str1.replace("A", "E")) # replaces 'A' with 'E' in str1
print(str1.index("e")) # finds the index of 'e' in str1
print(str1.find("k")) # finds the index of 'k' in str1
print(str1.split("i")) # splits str1 at 'i' and returns a list

print(f"Welcome, {str1} {str2}!") # f-string formatted output
print(str1.isalpha()) # checks if str1 contains only alphabets
print(str1.isdigit()) # checks if str1 contains only digits
print(str1.startswith("A")) # checks if str1 starts with 'A'
print(str1.endswith("u")) # checks if str1 ends with 'u'



print(str1.strip("A")) # removes 'A' from both ends of str1
print(str1.title()) # converts str1 to title case
