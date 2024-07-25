#largest of the three numbers

#x,y,z = input("enter the values what you want to give: ").split(",")
#a = int(x)
#b = int(y)
#c = int(z)

#if a > b:
 ##      print("a is gretest of all")
  #  else:
   #     print("not gretest of all")
#elif b > c:
 #   if b>c:
  #      print("b is greatest of all")
   # else:
    #    print("not-greater")
#else:
 #   print("c is greatest of all the numbers")


#swaroop said this way
a = input()
x,y,z = a.split(",")
num1 = int(x)
num2 = int(y)
num3 = int(z)
great = 0

if num1 > num2:
    if num1 > num3:
        great = num1
    else:
        great = num3
elif num2 > num1:
    if num2 > num3:
        great = num2
    else:
        great = num3
elif num3 > num1:
    if num3 > num2:
        great = num3
    else:
        great = num2
print(great)










































































































