"""
WAP to print the following pattern   

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
num2=int((input("Enter the number of rows: ")))
for i in range(1, num2+1):
    for j in range(1,num2-i+1):
        print(" ", end=" ")
    for k in range(1, 2*i):
        print("*", end=" ")
    print()