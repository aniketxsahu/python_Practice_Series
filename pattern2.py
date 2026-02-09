"""
WAP to print the following pattern

A
B B
C C C
D D D D
E E E E E
"""
num1=int((input("Enter the number of rows: ")))
for i in range(1,num1+1):
    for j in range(1, i + 1):
        print(chr(i+64), end=" ")
    print()