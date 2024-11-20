num = int(input("Enter the number to find its sum from 0: "))
sum = 0
for i in range(1, num +1):
    sum = sum + i
    num = num -1
    print("The Sum of all the digits are : ",sum)