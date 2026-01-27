# WAP to print Fibonacci series up to n terms 

previous= -1
next= 1
fibo= int(input("How many terms?:")) # User input
i=1
while i<=fibo:
    sum = previous + next
    print(sum, end=' ')
    previous= next
    next = sum
    i+=1
    