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