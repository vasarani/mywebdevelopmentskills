#if-elif-statement
#W = input("Give W:")
#if W == "sunny":
 #   print("playing outdoor games")
#elif W == "rainy":
 #   print("playing indoor games")
#else:
 #   print("robotic games")
#print("Have Fun!")


#if-statement
#W = input("Give W:")
#if W == "sunny":
 #   print("playing outdoor games")


#if-else-statement
#W = input("Give W:")
#if W == "sunny":
#    print("playing outdoor games")

#else:
 #   print("robotic games")
#print("Have Fun!")


# if-elif- statement
#weather = input("enter what you want: ")
#time_of_day = input("Enter day time what you want:")

#if weather == "sunny":
 #   print("you can play with your liked toys")
#elif weather == "rainy":
 #   print("you can play with your boat toys")
#elif weather == "snowy" and time_of_day == "night":
  #  print("you can play with your indoor games")
#else:
 #   print("you can play with your robotics")

#print("have a great day hope all are good!")


#nested if-elif statement
weather = input("enter what you want: ")
time_of_day = input("Enter day time what you want:")

if weather == "sunny":
    if time_of_day == "day":
        print("you can play with your liked toys")
    else:
        print("cook food for everyone")
elif weather == "rainy":
    if time_of_day == "evening":
        print("you can play with your boat toys")
    else:
        print("enjoy your food by watching the view")
elif weather == "snowy": 
    if time_of_day == "night":
        print("you can play with your indoor games")
    else: 
        print("have your dinner yet")
else:
    print("you can play with your robotics")

print("have a great day hope all are good!")












































