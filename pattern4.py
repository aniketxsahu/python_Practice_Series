"""
WAP to print the following pattern

A A A A A
B B B B
C C C
D D
E
"""
num3=int((input("Enter the number of rows: ")))
for i in range(1, num3+1):
    for j in range(num3 - i + 1):
        print(chr(i + 64), end=" ")
    print()
    