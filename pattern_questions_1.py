"""
WAP to print the following pattern   

*
**
***
*****
****** 

"""
int((input("Enter the number of rows: ")))
for i in range(1, 7):
    for j in range(1, i + 1):
        print("*", end="")
    print()