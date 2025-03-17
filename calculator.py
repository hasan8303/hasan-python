a = int(input("enter the first number"))
b = int(input("enter the second number"))
print("choose 1 for addition")
print("choose 2 for subtraction")
print("choose 3 for division ")
print("choose 4 for multiply")
option = int(input("enter the option"))

if option ==1:
   sum = a+b
   print(sum)
elif option ==2:
   subtract = a-b
   print(subtract)
elif option ==3:
   division = a/b
   print(division)
elif option ==4:
   multiply = a*b
   print(multiply)
else:
   print("error")