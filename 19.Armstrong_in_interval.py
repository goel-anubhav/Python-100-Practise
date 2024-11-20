lower=int(input("Enter the lower limit: "))
upper=int(input("Enter the upper limit: "))
for i in range(lower,upper+1):
    order=len(str(i))
    sum=0
    temp = i
    while temp>0:
        rem = temp%10
        sum = sum + rem ** order
        temp = temp//10
    if i == sum:
        print("All The Armstrong Numbers between",lower,"and",upper,"are: ", i)
    else:
        continue