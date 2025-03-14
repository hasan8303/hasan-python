#write a program to check if the number is divisible by 3 or 5

a = int(input("enter the number"))

if a%3==0 or a%5==0:
    print("the number is divisible by 3 or 5")
else:
    print("the number is not divisible by 3 or 5")