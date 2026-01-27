# WAP to print the number is Prime or Not Prime

num = int(input("Enter a number: ")) # User input
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "is Not a Prime number")
            break
    else:
        print(num, "is a Prime number")