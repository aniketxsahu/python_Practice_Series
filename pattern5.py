
"""
WAP to print the following pattern

A B C D E
B C D E
C D E
D E
E
"""
num4=int((input("Enter the number of rows: ")))
for i in range(1, num4+1):
    for j in range(i, num4 + 1):
        print(chr(j + 64), end=" ")
    print()