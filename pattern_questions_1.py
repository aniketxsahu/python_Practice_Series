"""
WAP to print the following pattern   

*
* *
* * *
* * * *
* * * * *
* * * * * *

"""
num1=int((input("Enter the number of rows: ")))
for i in range(1, num1+1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

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
    
"""
WAP to print the following pattern 

     *
    * *
   * * *
  * * * *
 * * * * *
* * * * * *
"""
num3=int((input("Enter the number of rows: ")))
for i in range(1, num3+1):
    for j in range(1, num3-i+1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(" * ", end=" ")
    print()

"""
WAP to print the following pattern 

     *
    * *
   * * *
  * * * *
 * * * * *
* * * * * *
* * * * * *
  * * * * 
   * * * 
    * * 
     *        
"""

num4=int((input("Enter the number of rows: ")))
for i in range(1, num4+1):
    for j in range(1, num4-i+1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(" * ", end=" ")
    print()
for i in range(num4-1, 0, -1):
    for j in range(1, num4-i+1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(" * ", end=" ")
    print()