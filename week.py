#write a program which takes numbers from 1 to 7 as input and print week day name from mon to sun

a = int(input("enter the first number"))

if a==1:
    print("today is monday")
elif a==2:
    print("today is tuesday")
elif a==3:
    print("today is wednesday")
elif a==4:
    print("today is tuhrsday")
elif a==5:
    print("today is friday")
elif a==6:
    print("today is saturday")
elif a==7:
    print("today is sunday")
else:
    print("a week has only 7 days")