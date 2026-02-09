"""
WAP to print the following pattern

A
B C
D E F
G H I J
K L M N O
"""
num2= int((input("Enter the number of rows: ")))
for i in range(1, num2+1):
    for j in range(1, i + 1):
        print(chr((i*(i-1))//2 + j + 64), end=" ")
    print()
