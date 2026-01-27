# compare area and parameter of rectangle

length= int(input("Enter the length :"))
width = int(input("Enter the width :"))
area= length*width
para = 2*(length + width)
if(area>para):
    print("Area is greater")
else:
    print("parameter is greater")

