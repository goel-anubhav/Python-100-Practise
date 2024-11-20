a=0
b=1
num = int(input("Enter the number to get its fibonacci series: "))
print(a,b,end=" ")
for i in range(2,num+1):
    c=a+b
    a=b
    b=c
    print(c,end=" ")