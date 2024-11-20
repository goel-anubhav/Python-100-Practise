num = int(input("Enter the number To find it is Armstrong or not: "))
order = len(str(num))
sum = 0
temp = num
while temp>0:
    rem = temp%10
    sum = sum + rem**order
    temp = temp//10

if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")