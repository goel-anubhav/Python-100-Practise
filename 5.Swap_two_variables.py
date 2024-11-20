# Method 1 by using third variable
a=int(input("Enter The First Number: "))
b=int(input("Enter The Second Number: "))
# c=a
# a=b
# b=c
# print("The First Number is: ",a)
# print("The Second Number is: ",b)

# Method 2 Without using third variable
a,b = b,a
print("The First Number is: ",a)
print("The Second Number is: ",b)