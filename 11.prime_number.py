a=int(input("Enter the number to check prime or not: "))
if a==1:
        print("It is not a prime number")
elif a>1:
        for i in range(2,a):
            if a%i==0:
                print("It is not a prime number")
                break
        else:
            print("It is a prime number")
else:
        print("It is not a prime number")