"""
WAP to print the following pattern

A
A B
A B C
A B C D
A B C D E
"""
num=int((input("Enter the number of rows: ")))
for i in range(1, num+1):
    for j in range(1, i + 1):
        print(chr(j+64), end=" ")
    print()