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
    