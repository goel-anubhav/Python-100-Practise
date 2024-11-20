a=int(input("Enter The First Number: "))
b=int(input("Enter The Second Number: "))
c=int(input("Enter The Third Number: "))
if a>b and a>c:
    print(a,"is the largest number among",a,b,c)
elif b>a and b>c:
    print(b,"is the largest number among",a,b,c)
elif c>a and c>b:
    print(c,"is the largest number among",a,b,c)
else:
    print("All 3 digits are equal",a,b,c)
