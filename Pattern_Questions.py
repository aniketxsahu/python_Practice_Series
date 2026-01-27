"""
WAP to print the following pattern

A
A B
A B C
A B C D
A B C D E
"""
int((input("Enter the number of rows: ")))
for i in range(1, 6):
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
int((input("Enter the number of rows: ")))
for i in range(1, 6):
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
int((input("Enter the number of rows: ")))
for i in range(1, 6):
    for j in range(1, i + 1):
        print(chr((i*(i-1))//2 + j + 64), end=" ")
    print()
