# This is using expression in factorial
# fact = int(input("Enter the number to find its factorial: "))
# factorial = 1
# for i in range(1, fact+1):
#     if fact ==0:
#         print("Factorial of 0 is 1")
#     elif fact<0:
#         print("Factorial of a negative number is not defined")
#     else:
#         factorial = factorial*i
# print("The factorial of",fact,"is",factorial)

# Method 2 by using recursion

def fact(n):
    if n==0:
        return 1
    else:
        return (n*fact(n-1))
num = int(input("Enter the number to find its factorial: "))
print("The factorial is",fact(num))